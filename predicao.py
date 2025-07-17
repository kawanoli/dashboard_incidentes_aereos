import streamlit as st
from PIL import Image
from cabecalho import cria_cabecalho

def tela_predicao():
    cria_cabecalho()

    st.markdown('<a name="predict"></a>', unsafe_allow_html=True)
    st.markdown("## Predição com Aprendizado de Máquina")
    st.markdown(
        """
        Antes de avançarmos com as análises técnicas e estatísticas, é importante retomarmos a pergunta central que orienta todo o nosso estudo: “É possível prever acidentes aéreos?” Essa questão é, por si só, complexa e desafiadora. Envolve não apenas o tratamento quantitativo de dados históricos, mas também a consideração de múltiplos fatores qualitativos, circunstanciais e até mesmo aleatórios, que muitas vezes estão fora do alcance dos modelos tradicionais de previsão.

Nosso estudo parte da premissa de que, embora acidentes aéreos sejam eventos raros (e justamente por isso difíceis de prever com alta precisão), há, sim, sinais e padrões que podem ser extraídos de bases históricas para auxiliar na identificação de riscos. A proposta, portanto, não é afirmar com certeza absoluta quando e onde um acidente ocorrerá, mas sim avaliar a probabilidade de ocorrência a partir de variáveis observáveis e, assim, contribuir para estratégias de prevenção e mitigação de riscos.

Tendo feito as reflexões iniciais no escopo do nosso estudo (que envolveram desde a revisão teórica sobre a segurança da aviação até a identificação de abordagens estatísticas e computacionais viáveis) agora partimos para uma etapa mais prática e objetiva: o tratamento da nossa base de dados.
        """
    )

    st.markdown('<a name="dataprep"></a>', unsafe_allow_html=True)
    st.markdown("## Preparação dos Dados")
    st.markdown(
        """
        Neste ponto do projeto, o foco se volta para as colunas disponíveis no nosso conjunto de dados. É aqui que começamos a "sentar e trabalhar" de fato com as informações. Essa etapa é crucial porque a qualidade e a estruturação dos dados impactam diretamente na capacidade preditiva dos modelos que poderemos construir.

O primeiro passo consiste em compreender profundamente cada coluna: o que ela representa, qual sua importância potencial na análise, e se há necessidade de transformações, correções ou enriquecimentos. Não se trata apenas de uma tarefa mecânica de limpeza de dados, mas sim de uma interpretação cuidadosa do contexto por trás de cada variável.

Vamos então, passar essas variáveis e dados para o nosso modelo, de forma organizada e bem estruturada.
        """
    )

    st.markdown('<a name="analisemodpred"></a>', unsafe_allow_html=True)
    st.markdown("## Analisando os Modelos de Predição")
    st.markdown(
        """
        Escolher o modelo de machine learning mais adequado para um determinado problema é uma das etapas mais desafiadoras em um processo de modelagem preditiva. Isso acontece porque não existe um algoritmo universalmente superior para todas as situações, pois o desempenho de um modelo depende diretamente das características do conjunto de dados, da natureza do problema, da forma como as variáveis estão estruturadas e da presença (ou não) de padrões subjacentes que os algoritmos possam aprender.

Dessa forma, tentar "adivinhar" de antemão qual modelo trará os melhores resultados seria não apenas ineficiente, mas também arriscado, pois estaríamos nos baseando em suposições ao invés de evidências concretas. Assim, optamos por uma abordagem mais sistemática e empírica: em vez de selecionar arbitrariamente um ou dois algoritmos para começar, decidimos realizar uma avaliação inicial utilizando a biblioteca LazyPredict, que nos permite testar, de maneira rápida e padronizada, o desempenho de diversos modelos supervisionados com configurações básicas.
        """
    )

    st.markdown('<a name="lazypred"></a>', unsafe_allow_html=True)
    st.markdown("## Por que usar o LazyPredict?")
    st.markdown(
        """
        A biblioteca LazyPredict tem como principal objetivo facilitar a experimentação com múltiplos algoritmos de machine learning com um esforço mínimo de codificação. Ela oferece uma maneira automatizada de treinar e avaliar diversos modelos padrão (tanto de regressão quanto de classificação) utilizando os parâmetros default de cada algoritmo. Essa ferramenta é particularmente útil em estágios iniciais de projetos, quando o foco está em entender quais algoritmos se adaptam melhor ao comportamento dos dados, antes de investir tempo em ajustes finos (tuning de hiperparâmetros) ou construção de pipelines mais sofisticados.

Ao rodar a análise com o LazyPredict, conseguimos gerar um panorama comparativo que inclui métricas de desempenho para cada modelo testado, como acurácia, precisão, recall, F1-score e tempo de execução. Com base nesses resultados, podemos identificar quais modelos demonstram maior potencial para o nosso caso específico e, a partir disso, decidir quais merecem um estudo mais aprofundado.

Nosso objetivo com o uso do LazyPredict é duplo:

- Explorar o comportamento de diferentes algoritmos frente aos nossos dados: Isso inclui observar como cada modelo lida com o equilíbrio (ou desequilíbrio) das classes, como reage à dimensionalidade do conjunto de variáveis e como se comporta em termos de generalização nos dados de teste.

- Obter uma base comparativa inicial de desempenho: A partir das métricas fornecidas, poderemos eleger os modelos mais promissores para fases posteriores do projeto.

Importante ressaltar que, neste momento, os modelos estão sendo avaliados com parâmetros padrão, o que significa que os resultados ainda não refletem o potencial máximo de cada algoritmo. No entanto, essa abordagem preliminar já é suficiente para termos uma visão clara de quais técnicas são, em princípio, mais compatíveis com a estrutura e os padrões do nosso conjunto de dados.
        """
    )

    st.markdown('<a name="graflazy"></a>', unsafe_allow_html=True)
    st.markdown("## Execução do LazyClassifier")
    st.markdown(
        """
        Antes de prosseguirmos com os testes de modelos preditivos, é fundamental delimitarmos com clareza o escopo do nosso problema de classificação. Afinal, qualquer tentativa de previsão precisa partir de uma definição explícita do que se deseja prever. No nosso caso, o objetivo não é simplesmente detectar qualquer tipo de ocorrência aérea, mas sim distinguir especificamente três categorias críticas: ACIDENTE, INCIDENTE GRAVE e INCIDENTE.

Essas três classificações representam, de diferentes formas, eventos relevantes do ponto de vista da segurança operacional. Embora existam outras classificações ou registros administrativos na base de dados (como "ocorrência sem relevância", "não concluído", entre outros), elas não agregam valor ao nosso objetivo central. Ao incluí-las, correríamos o risco de diluir a capacidade preditiva do modelo, pois estaríamos lidando com categorias que não refletem situações de risco real ou imediato à segurança de voo.

Por isso, optamos por filtrar apenas os registros cujas ocorrências foram classificadas como ACIDENTE, INCIDENTE GRAVE ou INCIDENTE. Essa decisão visa garantir que o modelo foque em prever eventos que, de fato, possuem relevância operacional e cujos padrões podem contribuir para estratégias de mitigação de riscos. Além disso, ao restringirmos o escopo, evitamos um desequilíbrio excessivo entre as classes e aumentamos a consistência do conjunto de dados usado para treinamento.

Com o conjunto de dados devidamente filtrado e ajustado ao nosso objetivo, avançamos para a etapa de avaliação inicial dos algoritmos de classificação. Para isso, utilizamos novamente a biblioteca LazyPredict, desta vez com o seu componente específico para tarefas classificatórias: o LazyClassifier.

O LazyClassifier segue a mesma lógica do LazyPredict usado anteriormente, mas agora voltado para problemas de classificação supervisionada. Ele permite aplicar e comparar, de forma rápida e automatizada, uma variedade de algoritmos clássicos (como Random Forest, Decision Tree, K-Nearest Neighbors, Logistic Regression, Support Vector Machine, entre outros) utilizando configurações padrão ou definidas previamente.

O grande diferencial dessa abordagem é que conseguimos realizar uma triagem eficiente de múltiplos modelos sem a necessidade de configurar manualmente cada pipeline. Isso não só economiza tempo, como também oferece uma visão panorâmica do desempenho de cada algoritmo sob as mesmas condições de entrada.

Utilizamos o LazyClassifier com os parâmetros definidos de acordo com as necessidades do nosso problema e as características da base de dados após o pré-processamento. O modelo foi treinado com os dados classificados em ACIDENTE, INCIDENTE GRAVE e INCIDENTE, e avaliado com base em métricas como acurácia, precisão, recall, F1-score, além do tempo de treinamento e tempo de predição. Essas métricas são fundamentais para entendermos não apenas se o modelo é eficaz em classificar corretamente as ocorrências, mas também se é eficiente do ponto de vista computacional.

Os resultados da execução do LazyClassifier são apresentados logo abaixo. A tabela gerada mostra, em ordem decrescente de desempenho, os modelos testados e suas respectivas métricas. A partir dessa análise inicial, seremos capazes de selecionar os algoritmos com melhor performance para fases posteriores do projeto, nas quais aplicaremos ajustes finos, técnicas de validação cruzada e, se necessário, balanceamento das classes.
        """
    )
    caminho_imagem = 'images/resultados_modelos.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_container_width=True)

    st.markdown('<a name="randomfor"></a>', unsafe_allow_html=True)
    st.markdown("## Destrinchando o Random Forest")
    st.markdown(
        """
        Após a execução do LazyClassifier e a consequente comparação de diversos algoritmos de classificação, observamos que o modelo Random Forest apresentou o melhor desempenho em relação às principais métricas avaliadas. Esse resultado nos motivou a investigar mais a fundo o comportamento desse algoritmo dentro do nosso conjunto de dados, com o objetivo de entender não apenas o que ele entrega em termos de performance, mas também por que ele se destaca nesse cenário específico.

A escolha por focar no Random Forest neste ponto do estudo se justifica por diversos motivos. Em primeiro lugar, ele se mostrou o modelo mais robusto na classificação entre as categorias ACIDENTE, INCIDENTE GRAVE e INCIDENTE, superando os demais em métricas como acurácia, F1-score e recall, sem apresentar um custo computacional excessivo. Além disso, o Random Forest é amplamente reconhecido na literatura por sua capacidade de lidar bem com dados complexos, ruídos e variáveis correlacionadas, o que é especialmente relevante no contexto de segurança operacional, onde os dados frequentemente apresentam múltiplos fatores inter-relacionados.
        """
    )
    
    st.markdown('<a name="treinrandom"></a>', unsafe_allow_html=True)
    st.markdown("## Treinamento Individual e Avaliação de Métricas")
    st.markdown(
        """
        Com o Random Forest treinado de forma dedicada e isolada, realizamos a avaliação do seu desempenho com mais profundidade. As métricas analisadas nos oferecem um panorama mais detalhado da sua eficácia, tanto em termos gerais quanto em relação ao comportamento por classe (através da matriz de confusão e métricas por classe). As principais métricas obtidas foram:

- Acurácia: Representa a proporção de classificações corretas em relação ao total de casos. Embora útil, pode ser enganosa em cenários com classes desbalanceadas.

- Precisão: Mede a proporção de verdadeiros positivos entre todos os casos classificados como positivos, sendo essencial para avaliar o risco de falsos alarmes.

- Recall (Sensibilidade): Avalia a proporção de acertos em relação ao total de ocorrências reais daquela classe — importante para garantir que eventos relevantes não passem despercebidos.

- F1-score: Combinação harmônica entre precisão e recall, especialmente útil quando há desequilíbrio entre as classes e precisamos ponderar ambos os aspectos.
        """
    )
    caminho_imagem = 'images/classification_report_rf.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_container_width=True)
    st.markdown(
        """
        Além dessas métricas, a visualização da matriz de confusão nos ajudará a entender onde o modelo erra mais, descobrindo onde ele se confunde (por exemplo, incidentes com acidentes) ou se é conservador demais e classifica a maioria dos eventos como menos graves.
        """
    )
    caminho_imagem = 'images/matriz_confusao_rf.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_container_width=True)

    st.markdown('<a name="matconfnorm"></a>', unsafe_allow_html=True)
    st.markdown("## Obtendo Matriz de Confusão Normalizada")
    st.markdown(
        """
        Após realizarmos o treinamento do modelo Random Forest de forma dedicada e avaliarmos suas métricas globais de desempenho, avançamos agora para uma representação visual e mais interpretável dos resultados: a matriz de confusão normalizada.

O uso da matriz de confusão é uma prática fundamental em problemas de classificação, especialmente quando o objetivo não é apenas saber quantas vezes o modelo acertou, mas também onde ele errou. Isso se torna ainda mais relevante no nosso estudo, em que estamos lidando com três classes distintas (ACIDENTE, INCIDENTE GRAVE e INCIDENTE), cada uma com seu próprio peso e impacto em termos de segurança aérea.

No entanto, uma matriz de confusão em valores absolutos pode, por vezes, dificultar a leitura e interpretação, sobretudo quando há diferença significativa na quantidade de registros entre as classes. Para tornar essa visualização mais acessível e comparável, optamos por utilizar a versão normalizada da matriz de confusão.

A matriz de confusão normalizada mostra, em termos percentuais, a distribuição dos acertos e erros do modelo para cada classe. Em vez de apresentar os números absolutos de previsões corretas e incorretas, ela expressa essas quantidades como proporções dentro de cada classe real. Isso significa que cada linha da matriz (correspondente à classe verdadeira) soma 100%.

Com isso, conseguimos observar, por exemplo:

- Qual a porcentagem de acidentes reais que o modelo conseguiu classificar corretamente como acidentes;

- Qual a proporção de incidentes graves que foram confundidos com outra categoria;

- Até que ponto os incidentes estão sendo superestimados ou subestimados em termos de severidade.

Essa forma de apresentação é especialmente útil quando o modelo precisa ser avaliado não só pela sua precisão global, mas também pela fidelidade com que trata cada tipo de ocorrência individualmente, algo fundamental em cenários de risco, onde uma classificação errada pode ter implicações sérias.
        """
    )
    caminho_imagem = 'images/matconfnorm.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_container_width=True)

    st.markdown('<a name="impmatnorm"></a>', unsafe_allow_html=True)
    st.markdown("## Por que isso é importante para o nosso estudo?")
    st.markdown(
        """
        Em um contexto como o da aviação, confundir um acidente com um incidente, por exemplo, pode implicar em subestimar um risco real, o que, na prática, compromete a utilidade do modelo em sistemas de monitoramento e prevenção. Ao visualizar a matriz normalizada, conseguimos compreender melhor a tendência de erro do modelo: se ele é conservador (tende a minimizar a gravidade) ou alarmista (tende a superestimar os riscos), e se isso varia de uma classe para outra.

Essa análise torna-se então essencial para tomar decisões conscientes sobre a aplicação do modelo. Em determinados contextos, pode ser preferível aceitar um número maior de falsos positivos (por exemplo, classificar erroneamente um incidente como acidente), contanto que nenhum caso grave passe despercebido. Já em outros casos, a precisão pode ser mais valorizada.
        """
    )

    st.markdown('<a name="impfeat"></a>', unsafe_allow_html=True)
    st.markdown("## Importância das Features")
    st.markdown(
        """
        Agora que avaliamos o desempenho do modelo Random Forest em classificar as ocorrências aéreas com base nos dados fornecidos, damos um passo importante rumo à interpretabilidade do modelo: a análise da importância das variáveis, ou, em termos técnicos, a avaliação do feature importance.

Enquanto a acurácia e demais métricas nos dizem quão bem o modelo está performando, entender a importância relativa de cada variável nos permite descobrir por que ele está tomando determinadas decisões. Isso é especialmente relevante no nosso contexto, pois nos ajuda a compreender quais fatores contribuem de maneira mais decisiva para a classificação de uma ocorrência como ACIDENTE, INCIDENTE GRAVE ou INCIDENTE.

Dentro do modelo Random Forest, a importância de uma variável é medida com base na contribuição que ela oferece para a redução da impureza (ou incerteza) em cada árvore de decisão do conjunto. Em outras palavras, o modelo avalia quais variáveis são mais úteis para separar corretamente as classes ao longo dos diferentes ramos das árvores.

Cada vez que uma variável é usada para dividir os dados em uma árvore, e essa divisão melhora a pureza dos grupos resultantes (ou seja, reduz a mistura entre classes), essa variável ganha “crédito”. Ao fim do treinamento, somamos esse crédito em todas as árvores, o que nos dá uma medida quantitativa de importância relativa de cada atributo.
        """
    )
    caminho_imagem = 'images/impfeat.png'
    imagem = Image.open(caminho_imagem)
    st.image(imagem, use_container_width=True)

    st.markdown('<a name="relevfeat"></a>', unsafe_allow_html=True)
    st.markdown("## Por que isso é relevante para o nosso estudo?")
    st.markdown(
        """
        Saber quais variáveis “desbalanceiam o jogo” (isto é, quais exercem mais influência na previsão do tipo de ocorrência aérea) nos fornece insights valiosos não só para a modelagem, mas também para a aplicação prática dos resultados. Por exemplo:

- Podemos identificar fatores críticos de risco com base nas variáveis que mais pesam na classificação de acidentes;

- Descobrimos possíveis vieses nos dados, caso alguma variável esteja influenciando excessivamente o modelo de forma não esperada;

- Entendemos melhor o contexto operacional, ao verificar se variáveis como o tipo de aeronave, o horário, a localidade ou o fator contribuinte (clima, falha humana, etc.) estão fortemente associados a eventos mais graves.

Além disso, esse tipo de análise pode ser um ponto de partida para refinar o modelo, seja através da remoção de variáveis pouco informativas, seja pelo aprofundamento em variáveis altamente relevantes, talvez criando novas features derivadas delas.
        """
    )

    st.markdown('<a name="concs"></a>', unsafe_allow_html=True)
    st.markdown("## Conclusões")
    st.markdown(
        """
        Ao longo deste trabalho, buscamos explorar de forma sistemática e fundamentada a pergunta central que orienta nossa investigação: “É possível prever acidentes aéreos utilizando aprendizado de máquina?”. Essa pergunta nos levou por uma jornada que combinou aspectos técnicos, operacionais e conceituais.

        Desde o início, reconhecemos que prever acidentes aéreos não é uma tarefa simples, tampouco exata. Estamos lidando com eventos raros, que muitas vezes dependem de fatores imprevisíveis ou contextuais. Porém, a proposta do estudo nunca foi alcançar uma previsão determinística ou infalível. Nosso foco esteve em detectar padrões e tendências que, com apoio de algoritmos de machine learning, pudessem indicar níveis de risco ou potenciais sinais de alerta.

A modelagem preditiva, nesse contexto, se mostrou uma ferramenta complementar, que não substitui o julgamento técnico ou a investigação operacional, mas pode contribuir com análises antecipadas e suporte à tomada de decisão.

A utilização do LazyClassifier nos permitiu testar rapidamente uma gama variada de modelos supervisionados e comparar seu desempenho sob uma mesma base de critérios. Foi a partir dessa triagem inicial que emergiu o Random Forest como o modelo com os melhores resultados em métricas como acurácia, F1-score e recall.

Esse resultado nos levou a uma análise mais aprofundada e individual do Random Forest, que confirmou sua robustez, estabilidade e capacidade de generalização mesmo em um contexto com certo desequilíbrio entre classes. A explicabilidade do modelo (por meio da matriz de confusão e da importância das features) também se mostrou um diferencial importante.

Em síntese, os resultados aqui apresentados apontam que é possível, sim, aplicar modelos de aprendizado de máquina para prever padrões de risco na aviação civil, desde que com a devida cautela metodológica e respeito ao contexto operacional.

Nosso modelo Random Forest se mostrou promissor para classificar a gravidade de ocorrências com base em dados históricos, e seu desempenho pode ser aprimorado com ajustes adicionais.

Entretanto, é fundamental reforçar que modelos preditivos não substituem a análise de especialistas, mas podem atuar como instrumentos de apoio à segurança operacional, capazes de identificar tendências, priorizar investigações e antecipar cenários de risco.   
        """
    )