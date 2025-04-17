import pandas as pd

from src.pipeline.transform import concat_dataframes

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4], 'col3': [5, 6]})
df_2 = pd.DataFrame({'col1': [7, 8], 'col2': [9, 10], 'col3': [11, 12]})
df_3 = pd.DataFrame({'col1': [13, 14], 'col2': [15, 16], 'col3': [17, 18]})


def testar_concat_dataframes():
    """
    Usar o padrão Triple A para testar a função concat_dataframes.
    """
    # arrange
    dataframes = [df_1, df_2, df_3]
    dataframes2 = pd.concat(dataframes, ignore_index=True)

    # act
    result = concat_dataframes(dataframes)

    # assert
    expected = pd.DataFrame(
        {
            'col1': [1, 2, 7, 8, 13, 14],
            'col2': [3, 4, 9, 10, 15, 16],
            'col3': [5, 6, 11, 12, 17, 18],
        }
    )
    pd.testing.assert_frame_equal(result, expected)
    assert result.equals(dataframes2)
