import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from typing import Union, List

class GS_API:
    def __init__(self, client: str, creds: str):
        self.client = client
        self.creds = creds
        
    def upload_base_sheet(self, sheet_url: str, worksheet_name: str):
        """
        Carregamos a planilha base
        """
        try:
            self.sheet_base = self.client.open_by_key(sheet_url).worksheet(worksheet_name)
            return self.sheet_base
        except Exception as e:
            print("Planilha base não encontrada: ", e)
        
    def upload_base_sheet_to_df(self):
        """
        Carregamos a planilha base em data frame
        """
        try:
            base_data = self.sheet_base.get_all_values()
            
            # Convertemos os dados para um DataFrame, ignorando a primeira linha como cabeçalho
            self.df_base = pd.DataFrame(base_data[1:], columns=base_data[0])
            
            return self.df_base
        except Exception as e:
            print("Cabeçalhos base não encontrados: ", e)

    def upload_principal_sheet(self, sheet_url: str, worksheet_name: str):
        """
        Carregamos a planilha principal
        """
        try:
            self.sheet_principal = self.client.open_by_key(sheet_url).worksheet(worksheet_name)
            return self.sheet_principal
        except Exception as e:
            print("Planilha principal não encontrada: ", e)

    def upload_principal_sheet_to_df(self, columns_quantity: Union[int, List[int]]):
        """
        Carregamos a planilha principal em data frame
        """
        try:
            if not self.sheet_principal:
                raise ValueError("Objeto sheet_principal não inicializado.")
            
            principal_data = self.sheet_principal.get_all_values()
            
            current_headers = [header.strip() for header in principal_data[0]] 
            
            if isinstance (columns_quantity, int):
                filtered_data = [row[:columns_quantity] for row in principal_data[1:]]  # itera sobre os dados da planilha limitando a quantidade de colunas.
                df_principal_headers = current_headers[:columns_quantity]
            elif isinstance (columns_quantity, List): # Caso eu queira selecinar colunas específicar a serem preenchidas da minha planilha principal (que eu quero que os dados estejam)
                filtered_data = [[row[i] for i in columns_quantity] for row in principal_data[1:]]
                df_principal_headers = [current_headers[i] for i in columns_quantity]
            else:
                raise TypeError ("Você digitou o tipo errado para a quantidade de colunas.")
            self.df_principal = pd.DataFrame(filtered_data, columns=df_principal_headers)
            return self.df_principal
        except Exception as e:
            print("Erro ao carregar os cabeçalhos:", e)
            return None

