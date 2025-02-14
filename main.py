from src.controller.readValue.readValue import readValue
from src.menu.menu import menu
from src.menu.menu import menuRead
from src.controller.addValue.addValue import addValue

while (True) :

    opcaoEscolhida  = menu()

    if (opcaoEscolhida == 1) :
        addValue()
        break
    if (opcaoEscolhida == 2) :
        while (True) :
            opcaoEscolhida = menuRead()
            flag = readValue(opcaoEscolhida)

            if opcaoEscolhida == 0 or  flag == 'n':
                break
        break
