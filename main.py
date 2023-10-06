from AllTeste.DownloadPlanilha import DownloadPlanilha 
from AllTeste.leituraDeDados import InterpretaPlanilha
from AllTeste.DescompactaArquivoZip import Descompactazip
from AllTeste.Persistencia import SalvaDocumentosDB, ObtemTaxaTransicaoMunicipio
from AllTeste.PlotagemGrafico import PlotagemGrafico
import os
from config_loader import config

script_dir = os.path.dirname(os.path.abspath(__file__))

URL = config['planilha']['url']
caminho_planilha = os.path.join(script_dir, config['planilha']['pasta'], config['planilha']['arquivo'])

# caminho_planilha_zip = DownloadPlanilha(URL)
# Descompactazip(caminho_planilha_zip)
#documentos = InterpretaPlanilha(caminho_planilha)
#SalvaDocumentosDB(documentos)

documentos_filtrados = ObtemTaxaTransicaoMunicipio(codigo_municipio=1100023)
PlotagemGrafico(documentos_filtrados)
print('Fim')
