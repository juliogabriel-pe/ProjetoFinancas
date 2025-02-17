from src.controller.readValue.read_value import read_value
from src.menu.menu import menu
from src.menu.menu import menu_read
from src.controller.addValue.add_value import add_value

while (True) :

    opcao_escolhida  = menu()

    if (opcao_escolhida == 1) :
        add_value()
        break
    elif (opcao_escolhida == 2) :
        while (True) :
            opcao_escolhida = menu_read()
            flag = read_value(opcao_escolhida)

            if opcao_escolhida == 0 or flag == 'n':
                break
    elif (opcao_escolhida == 0) :
        print('Obrigado e Volte sempre!')
        break
