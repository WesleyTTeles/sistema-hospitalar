from menu import *

"""
Aluno: Wesley Teixeira Teles
Turma: RAD Quarta Feira
"""

class main():
    def __init__(self):

        print("""
Bem vindo ao StarMed Seu Sistema Hospitalar

=============================
|           Menu            |
=============================

1 - Cadastrar Dados
2 - Alterar Dados
3 - Deletar Dados
4 - Associar Medico a Hospital
5 - Associar Paciente a Médico
6 - Associar Enfermeiro(a) a Hospital
7 - Relatórios
8 - Sair   
""")
        opcao_menu = int(input('Digite uma Opção Deseja: '))
        while opcao_menu != 8:
                menu_sistema(opcao_menu)
        
                opcao_menu = int(input('\n' + """
Digite a Opçao Desejada: 

1 - Cadastrar Dados
2 - Alterar Dados
3 - Deletar Dados
4 - Associar Medico a Hospital
5 - Associar Paciente a Médico
6 - Associar Enfermeiro(a) a Hospital
7 - Relatórios
8 - Sair  

"""))
        print('Obrigado por usar StarMed! Fechando o programa... ..')

main()
