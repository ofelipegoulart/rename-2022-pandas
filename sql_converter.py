import mysql.connector
import time
from mysql.connector import errorcode
import pandas as pd


def creating_sql_file(user: str, password: str, host: str, database: str):
    csv_file = pd.read_csv('./planilhas_apendice_resultado/resultado.csv')
    conn = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database)

    if conn.is_connected():
        db_info = conn.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = conn.cursor()
        cursor.execute('SELECT database();')
        linha = cursor.fetchone()
        time.sleep(2)
        print("Conectado ao banco de dados", linha)
        time.sleep(2)
        print("Criando a tabela...")
        tables = {'resources': (
            "CREATE TABLE teste_final_foi_agora "
            "(id int,"
            "Denominação_Genérica varchar(115) NOT NULL,"
            "Concentração_Composição varchar(346),"
            "Forma_Farmacêutica varchar(54),"
            "Código_ATC varchar(17),"
            "Componente varchar(35),"
            "Classificação_AWaRe varchar(10),"
            "PRIMARY KEY (id));")}
        for table_name in tables:
            table_description = tables[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        time.sleep(2)
        print("Adicionando os dados...")
        for row in csv_file.itertuples():
            val = (row[0], row[2], row[3], row[4], row[5], row[6], row[7])
            cursor.execute('''
                        INSERT INTO teste_final_foi_agora (id, Denominação_Genérica, Concentração_Composição,
                        Forma_Farmacêutica, Código_ATC, Componente, Classificação_AWaRe)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ''', val
                           )
        conn.commit()
        print("Concluído!")

        # Tem que substituir NaN por ' ', aproveita e já muda a coluna do ffill
