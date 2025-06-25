import streamlit as st
from paginainicial import pagina_inicial
from matmet import material_metodos
from estudo import resultado_estudos
from sobre import sobre_mim
from componentes import sidebar_style

def menu_lateral():
    # Menu lateral
    st.sidebar.image("images/dca.png", caption="Departamento de Engenharia da Computação e Automação", use_column_width=True)
    #st.sidebar.markdown(sidebar_logo(), unsafe_allow_html=True)
    st.sidebar.title("Menu")
    opcao = st.sidebar.selectbox("Selecione a página a ser vista", ["Página Inicial", "Material e Métodos", "Estudo", "Sobre o Autor"])

    if opcao == "Página Inicial":
        sidebar_style([
        ("Introdução", "introducao"),
        ("Contexto", "contexto"),
        ])
        pagina_inicial()

    elif opcao == "Material e Métodos":
        sidebar_style([
        ("Material e Métodos", "matmet"),
        ("Instalação de Bibliotecas necessárias", "bibliotecas"),
        ("Baixando os CSVs", "csvs"),
        ("Processamento Inicial do CSV", "processamento"),
        ("Área de Estudo", "areadeestudo"),
        ])
        material_metodos()

    elif opcao == "Estudo":
        sidebar_style([
        ("Da Influência Dos Anos Em Incidentes","influanos"),
        ("Ocorrências Mensais por Ano","ocomeses"),
        ("Distribuição das Ocorrências Mensais ao Longo dos Anos","distmesano"),
        ("Tipos de Incidentes registrados na base de dados do CENIPAs","incidentescenipa"),
        ("Top 10 Tipos de Ocorrências Mais Frequentes e Menos Frequentes","top10ocorrencias"),
        ("Distribuição dos Tipos de Incidentes (ICAO)","incidentesicao"),
        ("Sobre as Aeronaves Envolvidas","sobreaeronaves"),
        ("Sobre a Regionalidade dos incidentes","sobreregionalidade"),
        ("Do Estado das Aeronaves","estadoaeronaves"),
        ("Heatmap de Correlações","heatmapcorrela"),
        ("Dos fatores humanos / de engenharia","fatoreshumeng"),
        ("Heatmap fator_nome vs Tipo de Ocorrência","heatmapnomevsocorr"),
        ("Heatmap Fator Nome vs Fator Aspecto","heatmapnomevsaspec"),
        ("Dos fatores condicionantes","fatorescond"),
        ("Da idade das aeronaves","idadeaero"),
        ("Desafios da Manutenção de Aeronaves Modernas (década de 2010) no Brasil","desafiosmanut"),
        ("Conclusões da análise","conclusoes"),
        ])
        resultado_estudos()

    elif opcao == "Sobre o Autor":
        sobre_mim()

