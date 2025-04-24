from dotenv import load_dotenv
import os
from app.authentication import google_sheets_auth
from app.processing.sheet_loader import carregar_planilhas
from app.validating.verifying_rdo import checar_novo_rdo
from app.processing.processing_rdo import processar_novo_rdo
from services.uploadGS import upload_to_google_sheets

load_dotenv()

client, creds = google_sheets_auth()

sheet_base_url = os.getenv('sheet_base_url_SAP')
sheet_principal_url = os.getenv('sheet_principal_url_SAP')
df_base, df_principal, google_sheets_api = carregar_planilhas(client, creds, sheet_base_url, sheet_principal_url)

new_rdo_date = checar_novo_rdo(df_base, df_principal)

raw_RDO_materiais = os.getenv('RDO_materiais_SAP')
args_extra = {
    "new_rdo_date": new_rdo_date,
    "df_base": df_base,
    "linhas_materiais": [57, 59, 61, 63, 65, 67, 69, 71, 73, 75],
    "linhas_quantidades": [58, 60, 62, 64, 66, 68, 70, 72, 74, 76],
    "coluna_data": "CDO referente ao dia:",
    "linha_local": 55,
    "linha_extra": 77
}

novo_df = processar_novo_rdo(raw_RDO_materiais, args_extra)

if novo_df is not None:
    sheet_principal = google_sheets_api.upload_principal_sheet(sheet_url=sheet_principal_url, worksheet_name="PRESIDIOS")
    upload_to_google_sheets(novo_df=novo_df, sheet_principal=sheet_principal)
