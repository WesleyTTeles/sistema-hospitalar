from cadastrar import cadastrar_dados

def menu_sistema(opcao_menu):
                      
    match opcao_menu:
        case 1:
            cadastrar_dados()
        case 2:
            pass
        case 3:
            pass
        case 4:
            opcao_relatorio = int(input("""
Escolha Qual Opção Deseja Listar:

1 - Listar Todos os Hospitais
2 - Listar todos os Médicos
3 - Listar todos os Pacientes
4 - Listar Pacientes que moram no Centro de Aracaju
5 - Listar médico e seus Telefones
6 - Listar corpo clínico
"""))
        case 5:
            print('Obrigado por usar StarMed! Fechando o programa... ..')        
