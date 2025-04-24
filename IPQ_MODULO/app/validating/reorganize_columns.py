import pandas as pd

def reorganizar_as_colunas(new_rdo_date: list, df_base: pd.DataFrame, RDO_materiais: dict, linhas_materiais: list, linhas_quantidades: list, coluna_data: str, linha_local: int, linha_extra: int):
    """
    Função que irá transformar as colunas em linhas.
    Precisamos passar as colunas que são as dos materiais, quantidades, local e data.
    Irá retornar um novo DF já com as colunas em formas de linhas e o cabeçalho especificado.
    """
    novo_df = []
#
    for date in new_rdo_date:
        linha_especifica = df_base[df_base[coluna_data] == date]

        materiais = linha_especifica.iloc[:, linhas_materiais].values.flatten().tolist() 
        quantidades = linha_especifica.iloc[:, linhas_quantidades].values.flatten().tolist() 
        local = linha_especifica.iloc[:, linha_local].values[0]
        material_extra = linha_especifica.iloc[:, linha_extra].values[0]

        for material, quantidade in zip(materiais, quantidades):
            if pd.notna(material) and pd.notna(quantidade): 
                valor_unitario = RDO_materiais.get(material, None)
                valor_compra = float(quantidade) * valor_unitario if valor_unitario is not None else None

                nova_linha = { # VALORES QUE SÃO DE ACORDO COM OS QUEREMOS VISUALIZAR NO POWERBI
                    "DATA": date,
                    "LOCAL": local,
                    "MATERIAL": material,
                    "QUANTIDADE": quantidade,
                    "VALOR UNITÁRIO": valor_unitario,
                    "VALOR COMPRA": valor_compra
                }
                novo_df.append(nova_linha)

    # Converte a lista em um DataFrame e substitui valores NaN por valores padrão
    novo_df = pd.DataFrame(novo_df).fillna({"LOCAL": "", "VALOR UNITÁRIO": 0, "VALOR COMPRA": 0})
    
    print("Não há novos RDO's encontrados." if novo_df.empty else "Novos RDO's encontrados.")
    print("Não há materiais extra." if not material_extra else f"Há materiais extra: {material_extra}")

    return novo_df