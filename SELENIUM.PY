import os
import zipfile
import time
import ssl
import certifi
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient

#ssl.create_default_context(cafile=certifi.where())

# Obtém o diretório corrente do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Configurações do WebDriver do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o navegador em modo headless (sem GUI)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--ignore-certificate-errors")  # Ignora erros de certificado SSL

# Diretório de download (diretório corrente do script)
download = script_dir

# Inicializa o ChromeDriver usando webdriver_manager
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL direta para o arquivo zip
URL = 'https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/taxa_transicao/tx_transicao_municipios_2019_2020.zip'

# Abre a URL
#driver.get(URL)

# Monitora o progresso do download
# while True:
#     # Verifica se existe um arquivo .crdownload no diretório de download
#     arquivo_em_download = next(
#         (f for f in os.listdir(download) if f.endswith('.crdownload')),
#         None
#     )

#     if arquivo_em_download:
#         arquivo_caminho = os.path.join(download, arquivo_em_download)
#         tamanho_atual = os.path.getsize(arquivo_caminho)
#         print(f"Progresso: {tamanho_atual} bytes")
#     else:
#         # Não há mais arquivo .crdownload, o download foi concluído
#         print('Download concluído.')
#         break

#     time.sleep(1)  # Aguarde 1 segundo antes de verificar novamente

# # Fecha o navegador
# driver.quit()

#Inicio descompacta arquivo zip
# download_dir = script_dir
# zip_filename = 'tx_transicao_municipios_2019_2020.zip'
# zip_filepath = os.path.join(download_dir, zip_filename)

# if (os.path.exists(zip_filepath)):
#     with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
#         zip_ref.extractall()
#         print('Arquivo zip extraído.')
# else:
#     print('Arquivo zip não encontrado.')
# # Fim descompacta arquivo zip 

# Inicio conexao com o banco de dados
try:
    # Configuração do MongoDB
    #connection_string = "mongodb+srv://leticiasistemasads:Devx@cluster0.rrh7i0u.mongodb.net/?retryWrites=true&w=majority"
    connection_string = "mongodb://root:example@localhost/?retryWrites=true&w=majority"

    client = MongoClient(connection_string, tls=False)
    db = client["TesteSebrae"]
    colecao = db["TesteSebrae.taxa_transicao/tx_transicao_municipios"]
    print('DB is up')

    # Caminho para o arquivo Excel (xlsx)
    xlsx_file = "/Users/letdevx/workspace/TesteSebrae/TX_TRANSICAO_MUNICIPIOS_2019_2020/TX_TRANSICAO_MUNICIPIOS_2019_2020.xlsx"
    print('caminho ok')
    # Ler o arquivo Excel usando pandas
    data = pd.read_excel(xlsx_file, engine='openpyxl', skiprows=5)
    print('arquivo lido')

    # Converter o DataFrame pandas em uma lista de dicionários
    data_dict = data.to_dict(orient="records")
    print('dataframe convertido')

    # Inserir os dados no MongoDB
    colecao.insert_many(data_dict)

    # for i, linha in enumerate(data_dict):
    #     colecao.insert_one(linha)

    print("Dados inseridos com sucesso no MongoDB.")





except ssl.SSLError as err:
   print(f"Erro SSL: {err}")
except Exception as erro:
  print("Conexao com o banco de dados falhou")
  print(f"Ocorreu um erro: {erro}")
# Fim conexao com o banco de dados