import zipfile
import os

# Inicio Configuração de cores no terminal.
GREEN = "\033[92m"       
RESET = "\033[0m"        
BOLD = "\033[1m"        
RED = "\033[91m"
# Fim Configuração de cores no terminal. 

# Obtém o diretório corrente do script
script_dir = os.path.dirname(os.path.abspath(__file__))

def Descompactazip():
    try:
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

    except Exception as erro:
        print( RED + "Falha ao Descompactar arquivo" + RESET)
        print( RED + "Erro: {str(erro)}" + RESET)