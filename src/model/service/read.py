from src.model.conexaoBanco.conexaoBanco import db

lista = {}

def readDoc() :

    colecao = db.collection('Compras')

    try :
        lista = colecao.get()
        documentos = [doc.to_dict() for doc in lista]
        return documentos
    except :
        print('Erro na busca dos dados!')
        return []
