import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def grafico_ocorrencias_por_mes():
    # Carrega os dados
    df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Converte para datetime
    df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'], dayfirst=True, errors='coerce')

    # Filtra datas válidas
    df = df[df['ocorrencia_dia'].notna()]

    # Extrai ano e mês
    df['ano'] = df['ocorrencia_dia'].dt.year
    df['mes'] = df['ocorrencia_dia'].dt.month

    # Filtra intervalo de interesse
    df = df[df['ano'].between(2007, 2023)]

    # Agrupa por ano e mês
    ocorrencias_mes = df.groupby(['ano', 'mes']).size().reset_index(name='ocorrencias')

    # Traduz os meses para nome
    meses = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    ocorrencias_mes['mes_nome'] = ocorrencias_mes['mes'].map(meses)

    # Ordena os meses corretamente
    ocorrencias_mes['mes_nome'] = pd.Categorical(ocorrencias_mes['mes_nome'], categories=meses.values(), ordered=True)

    # Cria gráfico interativo com facetas por ano
    fig = px.bar(
        ocorrencias_mes,
        x='mes_nome',
        y='ocorrencias',
        facet_col='ano',
        facet_col_wrap=4,
        color='ocorrencias',
        color_continuous_scale='Blues',
        labels={'mes_nome': 'Mês', 'ocorrencias': 'Número de Ocorrências'},
        title='Número de Ocorrências por Mês (2007–2023)'
    )

    # Ajusta layout
    fig.update_layout(height=1000, showlegend=False)
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  # Remove "ano=" do título

    # Exibe no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_ocorrencias_mensais():
    # Lê o arquivo CSV
    df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Converte para datetime
    df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'], format='%d/%m/%Y', errors='coerce')
    df = df.dropna(subset=['ocorrencia_dia'])

    # Extrai ano e mês
    df['ano'] = df['ocorrencia_dia'].dt.year
    df['mes'] = df['ocorrencia_dia'].dt.month

    # Cria DataFrame agrupado
    ocorrencias = df.groupby(['ano', 'mes']).size().reset_index(name='quantidade')

    # Mapeia os meses para nomes
    meses_nome = {
        1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
    }
    ocorrencias['mes_nome'] = ocorrencias['mes'].map(meses_nome)

    # Ordena os meses corretamente
    ocorrencias['mes_nome'] = pd.Categorical(ocorrencias['mes_nome'], categories=list(meses_nome.values()), ordered=True)

    # Widget para selecionar anos
    #anos_disponiveis = sorted(ocorrencias['ano'].unique(), reverse=True)
    anos_disponiveis = sorted([ano for ano in ocorrencias['ano'].unique() if ano not in (2024, 2025)], reverse=True)
    anos_selecionados = st.multiselect('Selecione os anos para visualizar:', anos_disponiveis, default=anos_disponiveis[:5])

    # Filtra os dados
    dados_filtrados = ocorrencias[ocorrencias['ano'].isin(anos_selecionados)]

    # Gráfico interativo
    fig = px.line(
        dados_filtrados,
        x='mes_nome',
        y='quantidade',
        color='ano',
        markers=True,
        title='Ocorrências Mensais por Ano',
        labels={'mes_nome': 'Mês', 'quantidade': 'Número de Ocorrências', 'ano': 'Ano'}
    )

    fig.update_layout(xaxis_title='Mês', yaxis_title='Número de Ocorrências', legend_title='Ano')

    # Mostra no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_boxplot_ocorrencias_mensais():
    # Lê o CSV
    df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Converte datas
    df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'], format='%d/%m/%Y', errors='coerce')

    # Remove valores nulos
    df = df.dropna(subset=['ocorrencia_dia'])

    # Extrai ano e mês
    df['ano'] = df['ocorrencia_dia'].dt.year
    df['mes'] = df['ocorrencia_dia'].dt.month

    # Agrupa por ano e mês
    dados_por_mes_ano = df.groupby(['ano', 'mes']).size().reset_index(name='ocorrencias')

    # Filtra para anos válidos (excluindo anos futuros, se desejar)
    dados_por_mes_ano = dados_por_mes_ano[dados_por_mes_ano['ano'] <= 2023]

    # Cria nome do mês (opcional, para tornar mais legível)
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    dados_por_mes_ano['mes_nome'] = dados_por_mes_ano['mes'].apply(lambda x: meses[x-1])

    # Gráfico interativo com Plotly
    fig = px.box(
        dados_por_mes_ano,
        x='mes_nome',
        y='ocorrencias',
        points='all',  # mostra pontos individuais também
        title='Distribuição das Ocorrências Mensais ao Longo dos Anos',
        labels={'mes_nome': 'Mês', 'ocorrencias': 'Número de Ocorrências'},
        template='plotly_white',
        color_discrete_sequence=['teal']
    )

    fig.update_traces(marker=dict(size=5, opacity=0.5))  # pontos mais leves
    fig.update_layout(xaxis_title='Mês', yaxis_title='Ocorrências', showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

def grafico_top_10_tipos_acidentes():
    # Carrega os dados
    acidentes_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    tipos_acidentes_df = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Merge
    acidentes_com_tipos_df = pd.merge(acidentes_df, tipos_acidentes_df, on='codigo_ocorrencia1')

    # Conta os tipos e seleciona top 10
    tipos_acidentes_counts = acidentes_com_tipos_df['ocorrencia_tipo_categoria'].value_counts().head(10).reset_index()
    tipos_acidentes_counts.columns = ['Tipo de Acidente', 'Quantidade']

    # Gráfico de barras interativo
    fig = px.bar(
        tipos_acidentes_counts,
        x='Tipo de Acidente',
        y='Quantidade',
        text='Quantidade',
        color='Quantidade',
        color_continuous_scale='Blues',
        title='Top 10 Tipos de Acidentes',
        labels={'Quantidade': 'Número de Ocorrências', 'Tipo de Acidente': 'Tipo de Acidente'},
        template='plotly_white',
        height=500
    )

    fig.update_traces(
        textposition='outside',
        marker_line_width=1.5,
        marker_line_color='darkblue'
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        coloraxis_showscale=False,
        yaxis=dict(title='Número de Ocorrências', gridcolor='LightGray'),
        xaxis=dict(tickfont=dict(size=12))
    )

    st.plotly_chart(fig, use_container_width=True)

def grafico_bottom_10_tipos_acidentes():
    # Carrega os dados
    acidentes_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    tipos_acidentes_df = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Merge
    acidentes_com_tipos_df = pd.merge(acidentes_df, tipos_acidentes_df, on='codigo_ocorrencia1')

    # Conta os tipos e pega os 10 menos frequentes
    tipos_acidentes_counts = acidentes_com_tipos_df['ocorrencia_tipo_categoria'].value_counts()
    bottom_10_tipos = tipos_acidentes_counts.nsmallest(10).reset_index()
    bottom_10_tipos.columns = ['Tipo de Acidente', 'Quantidade']

    # Cria o gráfico de barras interativo
    fig = px.bar(
        bottom_10_tipos,
        x='Tipo de Acidente',
        y='Quantidade',
        text='Quantidade',
        color='Quantidade',
        color_continuous_scale='Reds',
        title='10 Tipos de Ocorrência Menos Frequentes',
        labels={'Quantidade': 'Número de Ocorrências', 'Tipo de Acidente': 'Tipo de Acidente'},
        template='plotly_white',
        height=500
    )

    fig.update_traces(
        textposition='outside',
        marker_line_width=1.5,
        marker_line_color='darkred'
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        coloraxis_showscale=False,
        yaxis=dict(title='Número de Ocorrências', gridcolor='LightGray'),
        xaxis=dict(tickfont=dict(size=12))
    )

    st.plotly_chart(fig, use_container_width=True)

def grafico_distribuicao_tipos_incidentes():
    # Carrega os dados
    acidentes_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    tipos_acidentes_df = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Merge
    acidentes_com_tipos_df = pd.merge(acidentes_df, tipos_acidentes_df, on='codigo_ocorrencia1')

    # Conta os tipos ICAO
    tipos_acidentes_counts = acidentes_com_tipos_df['taxonomia_tipo_icao'].value_counts().reset_index()
    tipos_acidentes_counts.columns = ['Tipo de Incidente', 'Quantidade']

    # Cria o gráfico de barras interativo
    fig = px.bar(
        tipos_acidentes_counts,
        x='Tipo de Incidente',
        y='Quantidade',
        text='Quantidade',
        color='Quantidade',
        color_continuous_scale='Blues',
        title='Distribuição dos Tipos de Incidentes',
        labels={'Quantidade': 'Número de Ocorrências', 'Tipo de Incidente': 'Tipo de Incidente'},
        template='plotly_white',
        height=600
    )

    fig.update_traces(textposition='outside', marker_line_width=1, marker_line_color='darkblue')
    fig.update_layout(
        xaxis_tickangle=-45,
        coloraxis_showscale=False,
        yaxis=dict(title='Número de Ocorrências', gridcolor='LightGray'),
        xaxis=dict(tickfont=dict(size=12))
    )

    st.plotly_chart(fig, use_container_width=True)

def grafico_tipos_incidentes_ano():
    # Carrega os dados
    acidentes_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    tipos_acidentes_df = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Renomeia coluna para merge
    tipos_acidentes_df = tipos_acidentes_df.rename(columns={'codigo_ocorrencia1': 'codigo_ocorrencia'})

    # Merge dos dados
    acidentes_com_tipos_df = pd.merge(acidentes_df, tipos_acidentes_df, on='codigo_ocorrencia', how='left')

    # Converte coluna de data
    acidentes_com_tipos_df['ocorrencia_dia'] = pd.to_datetime(acidentes_com_tipos_df['ocorrencia_dia'], format='%d/%m/%Y', errors='coerce')

    # Extrai ano
    acidentes_com_tipos_df['ano'] = acidentes_com_tipos_df['ocorrencia_dia'].dt.year

    # Obtém lista de anos disponíveis para seleção
    anos_disponiveis = sorted(acidentes_com_tipos_df['ano'].dropna().unique())

    # Caixa de seleção para escolher um ou mais anos
    anos_selecionados = st.multiselect(
        'Selecione os anos',
        options=anos_disponiveis,
        default=[2024] if 2024 in anos_disponiveis else [anos_disponiveis[-1]]
    )

    if not anos_selecionados:
        st.warning("Selecione ao menos um ano para mostrar o gráfico.")
        return

    # Filtra os dados pelos anos selecionados
    df_filtrado = acidentes_com_tipos_df[acidentes_com_tipos_df['ano'].isin(anos_selecionados)]

    # Conta os tipos de incidentes por ano
    tipos_counts = (
        df_filtrado.groupby(['ano', 'taxonomia_tipo_icao'])
        .size()
        .reset_index(name='Quantidade')
    )

    # Gráfico interativo Plotly com barras agrupadas por ano
    fig = px.bar(
        tipos_counts,
        x='taxonomia_tipo_icao',
        y='Quantidade',
        color='ano',
        barmode='group',
        text='Quantidade',
        title=f'Distribuição dos Tipos de Incidentes para os Anos Selecionados',
        labels={'taxonomia_tipo_icao': 'Tipo de Incidente', 'Quantidade': 'Número de Ocorrências', 'ano': 'Ano'},
        template='plotly_white',
        height=600
    )

    fig.update_traces(textposition='outside', marker_line_width=1)
    fig.update_layout(
        xaxis_tickangle=-45,
        yaxis=dict(title='Número de Ocorrências', gridcolor='LightGray'),
        xaxis=dict(tickfont=dict(size=12)),
        legend_title_text='Ano'
    )

    st.plotly_chart(fig, use_container_width=True)

def grafico_tipos_aeronaves():
    acidentes_df = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Conta os tipos de aeronaves
    counts = acidentes_df['aeronave_tipo_veiculo'].value_counts().reset_index()
    counts.columns = ['Tipo de Aeronave', 'Número de Ocorrências']

    # Gráfico de barras interativo
    fig = px.bar(
        counts,
        x='Tipo de Aeronave',
        y='Número de Ocorrências',
        text='Número de Ocorrências',
        title='Tipos de Aeronaves Envolvidas (2007–2023)',
        labels={'Tipo de Aeronave': 'Tipo de Aeronave', 'Número de Ocorrências': 'Número de Ocorrências'},
        color='Número de Ocorrências',
        color_continuous_scale='Blues',
        template='plotly_white',
        height=600
    )

    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_tickangle=-45,
        xaxis_tickfont_size=11,
        yaxis=dict(gridcolor='LightGray'),
        coloraxis_showscale=False,
        margin=dict(t=80, b=120)
    )

    st.plotly_chart(fig, use_container_width=True)

def grafico_top10_fabricantes():
    acidentes_df = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    
    # Limpa dados e filtra fabricantes válidos
    df = acidentes_df.replace("***", pd.NA).dropna(subset=['aeronave_fabricante'])
    
    # Conta e seleciona top 10 fabricantes
    counts = df['aeronave_fabricante'].value_counts().head(10).reset_index()
    counts.columns = ['Fabricante', 'Número de Ocorrências']
    
    # Cria gráfico de pizza
    fig = px.pie(
        counts,
        names='Fabricante',
        values='Número de Ocorrências',
        title='Top 10 Fabricantes de Aeronaves',
        hover_data=['Número de Ocorrências'],
        labels={'Número de Ocorrências': 'Número de Ocorrências'},
        color_discrete_sequence=px.colors.sequential.Reds
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        legend_title_text='Fabricante',
        margin=dict(t=80, b=80, l=80, r=80)
    )
    
    # Exibe no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_ocorrencias_por_uf():
    acidentes_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    
    # Limpa dados e filtra UFs válidas
    df = acidentes_df.replace("***", pd.NA).dropna(subset=['ocorrencia_uf'])
    
    # Conta ocorrências por UF
    counts = df['ocorrencia_uf'].value_counts().reset_index()
    counts.columns = ['Estado', 'Número de Ocorrências']
    
    # Cria gráfico de pizza
    fig = px.pie(
        counts,
        names='Estado',
        values='Número de Ocorrências',
        title='Frequência de Ocorrências por Estado',
        hover_data=['Número de Ocorrências'],
        labels={'Número de Ocorrências': 'Número de Ocorrências'},
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        legend_title_text='Estado',
        margin=dict(t=80, b=80, l=80, r=80)
    )
    
    # Exibe no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_quantidade_motores():
    acidentes_df = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    df = acidentes_df.replace("***", pd.NA).dropna(subset=['aeronave_motor_quantidade'])

    counts = df['aeronave_motor_quantidade'].value_counts().reset_index()
    counts.columns = ['Quantidade de Motores', 'Número de Ocorrências']
    counts['Quantidade de Motores'] = counts['Quantidade de Motores'].astype(str)

    # Criar coluna "root" para o Sunburst
    counts['root'] = 'Motores'

    fig = px.sunburst(
        counts,
        path=['root', 'Quantidade de Motores'],
        values='Número de Ocorrências',
        color='Número de Ocorrências',
        color_continuous_scale='Teal',
        title='Distribuição de Quantidade de Motores'
    )

    fig.update_layout(margin=dict(t=50, l=0, r=0, b=0))

    st.plotly_chart(fig, use_container_width=True)

def grafico_top3_ufs_por_ano():
    # Carrega os dados
    acidentes_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    df = acidentes_df.replace("***", pd.NA).dropna(subset=['ocorrencia_uf'])

    # Top 3 UFs
    top3 = df['ocorrencia_uf'].value_counts().head(3).index
    df = df[df['ocorrencia_uf'].isin(top3)]

    # Conversão da data
    df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'], format='%d/%m/%Y', errors='coerce')
    df['ano'] = df['ocorrencia_dia'].dt.year

    # Agrupa os dados por ano e UF
    df_grouped = df.groupby(['ano', 'ocorrencia_uf']).size().reset_index(name='ocorrencias')

    # Gráfico interativo com Plotly
    fig = px.line(
        df_grouped,
        x='ano',
        y='ocorrencias',
        color='ocorrencia_uf',
        markers=True,
        labels={
            'ano': 'Ano',
            'ocorrencias': 'Número de Ocorrências',
            'ocorrencia_uf': 'UF'
        },
        title='Ocorrências ao Longo dos Anos (Top 3 UFs)'
    )

    fig.update_layout(
        xaxis=dict(dtick=1),  # mostra todos os anos
        yaxis=dict(title='Número de Ocorrências'),
        legend_title='Unidade Federativa',
        template='plotly_white'
    )

    # Mostra no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_ano_fabricacao_acidentes():
    # Carrega e prepara os dados
    acidentes_df = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    df = acidentes_df.replace("***", pd.NA).dropna(subset=['aeronave_ano_fabricacao'])
    df['aeronave_ano_fabricacao'] = pd.to_numeric(df['aeronave_ano_fabricacao'], errors='coerce')
    df = df.dropna(subset=['aeronave_ano_fabricacao'])

    # Agrupamento por ano
    dados = df['aeronave_ano_fabricacao'].value_counts().sort_index().reset_index()
    dados.columns = ['ano_fabricacao', 'quantidade']

    # Filtro opcional para visualização
    dados = dados[(dados['ano_fabricacao'] >= 1930) & (dados['ano_fabricacao'] <= 2020)]

    # Gráfico de área interativo
    fig = px.area(
        dados,
        x='ano_fabricacao',
        y='quantidade',
        labels={
            'ano_fabricacao': 'Ano de Fabricação',
            'quantidade': 'Número de Aeronaves'
        },
        title='Ano de Fabricação das Aeronaves Envolvidas em Ocorrências',
        template='plotly_white'
    )

    fig.update_traces(line_color='dodgerblue', fillcolor='rgba(30, 144, 255, 0.3)')
    fig.update_layout(
        xaxis=dict(dtick=10, tickangle=45),
        yaxis=dict(range=[0, dados['quantidade'].max() + 50]),
        hovermode='x unified'
    )

    st.plotly_chart(fig, use_container_width=True)

def grafico_heatmap_correlacao():
    # Leitura dos dados
    df_o = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    df_t = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    df_a = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Limpeza e merge
    o = df_o.replace("***", pd.NA).set_index(df_o.columns[0])
    t = df_t.replace("***", pd.NA).set_index(df_t.columns[0])
    a = df_a.replace("***", pd.NA).set_index(df_a.columns[0])
    df = o.join(t, how='left').join(a, how='left')
    df = df.dropna(subset=[
        'aeronave_ano_fabricacao', 'ocorrencia_uf',
        'aeronave_fabricante', 'aeronave_tipo_veiculo',
        'taxonomia_tipo_icao'
    ])

    # Codificação de variáveis categóricas
    for col in ['ocorrencia_uf', 'aeronave_fabricante', 'aeronave_tipo_veiculo', 'taxonomia_tipo_icao']:
        df[col] = df[col].astype('category').cat.codes
    df['aeronave_ano_fabricacao'] = pd.to_numeric(df['aeronave_ano_fabricacao'], errors='coerce')

    # Mapas legíveis
    col_map = {
        'aeronave_ano_fabricacao': 'Ano de Fabricação',
        'ocorrencia_uf': 'Estado da Ocorrência',
        'aeronave_fabricante': 'Fabricante',
        'aeronave_tipo_veiculo': 'Tipo de Aeronave',
        'taxonomia_tipo_icao': 'Tipo ICAO'
    }
    inv_col_map = {v: k for k, v in col_map.items()}
    cols_legiveis = list(col_map.values())
    cols_tecnicos = list(col_map.keys())

    # Heatmap
    corr = df[cols_tecnicos].corr()
    heatmap = px.imshow(
        corr,
        x=[col_map[c] for c in cols_tecnicos],
        y=[col_map[c] for c in cols_tecnicos],
        color_continuous_scale='RdBu',
        zmin=-1, zmax=1,
        text_auto='.2f',
        title='Heatmap de Correlação Interativo'
    )
    heatmap.update_layout(width=800, height=600, coloraxis_colorbar={'title': 'Correlação'})
    st.plotly_chart(heatmap, use_container_width=True)

    # Seleção das variáveis
    col1, col2 = st.columns(2)
    with col1:
        y_legivel = st.selectbox('Variável Y:', cols_legiveis, index=0)
    with col2:
        x_legivel = st.selectbox('Variável X:', [v for v in cols_legiveis if v != y_legivel], index=1)

    y_var = inv_col_map[y_legivel]
    x_var = inv_col_map[x_legivel]

    # Apenas linha de tendência
    trend_fig = px.scatter(
        df,
        x=x_var, y=y_var,
        trendline='ols',
        opacity=0,
        labels={x_var: x_legivel, y_var: y_legivel},
        title=f'Relação entre {x_legivel} e {y_legivel} (Linha de Tendência)'
    )
    trend_fig.update_traces(marker=dict(opacity=0))
    trend_fig.update_layout(width=800, height=500)
    st.plotly_chart(trend_fig, use_container_width=True)

def plot_top_fatores():
    fatores_df = pd.read_csv('dados/fator_contribuinte.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    
    # Definições das colunas e títulos
    colunas_titulos = [
        ('fator_nome', 'Fator Nome'),
        ('fator_aspecto', 'Fator Aspecto'),
        ('fator_condicionante', 'Fator Condicionante'),
        ('fator_area', 'Fator Área')
    ]
    
    # Subplots 2x2
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[titulo for _, titulo in colunas_titulos],
        vertical_spacing=0.35,  # <-- aumenta o espaço entre as linhas
        horizontal_spacing=0.1
    )

    # Gerar gráficos
    for i, (coluna, titulo) in enumerate(colunas_titulos):
        contagem = fatores_df[coluna].value_counts().head(10)
        row, col = divmod(i, 2)
        fig.add_trace(
            go.Bar(
                x=contagem.index,
                y=contagem.values,
                text=contagem.values,
                textposition='outside',
                name=titulo,
                marker_color=px.colors.qualitative.Plotly[i]
            ),
            row=row + 1,
            col=col + 1
        )
        fig.update_xaxes(tickangle=45, row=row + 1, col=col + 1)

    fig.update_layout(
        height=1000,  # aumenta a altura total
        width=1100,
        title_text="Top 10 Fatores Contribuintes",
        showlegend=False,
        margin=dict(t=80, b=60)  # margens maiores
    )

    st.plotly_chart(fig, use_container_width=True)


def grafico_fatores_condicionantes_por_periodo():
    # Carrega os dados
    fatores_df = pd.read_csv('dados/fator_contribuinte.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')
    ocorrencia_tipo_df = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')

    # Renomeia colunas para merge
    fatores_df = fatores_df.rename(columns={'codigo_ocorrencia3': 'codigo_ocorrencia'})
    ocorrencia_tipo_df = ocorrencia_tipo_df.rename(columns={'codigo_ocorrencia1': 'codigo_ocorrencia'})

    # Merge dos dataframes
    fatores_com_tipo_df = pd.merge(
        fatores_df,
        ocorrencia_tipo_df[['codigo_ocorrencia', 'ocorrencia_tipo']],
        on='codigo_ocorrencia',
        how='left'
    )

    # Substituição para melhor visualização
    fatores_com_tipo_df['ocorrencia_tipo'] = fatores_com_tipo_df['ocorrencia_tipo'].replace(
        'GERENCIAMENTO DE TRÁFEGO AÉREO (ATM) / SERVIÇO DE COMUNICAÇÃO NAVEGAÇÃO, OU VIGILÂNCIA (CNS)',
        'ATM e CNS'
    )

    coluna_fator = 'fator_nome'

    # Cria a tabela cruzada completa
    tabela = pd.crosstab(
        fatores_com_tipo_df['ocorrencia_tipo'],
        fatores_com_tipo_df[coluna_fator]
    )

    # Heatmap completo - formato long para plotly
    tabela_long = tabela.reset_index().melt(id_vars='ocorrencia_tipo', var_name=coluna_fator, value_name='contagem')

    # Plot do heatmap completo
    fig_heatmap = px.density_heatmap(
        tabela_long,
        x=coluna_fator,
        y='ocorrencia_tipo',
        z='contagem',
        color_continuous_scale='YlGnBu',
        labels={'contagem': 'Número de Ocorrências'},
        text_auto=True,
        height=700,
    )
    fig_heatmap.update_layout(
        title=f'Heatmap Completo: {coluna_fator} vs Tipo de Ocorrência',
        xaxis_title=coluna_fator,
        yaxis_title='Tipo de Ocorrência',
        xaxis_tickangle=-45,
        font=dict(size=12),
        margin=dict(t=50, b=150),
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

    # Slider para escolher quantas das maiores correlações mostrar
    max_barras = st.slider('Quantas das maiores correlações mostrar?', min_value=5, max_value=50, value=20)

    # Extraindo as maiores correlações para o gráfico de barras:
    # Consideramos correlações como as células do heatmap com maiores valores (contagem)
    tabela_long_sorted = tabela_long.sort_values('contagem', ascending=False).head(max_barras)

    # Gráfico de barras mostrando as maiores correlações
    fig_barras = px.bar(
        tabela_long_sorted,
        x='contagem',
        y=coluna_fator,
        color='ocorrencia_tipo',
        orientation='h',
        labels={'contagem': 'Número de Ocorrências', coluna_fator: coluna_fator, 'ocorrencia_tipo': 'Tipo de Ocorrência'},
        title=f'Top {max_barras} maiores correlações entre {coluna_fator} e Tipo de Ocorrência',
        height=600
    )
    fig_barras.update_layout(yaxis={'categoryorder':'total ascending'}, margin=dict(t=60))
    st.plotly_chart(fig_barras, use_container_width=True)

def grafico_fator_nome_fator_aspecto():
    # Carrega os dados
    fatores_df = pd.read_csv('dados/fator_contribuinte.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')
    ocorrencia_tipo_df = pd.read_csv('dados/ocorrencia_tipo.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')

    # Renomeia colunas para merge
    fatores_df = fatores_df.rename(columns={'codigo_ocorrencia3': 'codigo_ocorrencia'})
    ocorrencia_tipo_df = ocorrencia_tipo_df.rename(columns={'codigo_ocorrencia1': 'codigo_ocorrencia'})

    # Merge dos dataframes
    fatores_com_tipo_df = pd.merge(
        fatores_df,
        ocorrencia_tipo_df[['codigo_ocorrencia', 'ocorrencia_tipo']],
        on='codigo_ocorrencia',
        how='left'
    )

    # Substitui nome longo por sigla para visualização (se quiser manter, pode remover esta parte)
    fatores_com_tipo_df['ocorrencia_tipo'] = fatores_com_tipo_df['ocorrencia_tipo'].replace(
        'GERENCIAMENTO DE TRÁFEGO AÉREO (ATM) / SERVIÇO DE COMUNICAÇÃO NAVEGAÇÃO, OU VIGILÂNCIA (CNS)',
        'ATM e CNS'
    )

    # Cria tabela cruzada fator_nome vs fator_aspecto
    tabela_fatores = pd.crosstab(
        fatores_com_tipo_df['fator_nome'],
        fatores_com_tipo_df['fator_aspecto']
    )

    # Converte tabela para formato long para plotly
    tabela_long = tabela_fatores.reset_index().melt(id_vars='fator_nome', var_name='fator_aspecto', value_name='contagem')

    # Heatmap completo com plotly
    fig_heatmap = px.density_heatmap(
        tabela_long,
        x='fator_aspecto',
        y='fator_nome',
        z='contagem',
        color_continuous_scale='YlGnBu',
        labels={'contagem': 'Contagem'},
        text_auto=True,
        height=700
    )
    fig_heatmap.update_layout(
        title='Heatmap Completo: Fator Nome vs Fator Aspecto',
        xaxis_title='Fator Aspecto',
        yaxis_title='Fator Nome',
        xaxis_tickangle=-45,
        font=dict(size=12),
        margin=dict(t=50, b=150),
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

    # Slider para escolher quantas das maiores correlações mostrar
    max_barras = st.slider(
        'Quantas das maiores correlações mostrar?',
        min_value=5,
        max_value=50,
        value=20,
        key='slider_fator_nome_aspecto'
    )

    # Seleciona as maiores correlações
    tabela_long_sorted = tabela_long.sort_values('contagem', ascending=False).head(max_barras)

    # Gráfico de barras horizontal para as maiores correlações
    fig_barras = px.bar(
        tabela_long_sorted,
        x='contagem',
        y='fator_nome',
        color='fator_aspecto',
        orientation='h',
        labels={'contagem': 'Contagem', 'fator_nome': 'Fator Nome', 'fator_aspecto': 'Fator Aspecto'},
        title=f'Top {max_barras} maiores correlações entre Fator Nome e Fator Aspecto',
        height=600
    )
    fig_barras.update_layout(yaxis={'categoryorder':'total ascending'}, margin=dict(t=60))
    st.plotly_chart(fig_barras, use_container_width=True)

def grafico_fatores_cond_mais_freq():
    # Carrega os dados
    fatores_df = pd.read_csv('dados/fator_contribuinte.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')

    # Limpeza e contagem
    fatores_df = fatores_df.replace("***", pd.NA)
    fatores_df = fatores_df.dropna(subset=['fator_condicionante'])

    fatores_condicionante_count = fatores_df['fator_condicionante'].value_counts().reset_index()
    fatores_condicionante_count.columns = ['Fator Condicionante', 'Quantidade']

    # Criação do gráfico interativo com Plotly
    fig = px.bar(
        fatores_condicionante_count,
        x='Fator Condicionante',
        y='Quantidade',
        text='Quantidade',
        title='Fatores Condicionantes Mais Frequentes',
        color='Quantidade',
        color_continuous_scale='Blues',
        template='plotly_white'
    )

    # Ajustes estéticos
    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title='Fator Condicionante',
        yaxis_title='Número de Ocorrências',
        xaxis_tickangle=-45,
        height=600,
        margin=dict(t=80, b=80),
        coloraxis_showscale=False
    )

    # Mostra no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_fatores_2019_2020():
    # Carrega os dados
    fatores_df = pd.read_csv('dados/fator_contribuinte.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')
    ocorrencia_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', delimiter=';', on_bad_lines='skip')

    # Renomeia para merge
    fatores_df = fatores_df.rename(columns={'codigo_ocorrencia3': 'codigo_ocorrencia'})

    # Merge
    fatores_com_ocorrencia_df = pd.merge(
        fatores_df,
        ocorrencia_df[['codigo_ocorrencia', 'ocorrencia_dia']],
        on='codigo_ocorrencia',
        how='left'
    )

    # Converte datas
    fatores_com_ocorrencia_df['ocorrencia_dia'] = pd.to_datetime(fatores_com_ocorrencia_df['ocorrencia_dia'], errors='coerce')

    # Filtra por períodos
    fatores_antes_2019 = fatores_com_ocorrencia_df[fatores_com_ocorrencia_df['ocorrencia_dia'].dt.year < 2019]
    fatores_2020_em_diante = fatores_com_ocorrencia_df[fatores_com_ocorrencia_df['ocorrencia_dia'].dt.year >= 2020]

    # Contagens
    cont_pre = fatores_antes_2019['fator_condicionante'].value_counts()
    cont_post = fatores_2020_em_diante['fator_condicionante'].value_counts()

    # Unifica fatores para garantir todos no gráfico
    fatores_unicos = sorted(set(cont_pre.index).union(cont_post.index))

    pre_vals = [cont_pre.get(f, 0) for f in fatores_unicos]
    post_vals = [cont_post.get(f, 0) for f in fatores_unicos]

    # Cria gráfico de barras agrupadas
    fig = go.Figure(data=[
        go.Bar(
            name='Antes de 2019',
            x=fatores_unicos,
            y=pre_vals,
            marker_color='lightgreen',
            text=pre_vals,
            textposition='outside'
        ),
        go.Bar(
            name='2020 em diante',
            x=fatores_unicos,
            y=post_vals,
            marker_color='lightskyblue',
            text=post_vals,
            textposition='outside'
        )
    ])

    # Layout
    fig.update_layout(
        barmode='group',
        title='Comparação dos Fatores Condicionantes Antes de 2019 e a partir de 2020',
        xaxis_title='Fator Condicionante',
        yaxis_title='Número de Ocorrências',
        xaxis_tickangle=-45,
        template='plotly_white',
        height=600,
        margin=dict(t=100, b=150)
    )

    # Exibe no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_ano_aeronaves():
    # Carrega os dados
    ocorrencia_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    aeronave_df = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Substitui "***" por NaN
    ocorrencia_df.replace("***", pd.NA, inplace=True)
    aeronave_df.replace("***", pd.NA, inplace=True)

    # Renomeia coluna para merge
    aeronave_df.rename(columns={'codigo_ocorrencia2': 'codigo_ocorrencia'}, inplace=True)

    # Remove espaços e garante tipo string
    ocorrencia_df['codigo_ocorrencia'] = ocorrencia_df['codigo_ocorrencia'].astype(str).str.strip()
    aeronave_df['codigo_ocorrencia'] = aeronave_df['codigo_ocorrencia'].astype(str).str.strip()

    # Merge
    df = pd.merge(aeronave_df, ocorrencia_df, on='codigo_ocorrencia', how='inner')

    # Remove registros sem data ou ano fabricação
    df = df.dropna(subset=['ocorrencia_dia', 'aeronave_ano_fabricacao'])

    # Converte tipos
    df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'], dayfirst=True, errors='coerce')
    df['ocorrencia_ano'] = df['ocorrencia_dia'].dt.year
    df['aeronave_ano_fabricacao'] = pd.to_numeric(df['aeronave_ano_fabricacao'], errors='coerce')

    # Filtra dados dos períodos
    df_antes_2010 = df[df['ocorrencia_ano'] < 2010]
    df_apos_2020 = df[df['ocorrencia_ano'] > 2020]

    # Cria figura Plotly com dois violinos lado a lado
    fig = go.Figure()

    fig.add_trace(go.Violin(
        y=df_antes_2010['aeronave_ano_fabricacao'],
        name='Incidentes antes de 2010',
        box_visible=True,
        line_color='skyblue',
        fillcolor='lightblue',
        opacity=0.7,
        meanline_visible=True,
        points='all',
        jitter=0.3,
        scalemode='count',
        bandwidth=3
    ))

    fig.add_trace(go.Violin(
        y=df_apos_2020['aeronave_ano_fabricacao'],
        name='Incidentes após 2020',
        box_visible=True,
        line_color='lightgreen',
        fillcolor='lightgreen',
        opacity=0.7,
        meanline_visible=True,
        points='all',
        jitter=0.3,
        scalemode='count',
        bandwidth=3
    ))

    # Atualiza layout
    fig.update_layout(
        title='Distribuição do Ano de Fabricação das Aeronaves Envolvidas em Incidentes (antes de 2010 e depois de 2020)',
        yaxis_title='Ano de Fabricação',
        violingap=0.3,
        violinmode='group',
        yaxis=dict(range=[1930, 2025], dtick=10),
        template='plotly_white',
        height=600,
        margin=dict(t=100, b=100)
    )

    # Exibe no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def grafico_ano_aeronaves_compacto():
    # Carrega os dados
    ocorrencia_df = pd.read_csv('dados/ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
    aeronave_df = pd.read_csv('dados/aeronave.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')

    # Substitui "***" por NaN
    ocorrencia_df.replace("***", pd.NA, inplace=True)
    aeronave_df.replace("***", pd.NA, inplace=True)

    # Renomeia colunas para merge
    aeronave_df.rename(columns={'codigo_ocorrencia2': 'codigo_ocorrencia'}, inplace=True)

    # Garante tipo string e remove espaços
    ocorrencia_df['codigo_ocorrencia'] = ocorrencia_df['codigo_ocorrencia'].astype(str).str.strip()
    aeronave_df['codigo_ocorrencia'] = aeronave_df['codigo_ocorrencia'].astype(str).str.strip()

    # Merge
    df = pd.merge(aeronave_df, ocorrencia_df, on='codigo_ocorrencia', how='inner')

    # Remove linhas sem data ou ano de fabricação
    df = df.dropna(subset=['ocorrencia_dia', 'aeronave_ano_fabricacao'])

    # Converte datas e extrai ano
    df['ocorrencia_dia'] = pd.to_datetime(df['ocorrencia_dia'], dayfirst=True, errors='coerce')
    df['ocorrencia_ano'] = df['ocorrencia_dia'].dt.year
    df['aeronave_ano_fabricacao'] = pd.to_numeric(df['aeronave_ano_fabricacao'], errors='coerce')

    # Filtra os incidentes antes de 2015 e após 2022
    df_antes_2015 = df[df['ocorrencia_ano'] < 2015]
    df_apos_2022 = df[df['ocorrencia_ano'] > 2022]

    # Cria figura Plotly com dois gráficos de violino lado a lado
    fig = go.Figure()

    fig.add_trace(go.Violin(
        y=df_antes_2015['aeronave_ano_fabricacao'],
        name='Incidentes antes de 2015',
        box_visible=True,
        line_color='skyblue',
        fillcolor='lightblue',
        opacity=0.7,
        meanline_visible=True,
        points='all',
        jitter=0.3,
        scalemode='count',
        bandwidth=3
    ))

    fig.add_trace(go.Violin(
        y=df_apos_2022['aeronave_ano_fabricacao'],
        name='Incidentes após 2022',
        box_visible=True,
        line_color='lightgreen',
        fillcolor='lightgreen',
        opacity=0.7,
        meanline_visible=True,
        points='all',
        jitter=0.3,
        scalemode='count',
        bandwidth=3
    ))

    # Atualiza layout
    fig.update_layout(
        title='Distribuição do Ano de Fabricação das Aeronaves Envolvidas em Incidentes (antes de 2015 e depois de 2022)',
        yaxis_title='Ano de Fabricação',
        violingap=0.3,
        violinmode='group',
        yaxis=dict(range=[1930, 2025], dtick=10),
        template='plotly_white',
        height=600,
        margin=dict(t=100, b=100)
    )

    # Exibe no Streamlit
    st.plotly_chart(fig, use_container_width=True)
