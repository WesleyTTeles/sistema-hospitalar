from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error

from conexao_db import conexao_mysql
load_dotenv()

def alterar_hospital():
    print('Favor Informe qual dado do Hospital deseja Atualizar:\n')

    dado_hospital = input('Cnpj | Nome | Rua | Bairro | Cidade | Cep | Telefone: \n').lower()
    if dado_hospital not in ['cnpj', 'nome', 'rua', 'bairro', 'cidade', 'cep', 'telefone']:
        print('Dado informado nao Localizado')
        alterar_hospital()
    else:
        dado_hospital_atualizado = input('Para qual nome deseja atualizar? ')
        query = f'''
            UPDATE Hospital SET {dado_hospital} = '{dado_hospital_atualizado}'
        '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Dados Atualizados com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")
    
def alterar_medico():
    print('Favor Informe qual dado do Médico deseja Atualizar:\n')

    dado_medico = input('Crm | Cpf | Nome | Rua | Bairro | Cidade | Cep | Cnpj_hospital: \n').lower()
    if dado_medico not in ['crm', 'cpf', 'nome', 'rua', 'bairro', 'cidade', 'cep', 'cnpj_hospital']:
        print('Dado informado nao Localizado')
        alterar_medico()
    else:
        dado_medico_atualizado = input('Para qual nome deseja atualizar? ')
        query = f'''
            UPDATE Medico SET {dado_medico} = '{dado_medico_atualizado}'
        '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Dados Atualizados com Sucesso!')
    
    except Error as err:
        print(f"Error: '{err}'")

def alterar_enfermeiro():
    print('Favor Informe qual dado do Enfermeiro(a) deseja Atualizar:\n')

    dado_enfermeiro = input('Corem | Cpf | Nome | Rua | Bairro | Cidade | Cep Cnpj_hospital | Crm_medico: \n').lower()
    if dado_enfermeiro not in ['corem','cpf','nome','rua','bairro','cidade','cep', 'cnpj_hospital', 'crm_medico']:
        print('Dado informado nao Localizado')
        alterar_enfermeiro()
    else:
        dado_enfermeiro_atualizado = input('Para qual nome deseja atualizar? ')
        query = f'''
            UPDATE Enfermeiro SET {dado_enfermeiro} = '{dado_enfermeiro_atualizado}'
        '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Dados Atualizados com Sucesso!')
    
    except Error as err:
        print(f"Error: '{err}'")

def alterar_paciente():
    print('Favor Informe qual dado do Paciente deseja Atualizar:\n')

    dado_paciente = input('Cpf | Rg | Nome | Rua | Bairro | Cidade | Cep | Crm_medico: \n').lower()
    if dado_paciente not in ['cpf','rg','nome','rua','bairro','cidade','cep', 'crm_medico']:
        print('Dado informado nao Localizado')
        alterar_enfermeiro()
    else:
        dado_paciente_atualizado = input('Para qual nome deseja atualizar? ')
        query = f'''
            UPDATE Enfermeiro SET {dado_paciente} = '{dado_paciente_atualizado}'
        '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Dados Atualizados com Sucesso!')
    
    except Error as err:
        print(f"Error: '{err}'")

def alterar_dados():

    opcao_cadastro = int(input("""
Escolha Qual Opção Deseja Alterar: 

1 - Hospital
2 - Médico 
3 - Enfermeiro
4 - Paciente
5 - Fechar Programa
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
        print('Obrigado por usar StarMed! Fechando o programa... ..')
        quit() 
    else:
        print('!!!!!!!!Opção Invalida!!!!!!!!')
        alterar_dados()
