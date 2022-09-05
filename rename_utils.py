import pandas as pd
import glob


class RENAME2022:

    def __init__(self, csv_folder):
        self.csv_folder = csv_folder
        self.csv_file = None
        self.list_dataframes = None

    def fill_name_medicine(self, csv_file):
        self.csv_file = csv_file
        name_csv_file = self.csv_file[0:-4]
        pd_treated = pd.read_csv('./planilhas_apendice_resultado/' + csv_file)
        new_pd = pd_treated['Denominação genérica'].fillna(method='ffill')
        new_pd.to_csv(f'{name_csv_file}_atualizado.csv')

    @staticmethod
    def concatenate_tables(list_dataframes):
        final_result = pd.concat(list_dataframes)
        final_result.to_csv('./planilhas_apendice_resultado/resultado.csv')

    def generate_final_file(self):
        list_files = list()
        list_dataframes = list()
        for filename in glob.glob(self.csv_folder + '/*.csv'):
            name_file = filename[-16:]
            list_files.append(name_file)
        list_files.remove('apendice_a_j.csv')
        for sheets in list_files:
            main_df = pd.read_csv('./planilhas_apendice/apendice_a_j.csv')
            # Inserindo a coluna Classificação AWaRe em todos os dataframes
            main_columns = main_df.columns
            df_sheets = pd.read_csv(f'./planilhas_apendice/{sheets}')
            name_new_column = main_columns[-1]
            df_sheets.insert(5, name_new_column, ' ')
            df_sheets.columns = main_columns
            list_dataframes.append(df_sheets)
        list_dataframes.insert(6, pd.read_csv('./planilhas_apendice/apendice_a_j.csv'))
        self.concatenate_tables(list_dataframes)

    @staticmethod
    def length_column():
        """
        Função para descobrir quantos caracteres possui a maior
        ‘string’ da coluna de Concentração/Composição. Será importante
        para a criação do arquivo SQL.
        """
        df = pd.read_csv('planilhas_apendice_resultado/resultado.csv')
        list_columns_name = []
        for i in range(1, 7):
            column_name = df.columns[i]
            info_columns = {
                column_name: max(df[column_name].str.len())
            }
            list_columns_name.append(info_columns)
        return list_columns_name

    @staticmethod
    def get_name_columns():
        df = pd.read_csv('planilhas_apendice_resultado/resultado.csv')
        return list(df.columns)


if __name__ == '__main__':
    r = RENAME2022('planilhas_apendice')
    r.generate_final_file()
    print(r.length_column())
    # r.fill_name_medicine('resultado.csv')
