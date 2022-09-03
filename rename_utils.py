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
        pd_treated = pd.read_csv('./planilhas_apendice/' + csv_file)
        new_pd = pd_treated.fillna(method='ffill')
        '''
        Importante: o método ffill preenche as células vazias com o valor anterior em todas as colunas 
        do dataframe. Tome cuidado para não preencher valores vazios em células que no RENAME não possuem
        valor no documento original.
        Se utilizar, modifique para a coluna do seu interesso, de modo a reduzir retrabalhos.
        '''
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
        list_dataframes.insert(6, pd.read_csv('./planilhas_apendice/apendice_a_j.csv'))
        final_result = pd.concat(list_dataframes)
        final_result.to_csv('./planilhas_apendice_resultado/resultado.csv')

    @staticmethod
    def length_column():
        """
        Função para descobrir quantos caracteres possui a maior
        ‘string’ da coluna de Concentração/Composição. Será importante
        para a criação do arquivo SQL.
        """
        df = pd.read_csv('planilhas_apendice_resultado/resultado.csv')
        column = df['Concentração/\nComposição']
        return max(column.str.len())

    @staticmethod
    def get_name_columns():
        df = pd.read_csv('planilhas_apendice_resultado/resultado.csv')
        return list(df.columns)


if __name__ == '__main__':
    r = RENAME2022('planilhas_apendice')
    print(r.get_name_columns())
