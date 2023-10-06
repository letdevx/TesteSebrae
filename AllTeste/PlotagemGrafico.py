import matplotlib.pyplot as plt
import pandas as pd

def PlotagemGrafico(documentos):
    dados_taxa_promocao = [d["taxa_promocao"] for d in documentos]

    niveis2d = [["ensino_fundamental", "ensino_medio"] for _ in dados_taxa_promocao]
    niveis = [elemento for sublista in niveis2d for elemento in sublista]
    totais2d = [[t["ensino_fundamental"]["total"], t["ensino_medio"]["total"]] for t in dados_taxa_promocao]
    totais = [elemento for sublista in totais2d for elemento in sublista]

    dados = { "Niveis": niveis,
              "Totais": totais }
    
    df = pd.DataFrame(dados)

    df.plot(kind='bar', x='Niveis', y='Totais', color='skyblue', edgecolor='black', legend=True, title='Taxa de Promocao - Ariquemes')
    
    print("fim")
     