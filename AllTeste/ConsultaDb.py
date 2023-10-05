import pymongo
from pymongo import MongoClient


connection_string = "mongodb://root:example@localhost/?retryWrites=true&w=majority"
# Conecte-se ao servidor MongoDB (por padrão, em localhost na porta 27017)
client = MongoClient(connection_string, tls=False)

# Acesse um banco de dados específico
banco_de_dados = cliente["TesteSebrae"]

# Acesse uma coleção específica dentro do banco de dados
colecao = banco_de_dados["tx_transicao_municipios"]

# Realize uma consulta (por exemplo, buscar todos os documentos na coleção)
documentos = colecao.find()

# Itere sobre os resultados da consulta
for documento in documentos:
    print(documento)

# Feche a conexão quando terminar
cliente.close()
