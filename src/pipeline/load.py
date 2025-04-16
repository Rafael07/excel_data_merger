import os
import pandas as pd



def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:

    """
        Função para receber um DataFrame e salvar em um arquivo excel

        args: 
            data_frame (pd.DataFrame): DataFrame a ser salvo
            output_path (str): caminho da pasta de arquivos   
            file_name (str): nome do arquivo de saída

        return: str
    """    

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(os.path.join(output_path, file_name), index=False)
    return 'Arquivo salvo com sucesso!!!'