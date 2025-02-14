import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.exceptions import FirebaseError

# Caminho para o arquivo JSON da chave privada
cred = credentials.Certificate('Seu Certificado')

# Verificar se já foi inicializado
if not firebase_admin._apps:
    try:
        # Inicializa o SDK com as credenciais
        firebase_admin.initialize_app(cred)
        print("Firebase inicializado com sucesso.")
    except FirebaseError as e:
        print(f'Erro ao inicializar o Firebase: {e}')

# Conecta-se ao Firestore
db = firestore.client()
