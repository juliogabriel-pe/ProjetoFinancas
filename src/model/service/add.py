from src.model.conexaoBanco.conexaoBanco import db
from datetime import datetime

def addDoc(valor, mesCompra, obs, parcelas, cartaoUsado) :

    dadosDoc = {
        'valor' : valor,
        'mes_compra' : mesCompra,
        'observacao' : obs,
        'parcela' : True if int(parcelas) > 0 else False,
        'quantidade_parcelas' : int(parcelas),
        'cartao_usado' : cartaoUsado,
        'ano' : datetime.now().strftime('%Y'),
        'data_adicao' : datetime.now().strftime('%d/%m/%Y'),
    }

    colecao = db.collection('Compras')

    try : 
        colecao.add(dadosDoc)
    except :
        print('Erro ao tentar salvar compras!')
