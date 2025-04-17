from pipeline.extract import extract_excel
from pipeline.load import load_excel
from pipeline.transform import concat_dataframes

if __name__ == '__main__':
    data_frame_list = extract_excel('data/input')
    data_frame = concat_dataframes(data_frame_list)
    load_excel(data_frame, 'data/output', 'output.xlsx')
