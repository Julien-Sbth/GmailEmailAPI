from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
import google.auth.transport.requests
from utils.config import TOKEN_FILE, CREDENTIALS_FILE, SCOPES
import os

def get_gmail_service():
    credentials = None

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token_file:
            credentials_info = json.load(token_file)
            credentials = Credentials(**credentials_info)

        if not credentials.valid:
            credentials.refresh(google.auth.transport.requests.Request())
            save_credentials(credentials)

        return build('gmail', 'v1', credentials=credentials)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        credentials = flow.run_local_server(port=0)
        save_credentials(credentials)
        return build('gmail', 'v1', credentials=credentials)


def save_credentials(credentials):
    with open(TOKEN_FILE, 'w') as token_file:
        json.dump(credentials_to_dict(credentials), token_file)


def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }