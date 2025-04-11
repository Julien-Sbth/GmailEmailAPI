from datetime import datetime, timedelta
from utils.config import EMAIL_QUERY, PROCESSING_CONFIG
import logging

logger = logging.getLogger(__name__)

def fetch_all_emails(service, query, days=PROCESSING_CONFIG['days_to_search']):
    all_messages = []
    page_token = None
    after_date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')

    full_query = f"{query} after:{after_date}"
    logger.info(f"Exécution de la requête: {full_query}")

    while True:
        try:
            results = service.users().messages().list(
                userId='me',
                q=full_query,
                maxResults=500,
                pageToken=page_token
            ).execute()

            messages = results.get('messages', [])
            all_messages.extend(messages)

            page_token = results.get('nextPageToken')
            if not page_token:
                break

        except Exception as e:
            logger.error(f"Erreur lors de la récupération des emails: {str(e)}")
            break

    return all_messages

def ensure_label_exists(service, label_name=PROCESSING_CONFIG['target_label']):
    try:
        labels = service.users().labels().list(userId='me').execute().get('labels', [])
        for label in labels:
            if label['name'].lower() == label_name.lower():
                return label['id']

        new_label = {
            'name': label_name,
            'messageListVisibility': 'show',
            'labelListVisibility': 'labelShow'
        }
        label = service.users().labels().create(userId='me', body=new_label).execute()
        logger.info(f"Label '{label_name}' créé avec l'ID {label['id']}")
        return label['id']
    except Exception as e:
        logger.error(f"Erreur lors de la gestion des labels: {str(e)}")
        raise

def process_emails(service):
    try:
        messages = fetch_all_emails(service, EMAIL_QUERY)
        logger.info(f"{len(messages)} emails de candidature trouvés.")

        if not messages:
            return

        label_id = ensure_label_exists(service)

        batch_size = PROCESSING_CONFIG['batch_size']
        for i in range(0, len(messages), batch_size):
            batch = messages[i:i + batch_size]

            for msg in batch:
                try:
                    service.users().messages().modify(
                        userId='me',
                        id=msg['id'],
                        body={
                            'addLabelIds': [label_id],
                            'removeLabelIds': ['INBOX']
                        }
                    ).execute()
                    logger.debug(f"Email {msg['id']} classé dans '{PROCESSING_CONFIG['target_label']}'")
                except Exception as e:
                    logger.warning(f"Erreur lors du traitement de l'email {msg['id']}: {str(e)}")

            logger.info(f"Lot traité: {i+1}-{min(i+batch_size, len(messages))} emails")

    except Exception as e:
        logger.error(f"Erreur dans le traitement principal: {str(e)}")
        raise