import pandas as pd 

def interpretaPlanilha(caminhoPlanilha):
    #caminhoPlanilha = './TX_TRANSICAO_MUNICIPIOS_2019_2020/TX_TRANSICAO_MUNICIPIOS_2019_2020.xlsx'

    #leitura da planinilia
    print('Lendo planilha...')
    df = pd.read_excel(caminhoPlanilha, skiprows=8)
    # Verificar os dados lidos
    print(df.head())

    #Iincio CoNVERTENDO  dados em dicionario
    documentos = []

    for _, row in df.iterrows():
        documento = {
            "ano": row["ANO"],
            "regiao":row["NO_REGIAO"],
            "uf":row["NO_UF"],
            "codigo_municipio":row["CO_MUNICIPIO"],    
            "nome_municipio": row["NO_MUNICIPIO"],
            "localizacao":row["TIPOLOCA"],
            "dependencia":row["DEPENDAD"],
            "taxa_promocao":{
                "ensino_fundamental":{
                    "total":row["TXPRO_FUN"],
                    "anos_iniciais":row["TXPRO_F14"],
                    "anos_finais":row["TXPRO_F58"],
                    "ano1": row["TXPRO_F00"],
                    "ano2": row["TXPRO_F01"],
                    "ano3": row["TXPRO_F02"],
                    "ano4": row["TXPRO_F03"],
                    "ano5": row["TXPRO_F04"],
                    "ano6": row["TXPRO_F05"],
                    "ano7": row["TXPRO_F06"],
                    "ano8": row["TXPRO_F07"],
                    "ano9": row["TXPRO_F08"]
                },
                "ensino_medio":{
                    "total":row["TXPRO_MED"],
                    "ano1": row["TXPRO_M01"],
                    "ano2": row["TXPRO_M02"],
                    "ano3": row["TXPRO_M03"]
                }, 
            },
            "taxa_repetencia": {
                "ensino_fundamental": {
                    "total": row["TXREP_FUN"],
                    "anos_iniciais":row["TXREP_F14"],
                    "anos_finais": row["TXREP_F58"],
                    "ano1": row["TXREP_F00"],
                    "ano2": row["TXREP_F01"],
                    "ano3": row["TXREP_F02"],
                    "ano4": row["TXREP_F03"],
                    "ano5": row["TXREP_F04"],
                    "ano6": row["TXREP_F05"],
                    "ano7": row["TXREP_F06"],
                    "ano8": row["TXREP_F07"],
                    "ano9": row["TXREP_F08"]
                },
                "ensino_medio": {
                    "total": row["TXREP_MED"],
                    "ano1": row["TXREP_M01"],
                    "ano2": row["TXREP_M02"],
                    "ano3": row["TXREP_M03"]
                }
            },
            "taxa_evasao": {
                "ensino_fundamental": {
                    "total": row["TXEVE_FUN"],
                    "anos_iniciais": row["TXEVE_F14"],
                    "anos_finais": row["TXEVE_F58"],
                    "ano1": row["TXEVE_F00"],
                    "ano2": row["TXEVE_F01"],
                    "ano3": row["TXEVE_F02"],
                    "ano4": row["TXEVE_F03"],
                    "ano5": row["TXEVE_F04"],
                    "ano6": row["TXEVE_F05"],
                    "ano7": row["TXEVE_F06"],
                    "ano8": row["TXEVE_F07"],
                    "ano9": row["TXEVE_F08"]
                },
                "ensino_medio": {
                    "total": row["TXEVE_MED"],
                    "ano1": row["TXEVE_M01"],
                    "ano2": row["TXEVE_M02"],
                    "ano3": row["TXEVE_M03"]
                }
            },
            "migracao_eja": {
                "ensino_fundamental": {
                    "total": row["TXEVM_FUN"],
                    "anos_iniciais": row["TXEVM_F14"],
                    "anos_finais": row["TXEVM_F58"],
                    "ano1": row["TXEVM_F00"],
                    "ano2": row["TXEVM_F01"],
                    "ano3": row["TXEVM_F02"],
                    "ano4": row["TXEVM_F03"],
                    "ano5": row["TXEVM_F04"],
                    "ano6": row["TXEVM_F05"],
                    "ano7": row["TXEVM_F06"],
                    "ano8": row["TXEVM_F07"],
                    "ano9": row["TXEVM_F08"]
                },
                "ensino_medio": {
                    "total": row["TXEVM_MED"],
                    "ano1": row["TXEVM_M01"],
                    "ano2": row["TXEVM_M02"],
                    "ano3": row["TXEVM_M03"]
                }
            }
        }   
        documentos.append(documento)
    #Fim CoNVERTENDO  dados em dicionario
    print('Planilha interpretada com sucesso')

    return documentos
