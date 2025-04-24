import pandas as pd
# Atualizar com o pydantic para validar entrada.
def upload_to_google_sheets(novo_df: pd.DataFrame, sheet_principal: pd.DataFrame):
    """
    Carrega o data frame para o .xlsx no google sheets
    """
    novos_rdos_para_planilha_principal = novo_df.values.tolist()
    sheet_principal.append_rows(novos_rdos_para_planilha_principal, value_input_option="USER_ENTERED")
    print("Novas linhas adicionadas com sucesso!")