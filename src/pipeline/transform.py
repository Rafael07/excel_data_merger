import pandas as pd
from typing import List

"""
    Função para transformar uma lista de DataFrames em um DataFrame

    args: data_frame_list (List[pd.DataFrame]): lista de DataFrames
    return: DataFrame
"""

def concat_dataframes(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)