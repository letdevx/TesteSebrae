from pymongo import MongoClient
from config_loader import config

# Inicio Configuração de cores no terminal.
GREEN = "\033[92m"       
RESET = "\033[0m"        
BOLD = "\033[1m"        
RED = "\033[91m"
# Fim Configuração de cores no terminal. 

connection_string = config['database']['connection_string']
client = MongoClient(connection_string, tls=False)
db = client["TesteSebrae"]
colecao = db["tx_transicao_municipios"]
print(GREEN +'\u2714 \033[1m DB is up'+ RESET)

def SalvaDocumentosDB(documentos):
    """"""
    try:
        # Inserir os dados no MongoDB
        colecao.insert_many(documentos)
        
        print( GREEN + " \u2714 \033[1m Dados inseridos com sucesso no MongoDB." + RESET)

    except Exception as err:
        print(RED + f"Erro: {err}" + RESET)
    
def ObtemTaxaTransicaoMunicipio(codigo_municipio):
    documentos_filtrados = colecao.find(
        { "codigo_municipio": codigo_municipio, "localizacao":"Total", "dependencia":"Total" },
        {"codigo_municipio":1,
        "nome_municipio":1, 
        "ano":1,
        "regiao":1,
        "uf":1,
        "localizacao":1,
        "dependencia":1,
        "taxa_promocao.ensino_fundamental.total":1, 
        "taxa_promocao.ensino_medio.total":1, 
        "taxa_repetencia.ensino_fundamental.total":1, 
        "taxa_repetencia.ensino_medio.total":1, 
        "taxa_evasao.ensino_fundamental.total":1,
        "taxa_evasao.ensino_medio.total":1,
        "migracao_eja.ensino_fundamental.total":1,
        "migracao_eja.ensino_medio.total":1})

    return list(documentos_filtrados)
