from DownloadPlanilha import DownloadPlanilha 
from leituraDeDados import InterpretaPlanilha
from DescompactaArquivoZip import Descompactazip
from Persistencia import SalvaDocumentosDB
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# TODO: mover URL para config
# TODO: mover nome da pasta e arquivo da planilha para config
URL = 'https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/taxa_transicao/tx_transicao_municipios_2019_2020.zip'
caminho_planilha = os.path.join(script_dir, '..', 'TX_TRANSICAO_MUNICIPIOS_2019_2020', 'TX_TRANSICAO_MUNICIPIOS_2019_2020.xlsx')

caminho_planilha_zip = DownloadPlanilha(URL)
Descompactazip(caminho_planilha_zip)
documentos = InterpretaPlanilha(caminho_planilha)
SalvaDocumentosDB(documentos)
