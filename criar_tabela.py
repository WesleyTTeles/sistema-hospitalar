from os import getenv
from dotenv import load_dotenv
from conexao_db import conexao_mysql
load_dotenv()

query_hospital = '''
    CREATE TABLE HOSPITAL (
    CNPJ     VARCHAR(14) PRIMARY KEY,
    NOME     VARCHAR(100),
    RUA      VARCHAR(50),
    BAIRRO   VARCHAR(20),
    CIDADE   VARCHAR(20),
    CEP      VARCHAR(8),
    TELEFONE VARCHAR(14)
);
'''

query_medico = '''
    CREATE TABLE MEDICO (
    CRM    VARCHAR(11) PRIMARY KEY, 
    CPF    VARCHAR(11),
    NOME   VARCHAR(20),
    RUA    VARCHAR(50),
    BAIRRO VARCHAR(20),
    CIDADE VARCHAR(20),
    CEP    VARCHAR(8)
);  
'''

query_enfermeiro = '''
    CREATE TABLE ENFERMEIRO (
    COREN  VARCHAR(11) PRIMARY KEY, 
    CPF    VARCHAR(11),
    NOME   VARCHAR(20),
    RUA    VARCHAR(50),
    BAIRRO VARCHAR(20),
    CIDADE VARCHAR(20),
    CEP    VARCHAR(8)
);
'''

query_paciente = '''
    CREATE TABLE PACIENTE (
    CPF    VARCHAR(11) PRIMARY KEY, 
    RG     VARCHAR(11),
    NOME   VARCHAR(20),
    RUA    VARCHAR(50),
    BAIRRO VARCHAR(20),
    CIDADE VARCHAR(20),
    CEP    VARCHAR(8)
);  
'''

query_hospital_medico = '''
    CREATE TABLE HOSPITAL_MEDICO (
    CNPJ_HOSPITAL VARCHAR(14),
    CRM_MEDICO    VARCHAR(10),
    PRIMARY KEY (CNPJ_HOSPITAL, CRM_MEDICO),
    FOREIGN KEY (CNPJ_HOSPITAL) REFERENCES HOSPITAL(CNPJ),
    FOREIGN KEY (CRM_MEDICO) REFERENCES MEDICO(CRM)
);
'''

query_paciente_medico = '''
    CREATE TABLE PACIENTE_MEDICO (
    CPF_PACIENTE VARCHAR(11),
    CRM_MEDICO   VARCHAR(11),
    PRIMARY KEY (CPF_PACIENTE, CRM_MEDICO),
    FOREIGN KEY (CPF_PACIENTE) REFERENCES PACIENTE(CPF),
    FOREIGN KEY (CRM_MEDICO) REFERENCES MEDICO(CRM)
);
'''

query_hospital_enfermeiro = '''
    CREATE TABLE HOSPITAL_ENFERMEIRO (
    CNPJ_HOSPITAL    VARCHAR(14),
    COREN_ENFERMEIRO VARCHAR(11),
    PRIMARY KEY (CNPJ_HOSPITAL, COREN_ENFERMEIRO),
    FOREIGN KEY (CNPJ_HOSPITAL) REFERENCES HOSPITAL(CNPJ),
    FOREIGN KEY (COREN_ENFERMEIRO) REFERENCES ENFERMEIRO(COREN)
);
'''

query_especialidade_medico = '''
    CREATE TABLE ESPECIALIDADE (
    ID_ESPECIALIDADE INT AUTO_INCREMENT PRIMARY KEY,
    ESPECIALIDADE VARCHAR(50),
    CRM_MEDICO VARCHAR(11),
    FOREIGN KEY (CRM_MEDICO) REFERENCES MEDICO(CRM)
);
'''

query_telefone_medico = '''
    CREATE TABLE TELEFONE (
    ID_TELEFONE INT AUTO_INCREMENT PRIMARY KEY,
    TELEFONE   VARCHAR(10),
    CRM_MEDICO VARCHAR(11),
    FOREIGN KEY (CRM_MEDICO) REFERENCES MEDICO(CRM)
);
'''

conexao = conexao_mysql(host_name = getenv("host"), user_name = getenv("db_user"), user_password = getenv("password"), db_name = getenv("db_name"))
cursor = conexao.cursor()
cursor.execute(query_telefone_medico)