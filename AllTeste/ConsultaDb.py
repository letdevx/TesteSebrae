import pymongo
from pymongo import MongoClient

# TODO: criar arquivo unico para fornecer client do Mongo

connection_string = "mongodb://root:example@localhost/?retryWrites=true&w=majority"
# Conecte-se ao servidor MongoDB (por padrão, em localhost na porta 27017)
client = MongoClient(connection_string, tls=False)

# Acesse um banco de dados específico
banco_de_dados = client["TesteSebrae"]

# Acesse uma coleção específica dentro do banco de dados
colecao = banco_de_dados["tx_transicao_municipios"]

documentos_filtrados = colecao.find(
    { "codigo_municipio": 1100023, "localizacao":"Total", "dependencia":"Total" },
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

for documento in documentos_filtrados:
    print(documento)

# Feche a conexão quando terminar
client.close()
