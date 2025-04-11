import os

TOKEN_FILE = os.getenv('GMAIL_TOKEN_FILE', '../token.json')
CREDENTIALS_FILE = os.getenv('GMAIL_CREDENTIALS_FILE', '../credentials.json')

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

EMAIL_QUERY = """
(subject:("Suite à votre candidature" OR "Votre candidature" OR "Alternance" OR "Candidature spontanée"
           OR "Réponse candidature" OR "Votre postulation" OR "Votre demande")
 OR body:("Suite à notre rencontre" OR "entretien" OR "poste" OR "recrutement"
          OR "processus de recrutement" OR "votre profil" OR "nous étudions votre candidature"))
-label:Candidatures
"""

PROCESSING_CONFIG = {
    'days_to_search': 90,
    'batch_size': 100,
    'target_label': "Candidatures"
}