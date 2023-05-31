from conexao_db import conexao_mysql
from os import getenv
from dotenv import load_dotenv
load_dotenv()

query_medico = '''
    CREATE TABLE Medico (
        crm             VARCHAR(11) PRIMARY KEY, 
        cpf             VARCHAR(11),
        nome            VARCHAR(20),
        rua             VARCHAR(50),
        bairro          VARCHAR(20),
        cidade          VARCHAR(20),
        cep             VARCHAR(8),
        cnpj_hospital   VARCHAR(14),
        FOREIGN KEY (cnpj_hospital) REFERENCES Hospital(cnpj)    
    )
'''

conexao = conexao_mysql(host_name = getenv("host"), user_name = getenv("db_user"), user_password = getenv("password"), db_name = getenv("db_name"))
cursor = conexao.cursor()
cursor.execute(query_medico)