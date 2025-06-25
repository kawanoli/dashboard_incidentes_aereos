# Análise de Incidentes Aéreos no Brasil

<p align="center">
  Veja o estudo online no link abaixo:
</p>
<p align="center">
  <a href="https://estudo-incidentes-aereos.streamlit.app">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit App">
  </a>
</p>

---

<p align="center">
    <img src="images/aviao2.jpg" alt="aviao_cabecalho">
</p>


O estudo "Estudo de falhas em aeronaves no espaço brasileiro" analisa dados históricos de ocorrências aeronáuticas no Brasil de 2007 a 2024, buscando padrões e tendências em falhas de manutenção e prevenção. Utilizando a linguagem Python e dados do CENIPA, a pesquisa investiga se acidentes aéreos podem ser previstos, suas similaridades e a existência de padrões nos fatores causadores. Conclui-se que o aumento de incidentes está ligado à sobrecarga da infraestrutura aeroportuária pós-pandemia, à qualidade da manutenção, à formação de mão de obra qualificada e à complexidade das aeronaves modernas, destacando que fatores humanos e operacionais exercem maior impacto do que apenas falhas materiais, sendo um problema multifacetado que exige um ciclo de cuidado mais rigoroso para ser contornado.

Este repositório contém um estudo aprofundado sobre incidentes aeronáuticos no espaço aéreo brasileiro, com o objetivo de identificar padrões, tendências e fatores contribuintes para o aumento de ocorrências nos últimos anos.

## Sumário
- [Estudo de Falhas em Aeronaves no Espaço Aéreo Brasileiro](#estudo-de-falhas-em-aeronaves-no-espaço-aéreo-brasileiro)
- [Sumário](#sumário)
- [Objetivo do Estudo](#objetivo-do-estudo)
- [Perguntas Norteadoras](#perguntas-norteadoras)
- [Dados Utilizados](#dados-utilizados)
- [Metodologia e Ferramentas](#metodologia-e-ferramentas)
- [Resultados e Conclusões Principais](#resultados-e-conclusões-principais)
- [Observações Adicionais](#observações-adicionais)


## Objetivo do Estudo
O principal objetivo deste estudo é **analisar dados históricos de ocorrências aeronáuticas para identificar padrões e tendências** que possam indicar falhas nos sistemas de manutenção e prevenção. A pesquisa visa verificar como situações prévias podem ser evitadas e como os sistemas de prevenção de acidentes podem ser aprimorados, servindo como uma ferramenta comparativa para eventos futuros.

## Perguntas Norteadoras
O estudo é guiado pelas seguintes perguntas:
*   É possível prever um acidente aéreo?
*   Quais são as similaridades entre acidentes "parecidos"?
*   Existe um padrão nos fatores causadores de acidentes aéreos?

## Dados Utilizados
Os dados foram coletados da base de dados de ocorrências aeronáuticas, **gerenciada pelo Centro de Investigação e Prevenção de Acidentes Aeronáuticos (CENIPA)**.

*   **Período Abrangido:** Ocorrências notificadas ao CENIPA no período de **2007 a 2023**, com alguns dados já referentes a 2024 e poucos a 2025.
*   **Área de Estudo:** Todo o território aéreo brasileiro e seus limites aeroespaciais, considerando fatores geográficos e climáticos que podem influenciar as ocorrências.
*   **Estrutura dos Dados:** As informações estão organizadas em arquivos `.csv` e incluem:
    *   Ocorrências.
    *   Tipos de ocorrências (com taxonomia padronizada pela ICAO).
    *   Aeronaves envolvidas (incluindo dados como fabricante, tipo de veículo, quantidade de motores e ano de fabricação).
    *   Fatores contribuintes.
    *   Recomendações.
    *   Número de fatalidades, local, data e horário dos eventos.
*   **Privacidade:** A privacidade de pessoas físicas e jurídicas envolvidas é resguardada conforme a Lei de Acesso à Informação (Lei nº 12.527/2011).

## Metodologia e Ferramentas
Este estudo utilizou uma abordagem de análise de dados exploratória e descritiva:

*   **Linguagem de Programação:** **Python**.
*   **Bibliotecas Utilizadas:**
    *   `pandas`: Para manipulação e análise de dados.
    *   `Plotly`, `matplotlib` e `seaborn`: Para a construção de representações gráficas e visualização de dados.
    *   `numpy`: Para operações numéricas.
    *   `chardet`: Para detecção automática da codificação de texto dos arquivos CSV.
*   **Ambiente de Desenvolvimento:** Inicialmente no Jupyter Notebook (compatível com Google Colab), e Streamlit.
*   **Medidas Descritivas:** Média aritmética, mediana e desvio-padrão foram utilizadas para a análise numérica.
*   **Processamento de Dados:**
    *   Leitura de arquivos `.csv` com codificação `UTF-8-SIG`, pulando linhas problemáticas (`on_bad_lines='skip'`) e delimitador `;`.
    *   Conversão de colunas de data para o tipo `datetime`.
    *   Tratamento de valores ausentes (ex: substituição de "***" por `NaN` e remoção de linhas com `NaN` em colunas cruciais).
    *   Utilização da **taxonomia de tipos de incidentes da ICAO** para padronização e evitar duplicações.
    *   Criação de gráficos de barras, gráficos de linha, box-plots e **heatmaps** para visualizar a distribuição e correlação dos dados.

## Resultados e Conclusões Principais
O estudo revelou insights importantes sobre os incidentes aeronáuticos no Brasil:

*   **Aumento de Ocorrências:** Observou-se um **aumento repentino no número de ocorrências a partir da segunda metade de 2023**, com 2023 e 2024 apresentando valores consideravelmente mais altos que anos anteriores, inclusive pós-pandemia.
*   **Impacto de Fatores Globais:** A análise mostrou o impacto de fatores relacionados à **qualidade das manutenções** frente a acontecimentos globais, como a pandemia de COVID-19 e a crise dos semicondutores.
*   **Necessidade de Melhoria:** Há uma clara necessidade de desenvolver **melhores sistemas de análise de necessidade de manutenção e monitoramento** do funcionamento de aeronaves.
*   **Tipos de Incidentes:**
    *   Excluindo colisões com aves, os tipos de incidentes mais frequentes estão relacionados a **falhas nos sistemas da aeronave**.
    *   A **falha de componente do sistema - não propulsor (SCF-NP)** é o tipo de incidente mais comum, tanto na análise geral quanto em 2024, indicando que sistemas embarcados menores podem estar influenciando o aumento de ocorrências, possivelmente devido a negligência em inspeções.
*   **Aeronaves Envolvidas:**
    *   **Aviões** representam a maior fatia de incidentes, o que é esperado devido à maior demanda por esse tipo de veículo [65].
    *   A **Cessna Aircraft** é a fabricante com mais envolvimento em incidentes, provavelmente devido à sua ampla fatia de mercado e diversidade de modelos, e não necessariamente por problemas de qualidade.
    *   Aeronaves **monomotoras e bimotoras** são as mais presentes em incidentes, refletindo a tendência global por designs mais econômicos e as legislações de poluentes.
*   **Regionalidade:** A frequência de ocorrências em diferentes estados do Brasil parece ser **diretamente proporcional à demanda de voos e aeroportos** em cada local, e não primariamente a fatores geomorfológicos.
*   **Ano de Fabricação da Aeronave:** Uma grande quantidade de aeronaves fabricadas na década de 2010 está envolvida em incidentes. Isso se relaciona com a **demanda de aeronaves, sua vida útil e as práticas de manutenção atuais**.
*   **Fatores Contribuintes (Humanos vs. Materiais):**
    *   **Fatores ligados à humanidade operam um impacto maior** do que fatores materiais.
    *   Problemas de **infraestrutura aeroportuária**, falta de pessoal qualificado e escalas exaustivas são citados.
    *   **"Recursos Humanos"** foi identificado como o fator com maior peso, estando interligado com todos os outros.
    *   **Problemas gerenciais e de operação humana** são as áreas com maior "calor" nos heatmaps de fatores.
    *   A **sobrecarga das operações** e a pressão para suprir a demanda estão afetando diretamente o desempenho humano na operação e manutenção, incluindo a possível reintrodução de aeronaves que ficaram paradas na pandemia sem inspeções minuciosas.
    *   A **formação de pilotos** é um fator condicionante relevante. O alto custo da formação, o déficit pré-pandemia e a intensificação da escassez pós-pandemia (devido a aposentadorias, migração e custos elevados de horas de voo) afetam a qualificação.
    *   Aeronaves fabricadas nos **anos 2000 e 2010**, com tecnologias avançadas como *fly-by-wire*, exigem manutenção e treinamento mais sofisticados. **Problemas não vêm do *fly-by-wire* puro, mas de sua integração com softwares (ex: MCAS), automação de cockpit e interfaces homem-máquina mal projetadas**, além da confiança excessiva dos pilotos na automação.
    *   Há uma **carência de mecânicos e engenheiros especializados** em aeronaves de novas gerações no Brasil, e a terceirização da manutenção pode comprometer a autossuficiência técnica.
    *   A **menor exposição de pilotos a situações reais de manutenção e avarias** pós-pandemia, devido a cortes e redução de contato prático, levou a uma formação mais frágil e ao enfraquecimento da cultura de segurança operacional.
*   **Conclusão Geral:** O aumento dos incidentes não se deve a um único fator, mas a um **contexto geral de sobrecarga da infraestrutura, qualidade da manutenção e formação de mão de obra que não acompanharam o aumento da demanda e as mudanças tecnológicas pós-pandemia**.

## Observações Adicionais
*   O estudo detalha o processo de carregamento e limpeza dos dados, incluindo a detecção de codificação e tratamento de valores ruidosos.
*   Os gráficos e tabelas são elaborados para realizar uma análise de correlação entre os diferentes aspectos dos incidentes.
