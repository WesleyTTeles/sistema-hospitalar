from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error

from conexao_db import conexao_mysql
load_dotenv()

def alterar_hospital():  
    
    cpnj_hospital = input('Informe o CNPJ do Hospital para ser Alterado: ')
    consulta_cnpj = f"SELECT CNPJ FROM HOSPITAL WHERE CNPJ = '{cpnj_hospital}'"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cnpj)
        resultado = cursor.fetchone()

        if resultado:
            print('Favor Informe qual dado do Hospital deseja Atualizar:\n')

            dado_hospital = input('Cnpj | Nome | Rua | Bairro | Cidade | Cep | Telefone: \n').upper()
            if dado_hospital not in ['CNPJ', 'NOME', 'RUA', 'BAIRRO', 'CIDADE', 'CEP', 'TELEFONE']:
                print('Dado informado nao Localizado')
                alterar_hospital()
            else:
                dado_hospital_atualizado = input('Para qual nome deseja atualizar? ')
                query = f'''
                    UPDATE HOSPITAL SET {dado_hospital} = '{dado_hospital_atualizado}'
                    WHERE CNPJ = '{cpnj_hospital}'
                '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Dados Atualizados com Sucesso!')
            except Error as err:
                print(f"Error: '{err}'")

        else:
            print("CNPJ não encontrado na base de dados, Tente Novamente")
            alterar_dados()

    except Error as err:
        print(f"Error: '{err}'")

def alterar_medico():

    crm_medico = input('Informe o CRM do Médico para ser Alterado: ')
    consulta_crm = f"SELECT CRM FROM MEDICO WHERE CRM = '{crm_medico}'"

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_crm)
        resultado = cursor.fetchone()
        
        if resultado:
            print('Favor Informe qual dado do Médico deseja Atualizar:\n')

            dado_medico = input('Crm | Cpf | Nome | Rua | Bairro | Cidade | Cep: \n').upper()
            if dado_medico not in ['CRM', 'CPF', 'NOME', 'RUA', 'BAIRRO', 'CIDADE', 'CEP']:
                print('Dado informado nao Localizado')
                alterar_medico()
            else:
                dado_medico_atualizado = input('Para qual nome deseja atualizar? ')
                query = f'''
                    UPDATE MEDICO SET {dado_medico} = '{dado_medico_atualizado}'
                    WHERE CRM = '{crm_medico}'
                '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Dados Atualizados com Sucesso!')
            
            except Error as err:
                print(f"Error: '{err}'")
        else:
            print("CRM não encontrado na base de dados, Tente Novamente")
            alterar_dados()

    except Error as err:
        print(f"Error: '{err}'")

def alterar_enfermeiro():

    coren_enfermeiro = input('Informe o COREM do Enfermeiro(a) para ser Alterado: ')
    consultar_coren = f"SELECT COREN FROM ENFERMEIRO WHERE COREN = '{coren_enfermeiro}'"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consultar_coren)
        resultado = cursor.fetchone()

        if resultado:
            print('Favor Informe qual dado do Enfermeiro(a) deseja Atualizar:\n')

            dado_enfermeiro = input('Corem | Cpf | Nome | Rua | Bairro | Cidade | Cep:  \n').upper()
            if dado_enfermeiro not in ['COREN','CPF','NOME','RUA','BAIRRO','CIDADE','CEP']:
                print('Dado informado nao Localizado')
                alterar_enfermeiro()
            else:
                dado_enfermeiro_atualizado = input('Para qual nome deseja atualizar? ')
                query = f'''
                    UPDATE ENFERMEIRO SET {dado_enfermeiro} = '{dado_enfermeiro_atualizado}'
                    WHERE COREN = '{coren_enfermeiro}'
                '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Dados Atualizados com Sucesso!')
            
            except Error as err:
                print(f"Error: '{err}'")
        else:
            print("COREM não encontrado na base de dados, Tente Novamente.")
            alterar_dados()

    except Error as err:
        print(f"Error: '{err}'")

def alterar_paciente():

    cpf_do_paciente = input('Informe o CPF do Paciente para ser Alterado: ')
    consulta_cpf = f"SELECT CPF FROM PACIENTE WHERE CPF = '{cpf_do_paciente}'"

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cpf)
        resultado = cursor.fetchone()

        if resultado:
            print('Favor Informe qual dado do Paciente deseja Atualizar:\n')

            dado_paciente = input('Cpf | Rg | Nome | Rua | Bairro | Cidade | Cep: \n').upper()
            if dado_paciente not in ['CPF','RG','NOME','RUA','BAIRRO','CIDADE','CEP']:
                print('Dado informado nao Localizado')
                alterar_paciente()
            
            else:
                dado_paciente_atualizado = input('Para qual nome deseja atualizar? ')
                query = f'''
                    UPDATE PACIENTE SET {dado_paciente} = '{dado_paciente_atualizado}'
                    WHERE CPF = '{cpf_do_paciente}'
                '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Dados Atualizados com Sucesso!')
            
            except Error as err:
                print(f"Error: '{err}'")
        else:
            print("CPF não encontrado na base de dados, Tente Novamente.")
            alterar_dados()

    except Error as err:
        print(f"Erro: {err}")

def alterar_especialidade():

    crm_medico = input('Informe o CRM do Médico para ser Alterado: ')
    consulta_crm = f"SELECT CRM FROM MEDICO WHERE CRM = '{crm_medico}'"

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_crm)
        resultado = cursor.fetchone()
        if resultado:
            
            nova_especialidade = input('Informe a Especialidade: ')
            query = f'''
                UPDATE ESPECIALIDADE_MEDICO SET ESPECIALIDADE = '{nova_especialidade}'
                WHERE CRM_MEDICO = '{crm_medico}'
            '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Dados Atualizados com Sucesso!')
            
            except Error as err:
                print(f"Error: '{err}'")
        else:
            print("CRM não encontrado na base de dados, Tente Novamente")
            alterar_dados()

    except Error as err:
        print(f"Error: '{err}'")

def alterar_telefone():
    pass

def alterar_dados():

    opcao_cadastro = int(input("""
Escolha Qual Opção Deseja Alterar: 

1 - Hospital
2 - Médico 
3 - Enfermeiro
4 - Paciente
5 - Especialidade
6 - Telefone do Médico
7 - Fechar Programa
""")) 

    if opcao_cadastro == 1:
        alterar_hospital()
    elif opcao_cadastro == 2:
        alterar_medico()
    elif opcao_cadastro == 3:
        alterar_enfermeiro()
    elif opcao_cadastro == 4:
        alterar_paciente()      
    elif opcao_cadastro == 5:
        alterar_especialidade()      
    elif opcao_cadastro == 6:
        alterar_telefone()      
    elif opcao_cadastro == 7:
        print('Obrigado por usar StarMed! Fechando o programa... ..')
        quit() 
    else:
        print('!!!!!!!!Opção Invalida!!!!!!!!')
        alterar_dados()
