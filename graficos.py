import streamlit as st
from PIL import Image

def grafico_ocorrencias_por_mes():
    # Caminho da imagem salva
    caminho_imagem = 'images/graficos/ocorrencias_mes.png'
    # Carrega a imagem
    imagem = Image.open(caminho_imagem)
    # Exibe a imagem no Streamlit
    st.image(imagem, use_column_width=True)

def grafico_ocorrencias_mensais():
    caminho_imagem = 'images/graficos/ocorrencias_mes_ano.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_boxplot_ocorrencias_mensais():
    caminho_imagem = 'images/graficos/ocorrencias_boxplot.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_top_10_tipos_acidentes():
    caminho_imagem = 'images/graficos/ocorrencias_freq.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_bottom_10_tipos_acidentes():
    caminho_imagem = 'images/graficos/ocorrencias_mfreq.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_distribuicao_tipos_incidentes():
    caminho_imagem = 'images/graficos/grafico_distribuicao_tipos_incidentes.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_tipos_incidentes_ano():
    caminho_imagem = 'images/graficos/grafico_tipos_incidentes_ano.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_tipos_aeronaves():
    caminho_imagem = 'images/graficos/grafico_tipos_aeronaves.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_top10_fabricantes():
    caminho_imagem = 'images/graficos/grafico_top10_fabricantes.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_ocorrencias_por_uf():
    caminho_imagem = 'images/graficos/grafico_ocorrencias_por_uf.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_quantidade_motores():
    caminho_imagem = 'images/graficos/grafico_quantidade_motores.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_top3_ufs_por_ano():
    caminho_imagem = 'images/graficos/grafico_top3_ufs_por_ano.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_ano_fabricacao_acidentes():
    caminho_imagem = 'images/graficos/grafico_ano_fabricacao_acidentes.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_heatmap_correlacao():
    caminho_imagem = 'images/graficos/grafico_heatmap_correlacao.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def plot_top_fatores():
    caminho_imagem = 'images/graficos/plot_top_fatores.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_fatores_condicionantes_por_periodo():
    caminho_imagem = 'images/graficos/grafico_fatores_condicionantes_por_periodo1.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

    caminho_imagem = 'images/graficos/grafico_fatores_condicionantes_por_periodo2.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_fator_nome_fator_aspecto():
    caminho_imagem = 'images/graficos/grafico_fator_nome_fator_aspecto1.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

    caminho_imagem = 'images/graficos/grafico_fator_nome_fator_aspecto2.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_fatores_cond_mais_freq():
    caminho_imagem = 'images/graficos/grafico_fatores_cond_mais_freq.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_fatores_2019_2020():
    caminho_imagem = 'images/graficos/grafico_fatores_2019_2020.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_ano_aeronaves():
    caminho_imagem = 'images/graficos/grafico_ano_aeronaves.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)

def grafico_ano_aeronaves_compacto():
    caminho_imagem = 'images/graficos/grafico_ano_aeronaves_compacto.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_column_width=True)
