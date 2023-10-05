import os
import zipfile
import time
import ssl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
from AllTeste.leituraDeDados import InterpretaPlanilha

# Inicio Configuração de cores no terminal.
GREEN = "\033[92m"       # Texto verde
RESET = "\033[0m"        # Reseta a formatação
BOLD = "\033[1m"         # Texto em negrito
# Fim Configuração de cores no terminal.

# Obtém o diretório corrente do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Inicio Configurações do WebDriver do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executa o navegador em modo headless (sem GUI)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--ignore-certificate-errors")  # Ignora erros de certificado SSL
# Fim Configurações do WebDriver do Chrome

# Diretório de download (diretório corrente do script)
download = script_dir

# Inicializa o ChromeDriver usando webdriver_manager
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL direta para o arquivo zip
URL = 'https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/taxa_transicao/tx_transicao_municipios_2019_2020.zip'

# Abre a URL
driver.get(URL)

# Monitora o progresso do download
while True:
    # Verifica se existe um arquivo .crdownload no diretório de download
    arquivo_em_download = next(
        (f for f in os.listdir(download) if f.endswith('.crdownload')),
        None
    )

    if arquivo_em_download:
        arquivo_caminho = os.path.join(download, arquivo_em_download)
        tamanho_atual = os.path.getsize(arquivo_caminho)
        print(f"Progresso: {tamanho_atual} bytes")
    else:
        # Não há mais arquivo .crdownload, o download foi concluído
        print('Download concluído.')
        break

    time.sleep(1)  # Aguarde 1 segundo antes de verificar novamente

# Fecha o navegador
driver.quit()

#Inicio descompacta arquivo zip
download_dir = script_dir
zip_filename = 'tx_transicao_municipios_2019_2020.zip'
zip_filepath = os.path.join(download_dir, zip_filename)

if (os.path.exists(zip_filepath)):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall()
        print('Arquivo zip extraído.')
else:
    print('Arquivo zip não encontrado.')
# Fim descompacta arquivo zip 

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
    xlsx_file = "./TX_TRANSICAO_MUNICIPIOS_2019_2020/TX_TRANSICAO_MUNICIPIOS_2019_2020.xlsx"
    documentos = InterpretaPlanilha(xlsx_file)

    # Inserir os dados no MongoDB
    colecao.insert_many(documentos)
    
    print( GREEN + " \u2714 \033[1m Dados inseridos com sucesso no MongoDB." + RESET)

except ssl.SSLError as err:
   print(f"Erro SSL: {err}")
except Exception as erro:
  print("Conexao com o banco de dados falhou")
  print(f"Ocorreu um erro: {erro}")
# Fim conexao com o banco de dados