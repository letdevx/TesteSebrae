import pymongo

# Conecte-se ao servidor MongoDB (por padrão, em localhost na porta 27017)
cliente = pymongo.MongoClient("mongodb://localhost:27017/")

# Acesse um banco de dados específico
banco_de_dados = cliente["nome_do_banco_de_dados"]

# Acesse uma coleção específica dentro do banco de dados
colecao = banco_de_dados["nome_da_colecao"]

# Realize uma consulta (por exemplo, buscar todos os documentos na coleção)
documentos = colecao.find()

# Itere sobre os resultados da consulta
for documento in documentos:
    print(documento)

# Feche a conexão quando terminar
cliente.close()
