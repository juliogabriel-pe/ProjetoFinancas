from src.model.conexaoBanco.conexao_banco import DB

lista = {}

def read_doc() :

    colecao = DB.collection('Compras')

    try :
        lista = colecao.get()
        documentos = [doc.to_dict() for doc in lista]
        return documentos
    except :
        print('Erro na busca dos dados!')
        return []
