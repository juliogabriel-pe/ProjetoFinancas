# Variaveis
boas_vindas = 'Bem vindo ao programa de finanças'
menus = [
    '0. Sair do app',
    '1. Adicionar uma compra',
    '2. Verificador',
]
menus_2 = [
    '0. Sair da busca',
    '1. Verificar o Total',
    '2. Verificar Janeiro',
    '3. Verificar Fevereiro',
    '4. Verificar Março',
    '5. Verificar Abril',
    '6. Verificar Maio',
    '7. Verificar Junho',
    '8. Verificar Julho',
    '9. Verificar Agosto',
    '10. Verificar Setembro',
    '11. Verificar Outubro',
    '12. Verificar Novembro',
    '13. Verificar Dezembro',
]
saida = 'Obrigado por usar o sistema!'

# body
def menu():

    print(boas_vindas)
    print('Menu: ')

    while (True) :
        for x in menus:
            print(x)

        opcao = input('Escolha uma opção: ')

        if (opcao.isnumeric()) :
            opcao = int(opcao)
            if (opcao == 0) :
                print(saida)
                return opcao
            elif (opcao == 1) :
                print(f'Você escolheu a opção: ({menus[1]})')
                return opcao
            elif (opcao == 2) :
                print(f'Você escolheu a opção: ({menus[2]})')
                return opcao
            # elif (opcao == 3) :
            #     print(f'Você escolheu a opção: ({menus[3]})')
            #     return opcao
            else :
                print('Desculpe não conseguir entender!')
                pass
        else:
            print('Desculpe não conseguir entender!')
            pass

def menu_read():

    print('Aq vc pode selecionar os intervalos de busca!')
    print('Menu: ')

    while (True) :
        for x in menus_2:
            print(x)

        opcao = input('Escolha uma opção: ')

        if (opcao.isnumeric()) :
            opcao = int(opcao)
            if (opcao == 0) :
                print(saida)
                return opcao
            elif (opcao == 1) :
                print(f'Você escolheu a opção: ({menus_2[1]})')
                return opcao
            elif (opcao == 2) :
                print(f'Você escolheu a opção: ({menus_2[2]})')
                return opcao
            elif (opcao == 3) :
                print(f'Você escolheu a opção: ({menus_2[3]})')
                return opcao
            elif (opcao == 4) :
                print(f'Você escolheu a opção: ({menus_2[4]})')
                return opcao
            elif (opcao == 5) :
                print(f'Você escolheu a opção: ({menus_2[5]})')
                return opcao
            elif (opcao == 6) :
                print(f'Você escolheu a opção: ({menus_2[6]})')
                return opcao
            elif (opcao == 7) :
                print(f'Você escolheu a opção: ({menus_2[7]})')
                return opcao
            elif (opcao == 8) :
                print(f'Você escolheu a opção: ({menus_2[8]})')
                return opcao
            elif (opcao == 9) :
                print(f'Você escolheu a opção: ({menus_2[9]})')
                return opcao
            elif (opcao == 10) :
                print(f'Você escolheu a opção: ({menus_2[10]})')
                return opcao
            elif (opcao == 11) :
                print(f'Você escolheu a opção: ({menus_2[11]})')
                return opcao
            elif (opcao == 12) :
                print(f'Você escolheu a opção: ({menus_2[12]})')
                return opcao
            elif (opcao == 13) :
                print(f'Você escolheu a opção: ({menus_2[13]})')
                return opcao
            else :
                print('Desculpe não conseguir entender!')
                pass
        else:
            print('Desculpe não conseguir entender!')
            pass