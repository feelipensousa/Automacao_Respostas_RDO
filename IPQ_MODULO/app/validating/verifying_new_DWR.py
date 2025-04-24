import pandas as pd
def verificar_rdo_novo(df_principal: pd.DataFrame, df_base: pd.DataFrame, new_rdo_date: list, column_date: int):
    """
    Irá diminuir a data do df_principal da data do df_base , irá verificar se há datas faltantes no df_principal.
    Se houver, um novo rdo foi preenchido.
    """
    principal_date = set(df_principal['DATA']) # Coluna data da planilha em que iremos carregar os dados
    base_date = set(df_base.iloc[:, column_date]) 
    
    novas_datas = base_date - principal_date
    
    new_rdo_date.extend(novas_datas)