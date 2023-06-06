from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error

from src.conexao_db import conexao_mysql
load_dotenv()

def listar_hospital():
    consulta_cnpj = f"SELECT CNPJ, NOME FROM HOSPITAL"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cnpj)
        resultados = cursor.fetchall()
        
        if resultados:
            print(f'Foram Encontrado {len(resultados)} Hospitais Cadastrado:\n')
            for resultado in resultados:
                dado_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", " | NOME:") 
                print(f'CNPJ: {dado_tratado}')
                conexao.close()
        else:
            print('Nao Foi Localizado nenhum HOSPITAL Cadastrado.')
    except Error as err:
        print(f'Error: {err}')

def listar_medicos():
    consulta_crm = f"SELECT CRM, NOME FROM MEDICO"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_crm)
        resultados = cursor.fetchall()
    
        if resultados:
            print(f'Foram Encontrado {len(resultados)} Médico Cadastrado:\n')
            for resultado in resultados:
                dado_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", " | NOME:") 
                print(f'CRM: {dado_tratado}')
                conexao.close()
        else:
            print('Nao Foi Localizado nenhum MEDICO Cadastrado.')
    except Error as err:
        print(f'Error: {err}')

def listar_pacientes():
    consulta_cpf = f"SELECT CPF, NOME FROM PACIENTE"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cpf)
        resultados = cursor.fetchall()
    
        if resultados:
            print(f'Foram Encontrado {len(resultados)} Pacientes Cadastrado:\n')
            for resultado in resultados:
                dado_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", " | NOME:") 
                print(f'CPF: {dado_tratado}')
                conexao.close()
        else:
            print('Nao Foi Localizado nenhum PACIENTE Cadastrado.')
    except Error as err:
        print(f'Error: {err}')

def listar_pacientes_aracaju():
    consulta_cpf = f"SELECT CPF, NOME FROM PACIENTE WHERE CIDADE = 'ARACAJU' AND BAIRRO = 'CENTRO'"
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cpf)
        resultados = cursor.fetchall()
    
        if resultados:
            print(f'Foram Encontrado {len(resultados)} Pacientes que Reside no Centro de Aracaju:\n')
            for resultado in resultados:
                dado_tratado = str(resultado).replace("(", "").replace(")", "").replace("'", "").replace(",", " | NOME:") 
                print(f'CPF: {dado_tratado}')
                conexao.close()
        else:
            print('Nao Foi Localizado nenhum PACIENTE que Reside no Centro de Aracaju.')
    except Error as err:
        print(f'Error: {err}')

def listar_corpo_clinico():
    query_medico = "SELECT CRM, NOME FROM MEDICO"
    query_enfermeiro = "SELECT COREN, NOME FROM ENFERMEIRO"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        
        cursor.execute(query_medico)
        resultados_medico = cursor.fetchall()
        
        cursor.execute(query_enfermeiro)
        resultados_enfermeiro = cursor.fetchall()
        
        if resultados_medico:
            print('\n----------- Médico -----------\n')
            for resultado in resultados_medico:
                crm = resultado[0]
                nome = resultado[1]
                print(f'CRM: {crm} | NOME: {nome}')
            
        else:
            print('Nenhum médico encontrado.')
        
        if resultados_enfermeiro:
            print('\n----------- Enfermeiro -----------\n')
            for resultado in resultados_enfermeiro:
                coren = resultado[0]
                nome = resultado[1]
                print(f'COREN: {coren} | NOME: {nome}')
        
        else:
            print('Nenhum enfermeiro encontrado.')
        
        conexao.close()
        
    except Error as err:
        print(f'Error: {err}')

def listar_medico_telefones():
    query = '''
        SELECT M.CRM, M.NOME, T.TELEFONE
        FROM MEDICO M
        JOIN TELEFONE_MEDICO T ON M.CRM = T.CRM_MEDICO
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()

        cursor.execute(query)
        resultados = cursor.fetchall()

        if resultados:
            for resultado in resultados:
                crm = resultado[0]
                nome = resultado[1]
                telefone = resultado[2]
                print(f'CRM: {crm} | NOME: {nome} | TELEFONE: {telefone}')
        else:
            print('Nenhum resultado encontrado.')

        conexao.close()

    except Error as err:
        print(f'Error: {err}')
