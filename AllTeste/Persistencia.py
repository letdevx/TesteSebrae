from pymongo import MongoClient
from config_loader import config

# Inicio Configuração de cores no terminal.
GREEN = "\033[92m"       
RESET = "\033[0m"        
BOLD = "\033[1m"        
RED = "\033[91m"
# Fim Configuração de cores no terminal. 

def SalvaDocumentosDB(documentos):
    """"""
    try:
        connection_string = config['database']['connection_string']
        client = MongoClient(connection_string, tls=False)
        db = client["TesteSebrae"]
        colecao = db["tx_transicao_municipios"]
        print(GREEN +'\u2714 \033[1m DB is up'+ RESET)

        # Inserir os dados no MongoDB
        colecao.insert_many(documentos)
        
        print( GREEN + " \u2714 \033[1m Dados inseridos com sucesso no MongoDB." + RESET)

    except Exception as err:
        print(RED + f"Erro: {err}" + RESET)
    
    