def checar_novo_rdo(df_base, df_principal, coluna_data=1):
    """
    Função para validar um novo RDO preenchido.
    """
    from app.validating.verifying_new_DWR import verificar_rdo_novo
    new_rdo_date = []
    verificar_rdo_novo(df_principal, df_base, new_rdo_date, column_date=coluna_data)
    return new_rdo_date
