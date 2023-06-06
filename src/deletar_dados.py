from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error

from src.consultar_dados import *
from src.conexao_db import conexao_mysql

load_dotenv()

def deletar_hospital():
    consultar_hospital()

    cnpj_hospital = input('Informe o CNPJ do Hospital que deseja excluir: ')
    query = f'''
            SELECT 
            (SELECT COUNT(*) FROM HOSPITAL_ENFERMEIRO WHERE CNPJ_HOSPITAL = '{cnpj_hospital}') AS total_enfermeiro,
            (SELECT COUNT(*) FROM HOSPITAL_MEDICO WHERE CNPJ_HOSPITAL = '{cnpj_hospital}') AS total_medico
            '''
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        resultado = cursor.fetchone()

        total_enfermeiro = resultado[0]
        total_medico = resultado[1]

        if total_enfermeiro > 0 or total_medico > 0:
            print("Não é possível excluir o Hospital pois Existem registros Médico ou Enfermeiro.")
        
        else:
            delete_query = f"DELETE FROM HOSPITAL WHERE CNPJ = '{cnpj_hospital}'"

            try:
                cursor.execute(delete_query)
                conexao.commit()
                conexao.close()
                print('Hospital excluído com sucesso!')
            except Error as err:
                print(f"Erro ao excluir o Hospital: '{err}'")

    except Error as err:
        print(f"Erro ao verificar registros dependentes: '{err}'")

def deletar_medico():
    consultar_medico()

    crm = input('Informe o CRM do Médico que deseja excluir: ')
    query = f'''
            SELECT 
            (SELECT COUNT(*) FROM HOSPITAL_MEDICO WHERE CRM_MEDICO = '{crm}') AS total_hospital,
            (SELECT COUNT(*) FROM ENFERMEIRO_MEDICO WHERE CRM_MEDICO = '{crm}') AS total_enfermeiro,
            (SELECT COUNT(*) FROM PACIENTE_MEDICO WHERE CRM_MEDICO = '{crm}') AS total_paciente,
            (SELECT COUNT(*) FROM ESPECIALIDADE_MEDICO WHERE CRM_MEDICO = '{crm}') AS total_especialidade,
            (SELECT COUNT(*) FROM TELEFONE_MEDICO WHERE CRM_MEDICO = '{crm}') AS total_telefone
            '''
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        resultado = cursor.fetchone()

        total_hospital = resultado[0]
        total_enfermeiro = resultado[1]
        total_paciente = resultado[2]
        total_especialidade = resultado[3]
        total_telefone = resultado[4]

        if total_hospital > 0 or total_enfermeiro > 0 or total_paciente > 0 or total_especialidade > 0 or total_telefone > 0:
            print("Não é possível excluir o Médico pois Existem registros Hospital, Paciente, Enfermeiro, Especialidade ou Telefone.")
        
        else:
            delete_query = f"DELETE FROM MEDICO WHERE CRM = '{crm}'"
            try:
                cursor.execute(delete_query)
                conexao.commit()
                conexao.close()
                print('Médico excluído com sucesso!')
            except Error as err:
                print(f"Erro ao excluir o Médico: '{err}'")

    except Error as err:
        print(f"Erro ao verificar registros dependentes: '{err}'")

def deletar_enfermeiro():
    consultar_enfermeiro()

    coren = input('Informe o COREN do Enfermeiro(a) que deseja excluir: ')
    query = f'''
            SELECT 
            (SELECT COUNT(*) FROM HOSPITAL_ENFERMEIRO WHERE COREN_ENFERMEIRO = '{coren}') AS total_hospital,
            (SELECT COUNT(*) FROM MEDICO_ENFERMEIRO WHERE COREN_ENFERMEIRO = '{coren}') AS total_medico
            '''
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        resultado = cursor.fetchone()

        total_hospital = resultado[0]
        total_medico = resultado[1]

        if total_hospital > 0 or total_medico > 0:
            print("Não é possível excluir o Enfermeiro(a) pois Existem registros de Hospital ou Médico.")
       
        else:
            delete_query = f"DELETE FROM ENFERMEIRO WHERE COREN = '{coren}'"
            try:
                cursor.execute(delete_query)
                conexao.commit()
                conexao.close()
                print('Enfermeiro(a) excluído com sucesso!')
            except Error as err:
                print(f"Erro ao excluir o Enfermeiro: '{err}'")

    except Error as err:
        print(f"Erro ao verificar registros dependentes: '{err}'")

def deletar_paciente():
    consultar_paciente()

    cpf = input('Informe o CPF do Paciente que deseja excluir: ')
    query = f'''
            SELECT 
            (SELECT COUNT(*) FROM PACIENTE_MEDICO WHERE CPF_PACIENTE = '{cpf}') AS total_medico
            '''
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        resultado = cursor.fetchone()

        total_medico = resultado[0]

        if total_medico > 0 :
            print("Não é possível excluir o Paciente pois Existem registros de Médico.")
       
        else:
            delete_query = f"DELETE FROM PACIENTE WHERE CPF = '{cpf}'"
            try:
                cursor.execute(delete_query)
                conexao.commit()
                conexao.close()
                print('Paciente excluído com sucesso!')
            except Error as err:
                print(f"Erro ao excluir o Paciente: '{err}'")

    except Error as err:
        print(f"Erro ao verificar registros dependentes: '{err}'")

def deletar_telefone():
    consultar_medico()
    crm = input('Informe o CRM do médico: ')
    consultar_telefone = f"SELECT ID_TELEFONE, TELEFONE FROM TELEFONE_MEDICO WHERE CRM_MEDICO = '{crm}'"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consultar_telefone)
        resultados = cursor.fetchall()

        if resultados:
            print(f'Foram Encontrado {len(resultados)} Telefones Vinculado a esse Médico:\n')
            for resultado in resultados:
                id_telefone, telefone = resultado
                print(f'ID: {id_telefone}, Telefone: {telefone}')
        else:
            print('Medico não Localizado ou Nao existe Telefone Cadastrado vinculado.')
    except Error as err:
        print(f'Error: {err}')
    
    id_telefone = input('\nInforme qual ID do Telefone você deseja Apagar: ')
    deletar_id = f"DELETE FROM TELEFONE_MEDICO WHERE ID_TELEFONE = '{id_telefone}'"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(deletar_id)
        conexao.commit()
        conexao.close()
        
        print('Telefone Apagado Com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def deletar_especialidade():
    consultar_medico()
    crm = input('Informe o CRM do médico: ')
    consultar_especialidade = f"SELECT ID_ESPECIALIDADE, ESPECIALIDADE FROM ESPECIALIDADE_MEDICO WHERE CRM_MEDICO = '{crm}'"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consultar_especialidade)
        resultados = cursor.fetchall()

        if resultados:
            print(f'Foram Encontrado {len(resultados)} Especialidade Vinculado a esse Médico:\n')
            for resultado in resultados:
                id_especialidade, especialidade = resultado
                print(f'ID: {id_especialidade}, Especialidade: {especialidade}')
        else:
            print('Medico não Localizado ou Nao existe Especialidade Cadastrado vinculado.')
    except Error as err:
        print(f'Error: {err}')
    
    id_especialidade = input('\nInforme qual ID da Especialidade você deseja Apagar: ')
    deletar_id = f"DELETE FROM ESPECIALIDADE_MEDICO WHERE ID_ESPECIALIDADE = '{id_especialidade}'"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(deletar_id)
        conexao.commit()
        conexao.close()
        
        print('Especialidade Apagado Com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def deletar_dados():
    opcao = int(input("""
Escolha Qual Opção Deseja Deletar: 

1 - Hospital
2 - Médico 
3 - Enfermeiro
4 - Paciente
5 - Especialidade do Médico
6 - Telefone do Médico
7 - Fechar Programa
""")) 

    if opcao == 1:
        deletar_hospital()
    elif opcao == 2:
        deletar_medico()
    elif opcao == 3:
        deletar_enfermeiro()
    elif opcao == 4:
        deletar_paciente()
    elif opcao == 5:
        deletar_especialidade()         
    elif opcao == 6:
        deletar_telefone()
    elif opcao == 7:
        print('Obrigado por usar StarMed! Fechando o programa... ..')
        quit() 
    else:
        print('!!!!!!!!Opção Invalida!!!!!!!!')
        deletar_dados()
