from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

def PlotagemGrafico(documentos):
    dados_taxa_promocao = [d["taxa_promocao"] for d in documentos]
    dados_taxa_repetencia = [d["taxa_repetencia"] for d in documentos]
    dados_taxa_evasao = [d["taxa_evasao"] for d in documentos]
    dados_migracao_eja = [d["migracao_eja"] for d in documentos]

    niveis2d = [["ensino_fundamental", "ensino_medio"] for _ in dados_taxa_promocao]
    niveis = [elemento for sublista in niveis2d for elemento in sublista]
    totais2d = [[t["ensino_fundamental"]["total"], t["ensino_medio"]["total"]] for t in dados_taxa_promocao]
    totais = [elemento for sublista in totais2d for elemento in sublista]

    # Criar um arquivo Excel
    wb = Workbook()
    ws = wb.active # sheet

    # Adiciona os dados na planilha
    ws.append(niveis)
    ws.append(totais)

    # Criar um gráfico de barras no Excel
    chart = BarChart()
    chart.type = "col"
    chart.title = "Taxa de Promocao - Ariquemes 2"
    chart.x_axis.title = "Niveis"
    chart.y_axis.title = "Totais"

    data = Reference(ws, min_col=1, min_row=2, max_col=2, max_row=2) # Seleciona as células que contém os dados
    categories = Reference(ws, min_col=1, min_row=1, max_col=2, max_row=1) # Seleciona as células que contém as categorias
    chart.add_data(data, titles_from_data=True) # Adiciona os dados no gráfico
    chart.set_categories(categories) # Adicione as categorias (rótulos no eixo X)

    # Adicionar o gráfico ao Excel
    ws.add_chart(chart, "E5")

    # Salvar o arquivo Excel
    wb.save("taxa_transicao_ariquemes.xlsx")
     