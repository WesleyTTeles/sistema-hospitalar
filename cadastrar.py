from conexao_db import conexao_mysql
from os import getenv
from dotenv import load_dotenv
load_dotenv()


def cadastrar_hospital():
    print('Favor Informe os dados para o Cadastro do Hospital:\n')

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

    conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()

def cadastrar_medico():
    print('Favor Informe os dados para o Cadastro do Médico:\n')

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

    conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()

def cadastrar_dados():

    opcao_cadastro = int(input("""
Escolha Qual Opção Deseja Cadastrar: 

1 - Hospital
2 - Médico 
3 - Paciente
4 - Enfermeiro
""")) 

    if opcao_cadastro == 1:
        cadastrar_hospital()
    elif opcao_cadastro == 2:
        cadastrar_medico()
