from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error

from conexao_db import conexao_mysql
load_dotenv()

def cadastrar_hospital():
    print('Favor Informe os dados para Cadastro do Hospital:\n')

    cnpj = input('CNPJ: ')
    nome = input('Nome do Hospital: ')
    rua = input('Nome da Rua: ')
    bairro = input('Nome do Bairro: ')
    cidade = input('Nome da Cidade: ')
    cep = input('Cep: ')
    telefone = input('Telefone: ')

    query = f'''
        INSERT INTO Hospital (cnpj, nome, rua, bairro, cidade, cep, telefone)
        VALUES ('{cnpj}', '{nome}', '{rua}', '{bairro}', '{cidade}', '{cep}', '{telefone}')
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Hospital Cadastrado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_medico():
    print('Favor Informe os dados para Cadastro do Médico:\n')

    crm = input('CRM: ')
    cpf = input('CPF: ')
    nome = input('Nome do Medico: ')
    rua = input('Nome da Rua: ')
    bairro = input('Nome do Bairro: ')
    cidade = input('Nome da Cidade: ')
    cep = input('Cep: ')
    cnpj_hospital = input('Informe o CNPJ do Hospital de Atuacao: ')

    query = f'''
        INSERT INTO Medico (crm, cpf, nome, rua, bairro, cidade, cep, cnpj_hospital)
        VALUES ('{crm}', '{cpf}', '{nome}', '{rua}', '{bairro}', '{cidade}', '{cep}' , '{cnpj_hospital}')
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Medico Cadastrado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_enfermeiro():
    print('Favor inform os dados para Cadastro do Enfermeiro(a)')

    corem = input('CRM: ')
    cpf = input('CPF: ')
    nome = input('Nome do Medico: ')
    rua = input('Nome da Rua: ')
    bairro = input('Nome do Bairro: ')
    cidade = input('Nome da Cidade: ')
    cep = input('Cep: ')
    cnpj_hospital = input('Informe o CNPJ do Hospital de Atuacao: ')
    crm_medico = input('Informe o CRM do Médico Responsavel: ')

    query = f''''
        INSERT INTO Enfermeiro corem, cpf, nome, rua, bairro, cidade, cep, cnpj_hospital
        VALUES ('{corem}','{cpf}','{nome}','{rua}','{bairro}','{cidade}','{cep}', '{cnpj_hospital}', '{crm_medico}')
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Enfermeiro(a) Cadastrado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_paciente():
    print('Favor inform os dados para Cadastro do Paciente')

    cpf = input('CPF: ')
    rg = input('RG: ')
    nome = input('Nome do Medico: ')
    rua = input('Nome da Rua: ')
    bairro = input('Nome do Bairro: ')
    cidade = input('Nome da Cidade: ')
    cep = input('Cep: ')
    crm_medico = input('Informe o CRM do Médico Responsavel Pelo Paciente: ')

    query = f'''
        INSERT INTO Pacientes cpf, rg, nome, rua, bairro, cidade, 
        VALUES ('{cpf}','{rg}','{nome}','{rua}','{bairro}','{cidade}','{cep}', '{crm_medico}')
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Paciente Cadastrado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_dados():

    opcao_cadastro = int(input("""
Escolha Qual Opção Deseja Cadastrar: 

1 - Hospital
2 - Médico 
3 - Enfermeiro
4 - Paciente
5 - Fechar Programa
""")) 

    if opcao_cadastro == 1:
        cadastrar_hospital()
    elif opcao_cadastro == 2:
        cadastrar_medico()
    elif opcao_cadastro == 3:
        cadastrar_enfermeiro()
    elif opcao_cadastro == 4:
        cadastrar_paciente()      
    elif opcao_cadastro == 5:
        print('Obrigado por usar StarMed! Fechando o programa... ..')
        quit() 
    else:
        print('!!!!!!!!Opção Invalida!!!!!!!!')
        cadastrar_dados()