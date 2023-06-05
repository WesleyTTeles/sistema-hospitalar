from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error

from conexao_db import conexao_mysql
load_dotenv()

def consultar_hospital():
    consulta_cnpj = f"SELECT CNPJ FROM HOSPITAL"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cnpj)
        resultados = cursor.fetchall()
        conexao.close()
    
        if resultados:
            print(f'Foram Encontrado {len(resultados)} Hospitais Cadastrado:\n')
            for resultado in resultados:
                cnpj_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", "") 
                print(f'CNPJ - {cnpj_tratado}')
        else:
            print('Nao Foi Localizado nenhum CNPJ Cadastrado.')
    except Error as err:
        print(f'Error: {err}')

def consultar_medico():
    consulta_crm = f"SELECT CRM FROM MEDICO"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_crm)
        resultados = cursor.fetchall()
        conexao.close()

        if resultados:
            print(f'Foram Encontrado {len(resultados)} Médico Cadastrado:\n')
            for resultado in resultados:
                crm_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", "") 
                print(f'CRM - {crm_tratado}')
        else:
            print('Nao Foi Localizado nenhum CRM Cadastrado.')
    except Error as err:
        print(f'Error: {err}')

def consultar_enfermeiro():
    consulta_coren = f"SELECT COREN FROM ENFERMEIRO"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_coren)
        resultados = cursor.fetchall()
        conexao.close()

        if resultados:
            print(f'Foram Encontrado {len(resultados)} Enfermeiro Cadastrado:\n')
            for resultado in resultados:
                coren_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", "") 
                print(f'COREN - {coren_tratado}')
        else:
            print('Nao Foi Localizado nenhum COREN Cadastrado.')
    except Error as err:
        print(f'Error: {err}')

def consultar_paciente():
    consulta_cpf = f"SELECT CPF FROM PACIENTE"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cpf)
        resultados = cursor.fetchall()
        conexao.close()

        if resultados:
            print(f'Foram Encontrado {len(resultados)} Paciente Cadastrado:\n')
            for resultado in resultados:
                cpf_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", "") 
                print(f'CPF - {cpf_tratado}')
        else:
            print('Nao Foi Localizado nenhum CPF Cadastrado.')
    except Error as err:
        print(f'Error: {err}')
