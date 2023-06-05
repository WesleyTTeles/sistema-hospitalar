from cadastrar_dados import *
from alterar_dados import alterar_dados
from deletar_dados import deletar_dados
from relatorio_dados import *

def menu_sistema(opcao_menu):
                      
    match opcao_menu:
        case 1:
            cadastrar_dados()
        case 2:
            alterar_dados()
        case 3:
            deletar_dados()
        case 4:
            associar_medico_hospital()
        case 5:
            associar_paciente_medico()
        case 6:
            associar_enfermeiro_hospital()
        case 7:
            associar_medico_enfermeiro()
        case 8:
            sub_menu()
        case 9:
            print('Obrigado por usar StarMed! Fechando o programa... ..')        
            quit()

def sub_menu():

    opc_sub = int(input("""
Escolha Qual Opção Deseja Listar:

1 - Listar Todos os Hospitais
2 - Listar todos os Médicos
3 - Listar todos os Pacientes
4 - Listar Pacientes que moram no Centro de Aracaju
5 - Listar médico e seus Telefones
6 - Listar corpo clínico
7 - Fechar o Programa
"""))  

    match opc_sub:
        case 1:
            listar_hospital()
        case 2:
            listar_medicos()
        case 3:
            listar_pacientes()
        case 4:
            listar_pacientes_aracaju()
        case 5:
            listar_medico_telefones()
        case 6:
            listar_corpo_clinico()
        case 7:
            print('Obrigado por usar StarMed! Fechando o programa... ..')
            quit()
        