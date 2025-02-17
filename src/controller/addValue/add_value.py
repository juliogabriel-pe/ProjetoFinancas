import re
from src.model.service.add import add_doc

# Variaveis
boas_vindas = 'Você selecionou a função para adicionar o valor comprado/parcelado'

# body
def add_value() :
    print(boas_vindas)

    while (True) :

        while (True) :

            valor_total = input('Digite o valor total: ')
            if not re.fullmatch(r'\d+,\d{1,2}|\d+', valor_total):
                print(f'Você digitou algo inválido: {valor_total}. Aceito apenas números com ou sem vírgula.')
            else:
                break

        obs_valor_total = input('Digite o tipo da compra ou deixe vazio: ')

        mes_compra = input('Digite o mês da compra (janeiro, fevereiro, ..., dezembro): ').lower()

        while (True) :

            parcelas_valor_total = input('Qual foi a quantidade de parcelas (se não tiver coloque 0): ')
            if not parcelas_valor_total.isnumeric() :
                print(f'Você digitou algo diferente de numero: {parcelas_valor_total}')
            else :
                break

        while (True) :

            cartao_valor_total = input('Cartão usado (will, nubank, picpay): ').upper()
            if ( cartao_valor_total not in ['WILL', 'NUBANK', 'PICPAY'] ) :
                print(f'Você digitou algo errado: {cartao_valor_total}')
            else :
                break

        flag = input('Quer adicionar novamente? (Sim/Não): ').upper()
        if (flag == 'SIM') : 
            print('Reiniciando!')
            try: 
                add_doc(valor_total, mes_compra, obs_valor_total, parcelas_valor_total, cartao_valor_total)
                print('Salvo!')
            except:
                print('Erro ao salvar a compra')
        else :
            print('Encerrando o programa!')

            try :
                add_doc(valor_total, mes_compra, obs_valor_total, parcelas_valor_total, cartao_valor_total)
                print('Salvo!')
            except :
                print('Erro ao salvar a compra!')
            break
