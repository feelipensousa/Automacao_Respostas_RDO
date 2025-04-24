from services.google_sheets_API import GS_API

def carregar_planilhas(client, creds, sheet_base_url, sheet_principal_url):
    """
    Função para carregar as planilhsa do google sheets necessárias.
    
    - df_base sendo a planilha que iremos extrair os dados.

    - df_principal sendo a planilha que iremos carregar os dados.
    """

    google_sheets_api = GS_API(client=client, creds=creds)
    google_sheets_api.upload_base_sheet(sheet_url=sheet_base_url, worksheet_name="Respostas ao formulário 1") # Nome da planilha base
    df_base = google_sheets_api.upload_base_sheet_to_df()

    google_sheets_api.upload_principal_sheet(sheet_url=sheet_principal_url, worksheet_name="PRESIDIOS") # Nome da planilha principal
    df_principal = google_sheets_api.upload_principal_sheet_to_df(columns_quantity=6)

    return df_base, df_principal, google_sheets_api
