from mysql.connector import connect
from mysql.connector import Error
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def conexao_mysql(host_name, user_name, user_password, db_name):
    conexao = None
    try:
        conexao = connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
        )
        print('Conexao Realizada com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")
    return conexao

#conexao = conexao_mysql(host_name = getenv("host"), user_name = getenv("db_user"), user_password = getenv("password"), db_name = getenv("db_name"))





