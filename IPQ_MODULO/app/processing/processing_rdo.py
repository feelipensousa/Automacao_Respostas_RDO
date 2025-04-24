import ast
from app.validating.reorganize_columns import reorganizar_as_colunas

def processar_novo_rdo(raw_RDO_materiais, args_extra):
    """
    Função para validar as linhas dos materiais e quantidades.
    """
    try:
        RDO_materiais = ast.literal_eval(raw_RDO_materiais)

        args = {
            "RDO_materiais": RDO_materiais,
            **args_extra
        }

        return reorganizar_as_colunas(**args)

    except (ValueError, SyntaxError) as e:
        print(f"Erro ao converter a string para dicionário: {e}")
        return None
