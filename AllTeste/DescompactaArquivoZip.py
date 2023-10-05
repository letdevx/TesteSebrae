import zipfile
import os

# Inicio Configuração de cores no terminal.
GREEN = "\033[92m"       
RESET = "\033[0m"        
BOLD = "\033[1m"        
RED = "\033[91m"
# Fim Configuração de cores no terminal. 

def Descompactazip(zip_filepath):
    try:
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