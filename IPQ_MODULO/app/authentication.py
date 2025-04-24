from google.oauth2.service_account import Credentials
import gspread
import os

def google_sheets_auth():
    """
    Função para autenticar as credenciais para acessar a api do google sheets.
    """
    credentials_path = os.getenv("credentials")
    creds = Credentials.from_service_account_file(credentials_path, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(creds)
    return client, creds
