import mysql.connector
import time
import pandas as pd


def connect_sql(user: str, password: str, host: str, database: str):
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
        return cursor
