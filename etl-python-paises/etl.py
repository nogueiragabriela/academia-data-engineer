import pandas as pd
import pyodbc
import os

#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

def etl (nome_dataframe):
    # Lendo o arquivo CSV usando o método read_csv
    df = pd.DataFrame(nome_dataframe)
    # Criando uma conexão com o SQL Server
    conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:" +  os.environ["server-name"] + ",1433;Database=" + os.environ["database-name"] + ";Uid=" + os.environ["username"] + ";Pwd=" + os.environ["password"] + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

    cursor = conn.cursor()

    cursor.execute('''  
                        IF OBJECT_ID(N'populacao_mediasalarial', N'U') IS NULL
                        CREATE TABLE populacao_mediasalarial (
                            id int IDENTITY (1,1) NOT NULL,
                            estado varchar(50) NOT NULL,
                            pais varchar(50) NOT NULL,
                            populacao varchar(50) NOT NULL,
                            mediasalarial varchar(50) NOT NULL,
                            PRIMARY KEY(id)
                            )
                ''')

    # Loop através de cada linha no DataFrame
    for index, row in df.iterrows():
        # Inserindo uma linha na tabela
        conn.execute("INSERT INTO populacao_mediasalarial (estado, pais, populacao, mediasalarial) VALUES (?, ?, ?, ?)", row[0], row[1], row[2], row[3])
    # Salvando as mudanças
    conn.commit()
    # Fechando a conexão
    conn.close()