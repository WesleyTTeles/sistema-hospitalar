from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error

from conexao_db import conexao_mysql
load_dotenv()

def cadastrar_hospital():
    print('Favor Informe os dados para Cadastro do Hospital:\n')
    
    cpnj = input('CNPJ: ')
    consulta_cnpj = f"SELECT CNPJ FROM HOSPITAL WHERE CNPJ = '{cpnj}'"
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cnpj)
        resultado = cursor.fetchone()
    
        if resultado:
            print("Ja Existe Hospital com esse CNPJ cadastrado na base de dados, Tente Novamente")
            cadastrar_dados()
        else:
            nome = input('Nome do Hospital: ')
            rua = input('Nome da Rua: ')
            bairro = input('Nome do Bairro: ')
            cidade = input('Nome da Cidade: ')
            cep = input('Cep: ')
            telefone = input('Telefone: ')

            query = f'''
                INSERT INTO HOSPITAL (CNPJ, NOME, RUA, BAIRRO, CIDADE, CEP, TELEFONE)
                VALUES ('{cpnj}', '{nome}', '{rua}', '{bairro}', '{cidade}', '{cep}', '{telefone}')
            '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Hospital Cadastrado com Sucesso!')
            except Error as err:
                print(f"Error: '{err}'")

    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_medico():
    print('Favor Informe os dados para Cadastro do Médico:\n')

    crm = input('CRM: ')
    consulta_crm = f"SELECT CRM FROM MEDICO WHERE CRM = '{crm}'"

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_crm)
        resultado = cursor.fetchone()

        if resultado:
            print("Ja Existe Médico com esse CRM cadastrado na base de dados, Tente Novamente")
            cadastrar_dados()
        else:
            cpf = input('CPF: ')
            nome = input('Nome do Medico: ')
            rua = input('Nome da Rua: ')
            bairro = input('Nome do Bairro: ')
            cidade = input('Nome da Cidade: ')
            cep = input('Cep: ')

            query = f'''
                INSERT INTO MEDICO (CRM, CPF, NOME, RUA, BAIRRO, CIDADE, CEP)
                VALUES ('{crm}', '{cpf}', '{nome}', '{rua}', '{bairro}', '{cidade}', '{cep}')
            '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Medico Cadastrado com Sucesso!')
            except Error as err:
                print(f"Error: '{err}'")

    except Error as err:
        print(f"Error: '{err}'")        

def cadastrar_enfermeiro():
    print('Favor inform os dados para Cadastro do Enfermeiro(a)')

    coren = input('COREN: ')
    consulta_coren = f"SELECT COREN FROM ENFERMEIRO WHERE COREN = '{coren}'"

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_coren)
        resultado = cursor.fetchone()

        if resultado:
            print("Ja Existe Enfermeiro(a) com esse COREN cadastrado na base de dados, Tente Novamente")
            cadastrar_dados()
        else:
            cpf = input('CPF: ')
            nome = input('Nome do Enfermeiro(a): ')
            rua = input('Nome da Rua: ')
            bairro = input('Nome do Bairro: ')
            cidade = input('Nome da Cidade: ')
            cep = input('Cep: ')

            query = f'''
                INSERT INTO ENFERMEIRO (COREN, CPF, NOME, RUA, BAIRRO, CIDADE, CEP)
                VALUES ('{coren}', '{cpf}', '{nome}', '{rua}', '{bairro}', '{cidade}', '{cep}')
            '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Enfermeiro(a) Cadastrado com Sucesso!')
            except Error as err:
                print(f"Error: '{err}'")

    except Error as err:
        print(f"Error: '{err}'")      

def cadastrar_paciente():
    print('Favor inform os dados para Cadastro do Paciente')

    cpf = input('CPF: ')
    consulta_cpf = f"SELECT CPF FROM PACIENTE WHERE CPF = '{cpf}'"

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(consulta_cpf)
        resultado = cursor.fetchone()

        if resultado:
            print("Ja Existe Paciente com esse CPF cadastrado na base de dados, Tente Novamente")
            cadastrar_dados()
        else:
            rg = input('RG: ')
            nome = input('Nome do Paciente: ')
            rua = input('Nome da Rua: ')
            bairro = input('Nome do Bairro: ')
            cidade = input('Nome da Cidade: ')
            cep = input('Cep: ')

            query = f'''
                INSERT INTO PACIENTE (CPF, RG, NOME, RUA, BAIRRO, CIDADE, CEP)
                VALUES ('{cpf}','{rg}','{nome}','{rua}','{bairro}','{cidade}','{cep}')
            '''
            try:
                conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
                cursor = conexao.cursor()
                cursor.execute(query)
                conexao.commit()
                print('Paciente Cadastrado com Sucesso!')
            except Error as err:
                print(f"Error: '{err}'")

    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_associar_especialidade():
    
    especialidade = input('Informe a Especialidade do Médico: ')
    crm_do_medico = input('Informe o CRM do Medico para Associação: ')
    
    query = f'''
        INSERT INTO ESPECIALIDADE_MEDICO (ESPECIALIDADE, CRM_MEDICO)
        VALUES ('{especialidade}', '{crm_do_medico}');
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Especialidade Cadastrado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_associar_numero_medico():

    telefone = input('Informe o número de Telefone do Médico: ')
    crm_do_medico = input('Informe o CRM do Medico para Associação: ')
    
    query = f'''
        INSERT INTO TELEFONE_MEDICO (TELEFONE, CRM_MEDICO)
        VALUES ('{telefone}', '{crm_do_medico}');
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Número Cadastrado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def associar_medico_hospital():

    cnpj_do_hospital = input('Informe o numero do CNPJ do Hospital em que o Médico Trabalha: ')
    crm_do_medico = input('Informe o CRM do Medico: ')
    
    query = f'''
        INSERT INTO HOSPITAL_MEDICO (CNPJ_HOSPITAL, CRM_MEDICO)
        VALUES ('{cnpj_do_hospital}', '{crm_do_medico}');
    '''
    
    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Médico Associado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def associar_paciente_medico():

    cpf_paciente = input('Informe o CPF do Paciente: ')
    crm_do_medico = input('Informe o CRM do Medico para Associação: ')
    
    query = f'''
        INSERT INTO PACIENTE_MEDICO (CPF_PACIENTE, CRM_MEDICO)
        VALUES ('{cpf_paciente}', '{crm_do_medico}');
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Paciente Associado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def associar_enfermeiro_hospital():

    cnpj_do_hospital = input('Informe o numero do CNPJ do Hospital em que o Enfermeiro(a) Trabalha: ')
    coren_enfermeiro = input('Informe o COREN do Enfermeiro(a) para Associação: ')
    
    query = f'''
        INSERT INTO HOSPITAL_ENFERMEIRO (CNPJ_HOSPITAL, COREN_ENFERMEIRO)
        VALUES ('{cnpj_do_hospital}', '{coren_enfermeiro}');
    '''

    try:
        conexao = conexao_mysql(host_name=getenv("host"), user_name=getenv("db_user"), user_password=getenv("password"), db_name=getenv("db_name"))
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print('Enfermeiro(a) Associado com Sucesso!')
    except Error as err:
        print(f"Error: '{err}'")

def cadastrar_dados():

    opcao_cadastro = int(input("""
Escolha Qual Opção Deseja Cadastrar: 

1 - Hospital
2 - Médico 
3 - Enfermeiro
4 - Paciente
5 - Especialidade do Médico
6 - Novo Número de Telefone do Médico
7 - Fechar Programa
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
        cadastrar_associar_especialidade()      
    elif opcao_cadastro == 6:
        cadastrar_associar_numero_medico()      
    elif opcao_cadastro == 7:
        print('Obrigado por usar StarMed! Fechando o programa... ..')
        quit() 
    else:
        print('!!!!!!!!Opção Invalida!!!!!!!!')
        cadastrar_dados()
