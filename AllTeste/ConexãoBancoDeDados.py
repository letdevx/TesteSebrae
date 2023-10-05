from pymongo import MongoClient
import ssl
from leituraDeDados import InterpretaPlanilha
# Inicio Configuração de cores no terminal.
GREEN = "\033[92m"       
RESET = "\033[0m"        
BOLD = "\033[1m"        
RED = "\033[91m"
# Fim Configuração de cores no terminal. 

def ConexaoDB():
    # Inicio conexao com o banco de dados
    try:
        # Configuração do MongoDB
        #connection_string = "mongodb+srv://leticiasistemasads:Devx@cluster0.rrh7i0u.mongodb.net/?retryWrites=true&w=majority"
        connection_string = "mongodb://root:example@localhost/?retryWrites=true&w=majority"

        client = MongoClient(connection_string, tls=False)
        db = client["TesteSebrae"]
        colecao = db["tx_transicao_municipios"]
        print(GREEN +'\u2714 \033[1m DB is up'+ RESET)

        # Caminho para o arquivo Excel (xlsx)
        planilha = "./TX_TRANSICAO_MUNICIPIOS_2019_2020/TX_TRANSICAO_MUNICIPIOS_2019_2020.xlsx"
        documentos = InterpretaPlanilha(planilha)

        # Inserir os dados no MongoDB
        colecao.insert_many(documentos)
        
        print( GREEN + " \u2714 \033[1m Dados inseridos com sucesso no MongoDB." + RESET)

    except ssl.SSLError as err:
        print(RED + f"Erro SSL: {err}" + RESET)
    
    # Fim conexao com o banco de dados