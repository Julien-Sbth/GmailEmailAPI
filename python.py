from auth import get_gmail_service
from emails.email_processor import process_emails
from utils.logger import logger

if __name__ == '__main__':
    try:
        logger.info("Démarrage du script...")
        service = get_gmail_service()
        process_emails(service)
        logger.info("Script exécuté avec succès!")
    except Exception as e:
        logger.critical(f"Échec critique: {str(e)}")