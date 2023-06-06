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
7 - Associar Enfermeiro(a) à Médico
8 - Relatórios
9 - Sair   
""")
        try:
                opcao_menu = int(input('Digite uma Opção Deseja: '))
                while opcao_menu != 9:
                        menu_sistema(opcao_menu)
                
                        opcao_menu = int(input('\n' + """
Digite a Opçao Desejada: 

1 - Cadastrar Dados
2 - Alterar Dados
3 - Deletar Dados
4 - Associar Medico a Hospital
5 - Associar Paciente a Médico
6 - Associar Enfermeiro(a) a Hospital
7 - Associar Enfermeiro(a) à Médico
8 - Relatórios
9 - Sair  
"""))
                print('Obrigado por usar StarMed! Fechando o programa... ..')
        except ValueError:
              print('\n!!!! Opção Inválida Fechando o programa... .. !!!!')

main()
