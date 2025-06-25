import streamlit as st
from cabecalho import cria_cabecalho

def material_metodos():
    cria_cabecalho()

    st.markdown('<a name="matmet"></a>', unsafe_allow_html=True)
    st.markdown("## Material e Métodos")
    st.markdown(
        """
        A área de estudo escolhida contempla todo o território aéreo brasileiro e seus limites aeroespaciais. 
        O território brasileiro, devido ao seu tamanho, possui vários fatores geográficos diferentes nas diversas 
        regiões do país, os quais podem influenciar diretamente as ocorrências no espaço aéreo local. Trabalhando 
        com dados do espaço aéreo brasileiro como um todo, é possível obter mais variáveis para estudo, considerando a 
        geomorfologia do país e fatores adicionais, como o clima das diferentes regiões.
        
        O conjunto de dados utilizado na pesquisa é composto por informações coletadas na base de dados de ocorrências 
        aeronáuticas, gerenciada pelo Centro de Investigação e Prevenção de Acidentes Aeronáuticos (CENIPA). Esta base 
        inclui as ocorrências aeronáuticas notificadas ao CENIPA no período de 2007 a 2023.
        
        Os dados de acidentes utilizados na pesquisa estão organizados em arquivos `.csv`, distribuídos em três tabelas 
        distintas: **ocorrência**, **tipo de ocorrência** e **aeronave**. A partir disso, foram elaborados gráficos e 
        tabelas separadas para cada item analisado no presente estudo, com o objetivo de realizar uma análise de correlação.
        
        Além disso, para calcular corretamente a quantidade de incidentes — evitando duplicações de registros únicos 
        com grafias diferentes — foi adotada a **taxonomia dos tipos de incidentes aéreos padronizada pela Organização 
        da Aviação Civil Internacional (ICAO)**.
        """
    )
    st.markdown('<a name="bibliotecas"></a>', unsafe_allow_html=True)
    st.markdown("## Instalação de Bibliotecas necessárias")
    st.markdown(
        """
        Para executar nossos scripts que geram os gráficos, precisamos realizar a instalação das bibliotecas 
        necessárias para execução dos nossos códigos deste documento.
        
        Utilizando o pip, faremos a instalação das dependências que precisamos. O pip é o gerenciador de 
        pacotes do Python. Ele permite instalar, atualizar e remover bibliotecas e módulos de forma simples.
        ```python
        #No terminal do computador/ambiente, executamos o seguinte comando:
        pip install pandas matplotlib seaborn numpy chardet plotly
        ```
        """
        )
    st.markdown('<a name="csvs"></a>', unsafe_allow_html=True)
    st.markdown("## Baixando os CSVs")
    st.markdown(
        """
        Utilizando o Google Drive para baixar os CSVs, iremos baixar os CSVs necessários para a execução da EDA.
        
        Infelizmente, os testes de biblioteca para baixar o arquivo .CSV direto do drive não foram tão produtivos, 
        visto que o problema estava na forma com que o Google Drive fornecia o arquivo por meio de link; os mesmos 
        vinham com a codificação errada (ascii, como se fosse HTML). Por conta disso, infelizmente teremos que 
        baixar manualmente do Drive.

        https://drive.google.com/drive/folders/1Dot5iuuPM2AfAiZwZNh2iR3R5z8AC9DX?usp=sharing

        """
    )
    st.markdown('<a name="processamento"></a>', unsafe_allow_html=True)
    st.markdown("## Processamento Inicial do CSV")
    st.markdown(
        """
        A biblioteca chardet (Character Detection) é usada para detectar automaticamente a codificação de textos 
        (como UTF-8, ISO-8859-1, etc.). Ela é útil quando você não sabe em qual codificação um arquivo ou conteúdo 
        de texto está, e precisa garantir que ele seja lido corretamente. O parâmetro 'rb' significa "ler o arquivo 
        em modo binário". Isso faz com que o conteúdo seja lido como bytes (e não como texto), que é exatamente o 
        que desejamos para saber o encoding.
        ```python
        # Lê uma fração do arquivo para detectar o encoding
        with open('ocorrencia.csv', 'rb') as f:
            result = chardet.detect(f.read(10000))  # Read the first 10,000 bytes

        print(result)
        ```
        Saber essa codificação é importante, pois pode afetar na forma com que nossos dados são lidos, interpretados 
        e mostrados, podendo afetar diretamente no desempenho da nossa análise. 
        Sendo assim, nossas linhas de leitura dos CSVs terão além do CSV que carregaremos, os parâmetros de encoding, 
        o parâmetro on_bad_lines para saber o que fazer caso encontre um dado ruidoso (nesse caso, pulá-lo), e o 
        delimitador para pontuar onde começa a próxima coluna de dados da linha que estamos processando os dados 
        (por serem datasets do tipo Comma Separated Values, o delimitador é o ";").
        ```python
        df = pd.read_csv('ocorrencia.csv', encoding='UTF-8-SIG', on_bad_lines='skip', delimiter=';')
        ```
        """
    )
    st.markdown('<a name="areadeestudo"></a>', unsafe_allow_html=True)
    st.markdown("## Área de Estudo")
    st.markdown(
        """
        A área de estudo escolhida contempla todo o território aéreo brasileiro e seus limites aeroespaciais. O território 
        brasileiro, devido ao seu tamanho, possui vários fatores geográficos diferentes, nas distintas regiões do país, 
        os quais podem influenciar diretamente as ocorrências no espaço aéreo local.
        
        O conjunto de dados utilizado na pesquisa é composto por informações coletadas na **base de dados de ocorrências 
        aeronáuticas**, gerenciada pelo **Centro de Investigação e Prevenção de Acidentes Aeronáuticos (CENIPA)**. 
        Esta base contém registros de ocorrências notificadas ao CENIPA entre os anos de **2007 a 2024** (e alguns poucos 
        dados já referentes a 2025), todos ocorridos em solo brasileiro.
        Dentre as informações disponíveis estão:
        - Dados sobre as **aeronaves envolvidas**;
        - Número de **fatalidades**;
        - **Local**, **data** e **horário** dos eventos;
        - Informações **taxonômicas** típicas das investigações de acidentes (AIG).
        
        A privacidade de pessoas físicas e jurídicas envolvidas é resguardada conforme previsto pela 
        **Lei de Acesso à Informação (Lei nº 12.527, de 18 de novembro de 2011)**.
        Essa base de dados é composta por informações preliminares provenientes do formulário **CENIPA-05** (Ficha de 
        Notificação de Ocorrências Aeronáuticas) e é consolidada a partir dos relatórios de investigações publicados. 
        Outra forma de visualização desses dados é pelo **painel SIPAER**, disponível na página do CENIPA.
        
        Embora o banco de dados não tenha apresentado falhas técnicas, ele continha **lacunas de descrição**. Os dados 
        que não podiam ser elencados nas categorias específicas de cada gráfico foram:
        - Removidos;
        - Mantidos sob as categorias **"outros"** ou **"***"**, quando ainda poderiam apresentar alguma influência nos 
        resultados, mesmo sem descrição completa.
        ---
        O presente estudo é norteado pelas seguintes perguntas:
        1. **Dá para prever um acidente aéreo?**  
        2. **Quais são as similaridades que existem entre acidentes "parecidos"?**  
        3. **Há um padrão nos fatores causadores de acidentes aéreos?**
        """
    )
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/cessna_172.jpg", width=500, caption="Cessna 172")
