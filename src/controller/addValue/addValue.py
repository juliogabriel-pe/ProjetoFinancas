import re
from src.model.service.add import addDoc

# Variaveis
boasVindas = 'Você selecionou a função para adicionar o valor comprado/parcelado'

# body
def addValue() :
    print(boasVindas)

    while (True) :

        while (True) :

            valorTotal = input('Digite o valor total: ')
            if not re.fullmatch(r'\d+,\d{1,2}|\d+', valorTotal):
                print(f'Você digitou algo inválido: {valorTotal}. Aceito apenas números com ou sem vírgula.')
            else:
                break

        obsValorTotal = input('Digite o tipo da compra ou deixe vazio: ')

        mesCompra = input('Digite o mês da compra (janeiro, fevereiro, ..., dezembro): ').lower()

        while (True) :

            parcelasValorTotal = input('Qual foi a quantidade de parcelas (se não tiver coloque 0): ')
            if not parcelasValorTotal.isnumeric() :
                print(f'Você digitou algo diferente de numero: {parcelasValorTotal}')
            else :
                break

        while (True) :

            cartaoValorTotal = input('Cartão usado (will, nubank, picpay): ').upper()
            if ( cartaoValorTotal not in ['WILL', 'NUBANK', 'PICPAY'] ) :
                print(f'Você digitou algo errado: {cartaoValorTotal}')
            else :
                break

        flag = input('Quer adicionar novamente? (Sim/Não): ').upper()
        if (flag == 'SIM') : 
            print('Reiniciando!')
            try: 
                addDoc(valorTotal, mesCompra, obsValorTotal, parcelasValorTotal, cartaoValorTotal)
                print('Salvo!')
            except:
                print('Erro ao salvar a compra')
        else :
            print('Encerrando o programa!')

            try :
                addDoc(valorTotal, mesCompra, obsValorTotal, parcelasValorTotal, cartaoValorTotal)
                print('Salvo!')
            except :
                print('Erro ao salvar a compra!')
            break
