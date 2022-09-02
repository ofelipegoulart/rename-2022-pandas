import pandas as pd
import glob

class RENAME2022:

    def __init__(self,csv_folder):
        self.csv_folder = csv_folder

    def concatenate_tables(self):
        list_dataframes = list()
        for filename in glob.glob(self.csv_folder + '/*.csv'):
            table = pd.read_csv(filename)
            list_dataframes.append(table)
            final_dataframe = pd.concat(list_dataframes)
            final_dataframe.to_csv('lista_rename_2022.csv')


r = RENAME2022('planilhas_apendice')
r.concatenate_tables()