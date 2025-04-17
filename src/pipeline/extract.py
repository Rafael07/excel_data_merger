import glob  # para trabalhar com arquivos
import os  # para trabalhar com o sistema operacional
from typing import List

import pandas as pd  # para trabalhar com dataframes

input_path = 'data/input'


def extract_excel(input_path: str) -> List[pd.DataFrame]:
    """
    Função para extrair arquivos excel do diretorio data/input
    e retornar um DataFrame.

    args: input_path (str): caminho da pasta de arquivos
    return: lista de DataFrame
    """
    files = glob.glob(os.path.join(input_path, '*.xlsx'))

    data_frame_list = []

    for file in files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_excel(input_path)
    print(data_frame_list)
