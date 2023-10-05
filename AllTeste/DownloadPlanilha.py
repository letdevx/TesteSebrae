import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inicio Configuração de cores no terminal.
GREEN = "\033[92m"       
RESET = "\033[0m"        
BOLD = "\033[1m"        
RED = "\033[91m"
# Fim Configuração de cores no terminal. 

def DownloadPlanilha(URL):
    """Realiza o download de um arquivo especificado pela URL"""
    
    try:
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
        download = os.path.join(script_dir, '..')

        # Inicializa o ChromeDriver usando webdriver_manager
        service = Service(executable_path=ChromeDriverManager().install()) #fornecer o caminho par o selenium 
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Abre a URL
        driver.get(URL)
        time.sleep(2)

        #Monitora o progresso do download
        arquivo_caminho = ''
        while True:
             # Verifica se existe um arquivo .crdownload no diretório de download
             arquivos_crdownload = (f for f in os.listdir(download) if f.endswith('.crdownload'))
             arquivo_em_download = next(
                 arquivos_crdownload,
                 None
             )

             if arquivo_em_download:
                arquivo_caminho = os.path.join(download, arquivo_em_download)
                tamanho_atual = os.path.getsize(arquivo_caminho)
                print( f"Progresso: {tamanho_atual} bytes")
             else:
                 # Não há mais arquivo .crdownload, o download foi concluído
                 print(GREEN+ "Download concluído!" +RESET)
                 break
             time.sleep(1)  # Aguarde 1 segundo antes de verificar novamente
         # Fecha o navegador
        driver.quit()
        return arquivo_caminho.removesuffix('.crdownload')
    
    except Exception as erro:
        print( RED + f"Erro: {str(erro)}" + RESET)
