import streamlit as st
from cabecalho import cria_cabecalho

def pagina_inicial():
    cria_cabecalho()
    
    st.image("images/aviao_pag_ini.jpg", caption="\"A vitória pertence aquele que acredita nela, e aquele que acredita nela por mais tempo.\" ~Pearl Harbor" ,use_container_width=True)

    st.markdown('<a name="introducao"></a>', unsafe_allow_html=True)
    st.markdown("## Introdução")
    st.markdown(
        """ 
        Com o passar dos anos, os aviões se firmaram como um meio de transporte seguro. Porém, com o aumento da frequência de 
        incidentes aeronáuticos nos últimos anos, a confiança depositada na segurança dos aviões tem sido questionada.
        O objetivo deste estudo é analisar os dados históricos de ocorrências aeronáuticas para identificar padrões e tendências 
        que possam indicar falhas nos sistemas de manutenção e prevenção. Para isso, utilizou-se algumas medidas numéricas 
        descritivas, como: média aritmética, mediana e desvio-padrão.
        A linguagem de programação Python foi utilizada para construir representações gráficas do comportamento dos dados 
        obtidos a partir da base de dados de ocorrências aeronáuticas, gerenciada pelo Centro de Investigação e Prevenção 
        de Acidentes Aeronáuticos (CENIPA).

        A análise revelou o impacto de fatores causadores relacionados à qualidade das manutenções, e de como elas 
        "se comportaram" frente a acontecimentos globais impactantes que aconteceram nos últimos anos, como é o caso da pandemia 
        global de COVID-19 e a crise dos semicondutores.
        Com isso, mostrou-se a necessidade de desenvolvimento de sistemas melhores de análise de necessidade de manutenção e 
        monitoramento do funcionamento de aeronaves. Além disso, também foi identificado um padrão de incidentes nos últimos 
        anos relacionado ao aumento da demanda de voos, quando comparado com anos anteriores.
        """
    )
    st.markdown('<a name="contexto"></a>', unsafe_allow_html=True)
    st.markdown("## Contexto")
    st.markdown(
        """
        Dentro da base de dados do CENIPA, foram coletadas tabelas em formato “.csv”, com as ocorrências, tipo das ocorrências, 
        aeronaves envolvidas, fatores contribuintes e recomendações, para cada acidente individualmente.

        O presente estudo é norteado pelas seguintes perguntas:

        - (i) Dá para prever um acidente aéreo?  
        - (ii) Quais são as similaridades que existem entre acidentes “parecidos”?  
        - (iii) Há um padrão nos fatores causadores de acidentes aéreos?

        Dado o contexto acima, neste estudo, tem-se como **objetivo geral** verificar, por meio da análise de acontecimentos 
        prévios, como essas situações podem ser evitadas e como os sistemas de prevenção de acidentes podem ser aperfeiçoados, 
        servindo assim como uma ferramenta para prevenção de futuros acidentes (provendo uma possibilidade de comparativo com 
        situações prévias em acontecimentos futuros).
        """
    )