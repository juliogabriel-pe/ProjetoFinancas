from src.model.conexaoBanco.conexao_banco import DB
from datetime import datetime

def add_doc(valor, mes_compra, obs, parcelas, cartao_usado) :

    dados_doc = {
        'valor' : valor,
        'mes_compra' : mes_compra,
        'observacao' : obs,
        'parcela' : True if int(parcelas) > 0 else False,
        'quantidade_parcelas' : int(parcelas),
        'cartao_usado' : cartao_usado,
        'ano' : datetime.now().strftime('%Y'),
        'data_adicao' : datetime.now().strftime('%d/%m/%Y'),
    }

    colecao = DB.collection('Compras')

    try : 
        colecao.add(dados_doc)
    except :
        print('Erro ao tentar salvar compras!')
