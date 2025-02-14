from src.model.service.read import readDoc

lista = readDoc()

def readValue(opcao):
    valores_mensais = {
        'janeiro': 0,
        'fevereiro': 0,
        'março': 0,
        'abril': 0,
        'maio': 0,
        'junho': 0,
        'julho': 0,
        'agosto': 0,
        'setembro': 0,
        'outubro': 0,
        'novembro': 0,
        'dezembro': 0
    }

    for doc in lista:
        mes_compra = doc.get('mes_compra', '').lower()
        valor = doc.get('valor', '0').replace(',', '.')
        if mes_compra in valores_mensais:
            try:
                valores_mensais[mes_compra] += float(valor)
            except ValueError:
                print(f"Erro ao converter o valor: {valor}")

    if opcao == 1:
        for mes, valor in valores_mensais.items():
            print(f"{mes.capitalize()}: {valor:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 2:
        print(f"Janeiro: {valores_mensais['janeiro']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 3:
        print(f"Fevereiro: {valores_mensais['fevereiro']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 4:
        print(f"Março: {valores_mensais['março']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 5:
        print(f"Abril: {valores_mensais['abril']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 6:
        print(f"Maio: {valores_mensais['maio']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 7:
        print(f"Junho: {valores_mensais['junho']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 8:
        print(f"Julho: {valores_mensais['julho']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 9:
        print(f"Agosto: {valores_mensais['agosto']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 10:
        print(f"Setembro: {valores_mensais['setembro']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 11:
        print(f"Outubro: {valores_mensais['outubro']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 12:
        print(f"Novembro: {valores_mensais['novembro']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
    elif opcao == 13:
        print(f"Dezembro: {valores_mensais['dezembro']:.2f}")
        flag = input('Continuar verificando (s/n): ').lower()
        return flag
