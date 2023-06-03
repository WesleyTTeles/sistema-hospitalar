from cadastrar import *
from alterar import alterar_dados

def menu_sistema(opcao_menu):
                      
    match opcao_menu:
        case 1:
            cadastrar_dados()
        case 2:
            alterar_dados()
        case 3:
            pass
            #deletar_dados()
        case 4:
            associar_medico_hospital()
        case 5:
            associar_paciente_medico()
        case 6:
            associar_enfermeiro_hospital()
        case 7:
            opcao_relatorio = int(input("""
Escolha Qual Opção Deseja Listar:

1 - Listar Todos os Hospitais
2 - Listar todos os Médicos
3 - Listar todos os Pacientes
4 - Listar Pacientes que moram no Centro de Aracaju
5 - Listar médico e seus Telefones
6 - Listar corpo clínico
"""))       
        case 8:
            print('Obrigado por usar StarMed! Fechando o programa... ..')        
            quit()