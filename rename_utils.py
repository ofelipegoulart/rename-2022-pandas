import pandas as pd
import glob


class RENAME2022:

    def __init__(self, csv_folder):
        self.csv_folder = csv_folder
        self.csv_file = None

    def concatenate_tables(self):
        list_dataframes = list()
        for filename in glob.glob(self.csv_folder + '/*.csv'):
            table = pd.read_csv(filename)
            list_dataframes.append(table)
            final_dataframe = pd.concat(list_dataframes)
            final_dataframe.to_csv('lista_rename_2022.csv')

    def fill_name_medicine(self, csv_file):
        self.csv_file = csv_file
        name_csv_file = self.csv_file[0:-4]
        pd_treated = pd.read_csv(csv_file)
        new_pd = pd_treated.fillna(method='ffill')
        new_pd.to_csv(f'{name_csv_file}_atualizado.csv')

    def generate_final_file(self):
        list_files = list()
        list_dataframes = list()
        for filename in glob.glob(self.csv_folder + '/*.csv'):
            name_file = filename[-16:]
            list_files.append(name_file)
        list_files.remove('apendice_a_j.csv')
        for sheets in list_files:
            main_df = pd.read_csv('./planilhas_apendice/apendice_a_j.csv')
            main_columns = main_df.columns
            df_sheets = pd.read_csv(f'./planilhas_apendice/{sheets}')
            name_new_column = main_columns[-1]
            df_sheets.insert(5, name_new_column, '')
            df_sheets.columns = main_columns
            list_dataframes.append(df_sheets)
        list_dataframes.insert(6,pd.read_csv('./planilhas_apendice/apendice_a_j.csv'))
        final_result = pd.concat(list_dataframes)
        final_result.to_csv('./planilhas_apendice_resultado/resultado.csv')


if __name__ == '__main__':
    r = RENAME2022('planilhas_apendice')
    r.generate_final_file()
