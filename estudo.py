import streamlit as st
from cabecalho import cria_cabecalho
from graficos import *

def resultado_estudos():
    cria_cabecalho()

    st.markdown(
        """
        Esta etapa de análise de dados deste estudo tem como objetivo compreender, estruturar e extrair informações relevantes 
        a partir dos registros de ocorrências aeronáuticas disponibilizados pelo CENIPA, referentes ao território brasileiro 
        a partir do ano de 2007. Esses dados, apesar de sua abrangência e riqueza informativa, apresentam alguns desafios, 
        como lacunas descritivas e categorias genéricas. Ainda assim, fornecem um panorama valioso para a identificação de padrões, 
        recorrências e possíveis fatores preditivos relacionados a acidentes aéreos.
        
        Por meio da organização, limpeza e categorização desses registros (que incluem dados sobre aeronaves, fatalidades, localizações, 
        horários e fatores contribuintes), busca-se investigar questões centrais da pesquisa, como a possibilidade de prever acidentes, 
        a existência de similaridades entre casos e a presença de padrões nos fatores causadores. A análise estatística e exploratória 
        desse conjunto de dados representa, portanto, uma etapa essencial para fundamentar as hipóteses do estudo e orientar a 
        construção de modelos preditivos e interpretativos no contexto da segurança da aviação.
        """
    )
    st.markdown('<a name="influanos"></a>', unsafe_allow_html=True)
    st.markdown("## Da Influência Dos Anos Em Incidentes")
    st.markdown("### Ocorrências por Mês (2007–2023)")
    grafico_ocorrencias_por_mes()

    st.markdown('<a name="ocomeses"></a>', unsafe_allow_html=True)
    st.markdown("## Ocorrências Mensais por Ano")
    grafico_ocorrencias_mensais()
    st.markdown(
        """ 
        Ao analisarmos os dois gráficos de distribuição mensal das ocorrências de incidentes ao longo dos anos considerados, 
        é possível identificar uma peculiaridade: embora a quantidade de ocorrências tenha se mantido relativamente estável 
        entre os meses e anos, observa-se um aumento expressivo e repentino a partir da segunda metade de 2023. Esse desvio 
        do padrão pode indicar uma mudança pontual no cenário da aviação brasileira e merece atenção especial nas análises seguintes.       
        """
    )
    st.markdown('<a name="distmesano"></a>', unsafe_allow_html=True)
    st.markdown("## Distribuição das Ocorrências Mensais ao Longo dos Anos")
    grafico_boxplot_ocorrencias_mensais()
    st.markdown(
        """
    Destrinchando melhor os incidentes que foram registrados no espaço aéreo brasileiro dentro do período 
    de 2007 a 2024, conseguimos filtrar todos os tipos de ocorrencia que temos registrados na base de dados do CENIPA
    Para facilitar a interpretação de dados, podemos pegar a tabela de incidentes registrados na base de 
    dados do CENIPA, presente abaixo:
        """
    )
    st.markdown('<a name="incidentescenipa"></a>', unsafe_allow_html=True)
    st.markdown("## Tipos de Incidentes registrados na base de dados do CENIPA")
    st.markdown(
        """
        | Tipo de Incidente |
        |-------------------|
        | FALHA DO MOTOR DURANTE O VÔO |
        | POUSANDO SEM TREM DE POUSO |
        | PERDA DE CONTROLE NO TERRENO |
        | ATERRAGEM LENTA |
        | PERDA DE CONTROLE NO AR |
        | DESCONHECIDO |
        | SOBRE O TREM DE POUSO |
        | COLISÃO DE TERRENO |
        | INCURSÃO DE PISTA |
        | FENÔMENO METEOROLÓGICO NO AR |
        | ATERRAGEM DURA |
        | OUTROS TIPOS |
        | SOBRE O ROTOR |
        | FALHA DO SISTEMA/COMPONENTE |
        | COLISÃO CONTRA OBSTÁCULO DURANTE O VÔO |
        | SOBRE JANELAS / PORTAS / PÁRA-BRISA |
        | PERDA DE COMPONENTE DURANTE O VÔO |
        | COLISÃO CONTRA OBSTÁCULO NO CHÃO |
        | FOGO DURANTE O VÔO |
        | DESEMBARQUE ANTES DA ÁREA DA PISTA |
        | CARREGAR LANÇAMENTO |
        | DESCOMPRESSÃO EXPLOSIVA/NÃO INTENCIONAL |
        | COLISÃO DE AERONAVES NO AR |
        | DESCONSCIÊNCIA ESPACIAL |
        | ATERRANDO EM LUGAR IMPREVISÍVEL |
        | ESTOURO DE PNEU |
        | FOME DE COMBUSTÍVEL |
        | PERDA DE COMPONENTES NO SOLO |
        | SOBRE A HÉLICE |
        | MANOBRAS DE BAIXA ALTITUDE |
        | FOGO NO CHÃO |
        | COLISÃO DE VEÍCULO CONTRA AERONAVES |
        | FOD - DANOS CAUSADOS POR OBJETO DESCONHECIDO |
        | COLISÃO DURANTE O VÔO CONTRA OBJETO REBOCADO |
        | AERONAVE ATINGIDA POR OBJETO |
        | FENÔMENO METEOROLÓGICO NO TERRENO |
        | COLISÃO DE AERONAVES NO SOLO |
        | FALHA ESTRUTURAL |
        | TRÁFEGO AÉREO |
        | COMANDOS DE VÔO |
        | VAZAMENTOS DE FLUIDO |
        | FUMAR NA CABINE |
        | SAINDO DA PISTA |
        | SOBRE PASSAGEIROS/TRIPULAÇÃO DURANTE O VÔO |
        | DESLIGAMENTO INVOLUNTÁRIO DO MOTOR |
        | PROBLEMAS FISIOLÓGICOS |
        | LANÇAMENTO DE PESSOAS |
        | COLISÃO CONTRA PÁSSARO |
        | FALHA DO MOTOR NO SOLO |
        """
    )
    st.markdown('<a name="top10ocorrencias"></a>', unsafe_allow_html=True)
    st.markdown("## Top 10 Tipos de Ocorrências Mais Frequentes e Menos Frequentes")
    grafico_top_10_tipos_acidentes()
    st.markdown(
        """
        Ao analisar os tipos de incidentes mais frequentes na tabela, observa-se uma tendência que aponta para a influência 
        de falhas de manutenção nas ocorrências registradas. Com exceção do outlier "colisão com aves", os quatro incidentes 
        mais recorrentes estão diretamente relacionados a falhas nos sistemas das aeronaves. É possível, inclusive, considerar 
        que em alguns casos de colisão, fatores mecânicos ou operacionais também possam ter contribuído indiretamente para o 
        desfecho do evento. Esse padrão reforça a importância da manutenção preventiva e da supervisão técnica contínua como 
        elementos-chave na prevenção de novos incidentes.
        """
    )
    grafico_bottom_10_tipos_acidentes()
    st.markdown(
        """
        Porém, em contrapartida, vendo os incidentes com menos aparição, também podemos visualizar falhas de sistemas 
        aeronáuticos entre os aqui tabelados; o que implica que, embora a manutenção de fato tem seu peso na equação de 
        quantidade de incidentes, ela não é necessáriamente a que tem maior peso individualmente falando, necessitando 
        então maior aprofundamento em outras variáveis que podem estar interligadas e correlacionadas indiretamente à 
        mecânica e operação dos sistemas.
        Devido a dificuldade de se trabalhar esses dados por meio da filtragem do tipo de incidente, visto que muitas 
        vezes um tipo de incidente pode ter variações do tipo de incidente, como por exemplo, os variados registros de 
        tipos de falhas, a partir desse momento, dentro desse estudo, iremos trabalhar com a taxonomia da ICAO, para 
        melhor visualizaçã̃o dos tipos de incidentes e sua associação com outros fatores.
        
        Desenvolvido pela equipe CAST/ICAO Common Taxonomy Team (CICTT), que foi encarregada de criar taxonomias e 
        definições comuns para sistemas de relatório de acidentes e incidentes de aviação. O objetivo principal é 
        classificar ocorrências (acidentes e incidentes) em um alto nível para permitir a análise de dados em apoio a 
        iniciativas de segurança. A intenção é fornecer taxonomias e definições "alvo" para organizações que estão implementando 
        novos sistemas de segurança.
        O caderno de taxonomias pode ser facilmente encontrado quando pesquisamos por "AVIATION OCCURRENCE 
        CATEGORIES - DEFINITIONS AND USAGE NOTES - CAST/ICAO Common Taxonomy Team - CICTT".
        """
    )
    st.markdown('<a name="incidentesicao"></a>', unsafe_allow_html=True)
    st.markdown("## Distribuição dos Tipos de Incidentes (ICAO)")
    grafico_distribuicao_tipos_incidentes()
    grafico_tipos_incidentes_ano()
    st.markdown(
        """
        Ao compararmos os dados gerais plotados com aqueles filtrados para o ano de 2024 (que apresentou o maior 
        número de incidentes) observa-se que o padrão de falhas se mantém consistente, com variações mínimas no ranqueamento 
        das ocorrências, praticamente insignificantes dentro do contexto geral de análise da relevância das variáveis.
        
        Importante destacar que essa análise pode ser estendida a outros anos, permitindo filtros por períodos específicos para 
        avaliar se o comportamento das falhas se mantém estável ou apresenta variações significativas em diferentes contextos temporais.
        
        Em ambos os gráficos, nota-se que o tipo de incidente mais frequente é o SCF-NP (System Component Failure - Non Powerplant), 
        relacionado a falhas mecânicas em componentes que não estão associados ao fornecimento de energia da aeronave. Isso indica 
        que sistemas menores embarcados podem estar influenciando diretamente o aumento no número de incidentes.
        
        Consequentemente, esses sistemas e componentes podem não estar recebendo a devida atenção durante as inspeções, sugerindo 
        que podem estar sendo parcialmente negligenciados ou não submetidos a uma revisão criteriosa.
        """
    )

    st.markdown('<a name="sobreaeronaves"></a>', unsafe_allow_html=True)
    st.markdown("## Sobre as Aeronaves Envolvidas")
    grafico_tipos_aeronaves()
    st.markdown(
        """
        Como já era esperado, os aviões representam a maior proporção de incidentes registrados na aviação civil brasileira. 
        Esse dado confirma uma tendência previsível: quanto maior a presença e a demanda por determinado tipo de aeronave no 
        espaço aéreo, maior também a probabilidade de ocorrência de incidentes envolvendo esse modelo. Não há, portanto, 
        surpresas quanto à distribuição dos eventos por tipo de veículo, pois nenhum outro modal aéreo apresenta números que contrariem 
        a expectativa inicial.

        Embora esse dado, isoladamente, não permita inferências conclusivas sobre causas ou responsabilidades, ele é significativo 
        por indicar qual categoria de aeronave concentra a maior parte das ocorrências e, consequentemente, onde reside o foco 
        principal deste estudo. Isso nos leva a refletir sobre a importância de analisar não apenas o número de incidentes, mas 
        também os contextos operacionais em que esses aviões estão inseridos (como frequência de uso, rotas, idade da frota, 
        manutenção e condições meteorológicas associadas).

        Ao entendermos que os aviões lideram naturalmente as estatísticas por representarem a espinha dorsal da aviação 
        comercial, reforça-se a necessidade de olhar com atenção para os fatores que envolvem seu desempenho e segurança operacional. 
        Afinal, são justamente esses veículos os maiores protagonistas do cenário que buscamos compreender e aprimorar ao longo desta pesquisa.
        """
    )
    grafico_top10_fabricantes()
    st.markdown(
        """
        Aproveitando para destrinchar também acerca das empresas fabricantes dessas aeronaves, trás-se a curiosidade de se 
        trazer que a Cessna Aircraft é a empresa que mais se envolve nos incidentes, não necessáriamente por conta da qualidade 
        de seus aviões, mas muito por conta de posicionamento no mercado e em correlação, a fatia de mercado abarcada pela empresa.
        O público-alvo da Cessna é bastante amplo e diversificado, por conta da sua variedade de modelos de aeronaves.
        Para estudantes e pilotos de aviação geral, a Cessna é reconhecida por seus aviões de treinamento, amplamente utilizados em 
        escolas de aviação para formação de pilotos. A Cessna oferece também uma gama de aeronaves para atividades de lazer, turismo, 
        e transporte pessoal. 
        Para nível empresarial, a Cessna produz aviões de negócios, como o Citation, que são utilizados para viagens de trabalho, 
        transporte de executivos e transporte de cargas. A Cessna oferece também aviões de negócios que podem ser usados em diferentes 
        tipos de operações, como transporte aéreo, transporte de passageiros e transporte de cargas.
        """
    )
    grafico_quantidade_motores()
    st.markdown(
        """
        No que diz respeito aos tipos de motores das aeronaves envolvidas nos incidentes registrados no dataset, observa-se uma 
        tendência que reflete não apenas o cenário nacional, mas também um movimento global da engenharia aeronáutica. O predomínio 
        de aeronaves com menos motores (especialmente monomotores e bimotores) está alinhado a uma busca constante por soluções 
        mais eficientes, sustentáveis e econômicas.

        Esse padrão é impulsionado por atualizações cada vez mais rigorosas nas legislações ambientais, que impõem limites à 
        emissão de poluentes, além do avanço tecnológico voltado à redução do consumo de combustível. Como resultado, há um 
        incentivo ao uso de motores menores e mais eficientes, favorecendo aeronaves mais leves e econômicas, como aquelas 
        utilizadas para instrução, pequenos voos regionais ou missões específicas.

        Consequentemente, monomotores e bimotores aparecem com maior frequência entre os incidentes registrados, simplesmente 
        porque representam a maior parte da frota operacional nessas categorias. Em contrapartida, os quadrimotores (antes mais comuns) 
        tornaram-se praticamente obsoletos no contexto atual, tanto pelo custo elevado de operação quanto pelas exigências ambientais e 
        pela evolução de projetos mais modernos.
        """
    )
    st.markdown('<a name="sobreregionalidade"></a>', unsafe_allow_html=True)
    st.markdown("## Sobre a Regionalidade dos incidentes")
    grafico_ocorrencias_por_uf()
    st.markdown(
        """
        Verificando onde estão ocorrendo mais incidentes, percebe-se que a grosso modo, uma possível teoria que a geomorfologia 
        poderia afetar a quantidade de incidentes cai por terra - no fim das contas, a tendência segue diretamente proporcional 
        à demanda de vôos em cada estado e demanda de aeroportos específicos de cada estado, que muitas vezes podem sofrer com alta demanda.
        Vale incrementar para a nossa análise, uma nota para essa matéria do site Airway:
        https://www.airway.com.br/guarulhos-e-congonhas-atrairam-mais-11-milhoes-de-passageiros-e-lideraram-ranking-de-aeroportos-de-2023/
        """
    )
    grafico_top3_ufs_por_ano()
    st.markdown(
        """
        Ao analisarmos os três estados com maior número de incidentes, observamos que eles mantêm uma tendência relativamente linear 
        ao longo dos anos, sem variações significativas que indiquem mudanças abruptas no comportamento dos dados. Esse padrão 
        sugere que as variáveis relacionadas à regionalidade, por si só, não exercem um impacto direto ou decisivo sobre os resultados do estudo.

        A única exceção a essa estabilidade ocorre a partir do segundo semestre de 2022, quando se verifica um aumento atípico no 
        número de ocorrências, sendo este um outlier que se destaca visualmente nos gráficos e que altera momentaneamente a distribuição regular 
        observada nos anos anteriores.
        """
    )
    st.markdown('<a name="estadoaeronaves"></a>', unsafe_allow_html=True)
    st.markdown("## Do Estado das Aeronaves")
    grafico_ano_fabricacao_acidentes()
    st.markdown(
        """
        Analisando o ano de fabricação das aeronaves envolvidas nos incidentes, podemos ligar novamente a linha de manutenção que 
        víamos no início da análise.

        Podemos perceber uma grande quantidade de aeronaves fabricadas nos anos de 2010 e década. Embora pareça curioso e pareça 
        um dado inicialmente aleatório, faz sentido quando pensamos em variáveis de: demanda de aeronaves, vida útil das aeronaves, 
        aumento do número de aeronaves compradas em uma certa época de aumento econômico e o como atualmente as manutenções das 
        aeronaves estão sendo feitas.

        A vida útil de um avião comercial, em média, é de 25 a 30 anos. No entanto, a vida útil de uma aeronave é também medida 
        pelo número de ciclos de voo (decolagem, voo e pouso), e não apenas pelo tempo em anos. Alguns aviões podem durar até 75.000 ciclos de voo. 

        Alguns fatores que afetam a vida útil:
        - Ciclos de voo: Aviões que realizam voos curtos e frequentes, como em rotas regionais, tendem a ter uma vida útil menor em termos de ciclos de voo, mesmo que durem o mesmo tempo em anos. 
        - Manutenção: A manutenção adequada e os testes de segurança periódicos são essenciais para prolongar a vida útil de uma aeronave. 
        - Tecnologia de fabricação: Avances tecnológicos na fabricação de aeronaves podem contribuir para uma maior durabilidade. 
        - Peso e tipo de voo: Aviões de grande porte que transportam cargas pesadas ou que realizam voos longos podem ter uma vida útil menor em termos de ciclos de voo.
        """
    )
    st.markdown('<a name="heatmapcorrela"></a>', unsafe_allow_html=True)
    grafico_heatmap_correlacao()
    st.markdown(
        """
        A partir da análise do heatmap das variáveis mais generalistas avaliadas inicialmente, percebe-se que nenhuma delas, de forma 
        isolada, apresenta uma correlação forte o suficiente para explicar de maneira direta o volume de incidentes registrados. Esse 
        resultado indica a necessidade de aprofundar a análise em variáveis mais específicas e contextuais, buscando relações menos 
        evidentes que possam contribuir de forma significativa para a compreensão dos fatores envolvidos.

        Apesar disso, é possível identificar uma leve correlação envolvendo o tipo de aeronave e o fabricante, o que reforça uma hipótese já 
        observada anteriormente: determinados fabricantes tendem a se especializar em tipos específicos de aeronaves, como aviões leves ou 
        aeronaves de instrução, que, por sua vez, estão mais presentes nas estatísticas de incidentes. Essa correlação, embora não conclusiva 
        por si só, aponta para caminhos mais detalhados a serem explorados nas próximas etapas da investigação.
        """
    )
    st.markdown('<a name="fatoreshumeng"></a>', unsafe_allow_html=True)
    st.markdown("## Dos fatores humanos / de engenharia")
    plot_top_fatores()
    st.markdown(
        """
        Analisando esses 4 gráficos, vemos que fatores ligados à humanidade operam maior impacto do que fatores materiais.
        Isso pode se dar por problemas de infraestrutura aeroportuária. Muitos aeroportos enfrentam capacidade limitada, 
        especialmente nos horários de pico, trazendo Problemas logísticos com bagagens e embarque/desembarque; além da falta de 
        modernização de sistemas de controle de tráfego ou pistas antigas e mal conservadas, e falta de pessoal qualificado (pilotos, 
        controladores de voo, mecânicos), além de escalas exaustivas, afetando segurança e produtividade.
        Oscilações nos preços do combustível (um dos maiores custos das companhias) e crises econômicas também afetam a demanda por 
        voos. Pandemias ou eventos globais podem paralisar operações.
        Analisando os outros 3 gráficos, em especial o de fator nome (primeiro), vemos que desses tópicos aqui abordados, no fim 
        das contas o maior peso se dá por recursos humanos, visto que ele está interligado com todos os outros indiretamente ou diretamente.
        """
    )
    #heatmaps, não vale a pena mexer
    st.markdown('<a name="heatmapnomevsocorr"></a>', unsafe_allow_html=True)
    grafico_fatores_condicionantes_por_periodo()
    st.markdown(
        """
        Ao observarmos o heatmap que relaciona os nomes dos fatores contribuintes com os tipos de ocorrência, fica evidente uma 
        concentração nas áreas de maior intensidade ("calor") associadas, majoritariamente, a falhas de natureza gerencial e 
        operacional humana. Excluindo as ocorrências relacionadas à falha de motor em voo (por se tratarem de eventos mais específicos e de 
        categorização técnica complexa), nota-se que os fatores com maior recorrência estão ligados à gestão operacional, tomada de decisão, 
        procedimentos inadequados e falhas na execução de tarefas.

        Essa evidência reforça a ideia de que, mais do que questões técnicas ou estruturais, grande parte dos incidentes está 
        relacionada a aspectos organizacionais e comportamentais. Isso indica a necessidade de maior atenção a processos de treinamento, 
        padronização de procedimentos, supervisão e cultura de segurança dentro das organizações aeronáuticas.
        """
    )
    st.markdown('<a name="heatmapnomevsaspec"></a>', unsafe_allow_html=True)
    grafico_fator_nome_fator_aspecto()
    st.markdown(
        """
        Percebe-se nesse segundo heatmap, uma forte concentração de aspectos psicológicos, relacionados ao ambiente operacional, 
        que afetam o desempenho humano na área. A sobrecarga das operações e a corrida para suprir a demanda está afetando diretamente 
        todas as variáveis, sendo assim impactando tanto na operacionalização das aeronaves, quanto na manutenção também das mesmas, 
        pois muitas aeronaves antes paradas na pandemia, podem estar sendo trazidas de volta a operação com mais urgência, e podendo não 
        estar passando por inspeções mais minuciosas que aeronaves nessas condições necessitariam; nessas condições de maior exposição à 
        intempéries, necessita-se maior cuidado com a operação, pois aspectos mecânicos podem ter sido afetados.
        """
    )

    st.markdown('<a name="fatorescond"></a>', unsafe_allow_html=True)
    st.markdown("## Dos fatores condicionantes")
    grafico_fatores_cond_mais_freq()
    st.markdown(
        """
        Vendo os fatores condicionantes mais frequentes, vemos que a operação das aeronaves, ou seja, os pilotos, também sofreram e vem sofrendo com aspectos que podemos inferir que estão ligados à formação dos mesmos.
        A formação de um piloto comercial no Brasil pode ultrapassar R\$ 200 mil, considerando cursos teóricos, certificações médicas e, principalmente, as horas de voo, que variam de R\$ 750 a R\$ 2.000 cada.
        Antes da pandemia, o Brasil enfrentava um déficit anual de cerca de 40% na formação de pilotos comerciais e mecânico. Após a retomada das atividades aéreas, a escassez se intensificou devido à aposentadoria de profissionais mais experientes e à migração de novos pilotos para mercados internacionais.
        Durante a pandemia, muitos voos foram suspensos, reduzindo as oportunidades para acumular as horas de voo necessárias para a certificação. Além disso, a crise econômica elevou os custos das horas de voo, tornando-as inacessíveis para muitos aspirantes. Esses fatores já afetavam à aviação no Brasil, se intensificando na pandemia e causando o aumento que vimos no início da nossa análise.
        """
    )
    grafico_fatores_2019_2020()
    st.markdown(
        """
        Trabalhando mais o aspecto da pandemia, vemos que de 2020 em diante, houve uma mudança na posição de manutenção no ranqueamento de fatores condicionantes. Isso, analisando mais a fundo, pode-se ter a ver com mudanças de tecnologia e Mudanças nos Modelos, principalmente quando puxamos novamente a questão da idade das aeronaves envolvidas.
        Nos anos 2000 e início de 2010, algumas aeronaves entraram em operação com novos sistemas e tecnologias.
        Aviões com "fly-by-wire": Muitas aeronaves lançadas nesse período foram equipadas com sistemas avançados de controle eletrônico, conhecidos como fly-by-wire, em que comandos de voo são dados através de computadores em vez de cabos tradicionais. Esses sistemas permitem maior precisão e eficiência, mas também aumentam a complexidade. Durante essa era, houve uma intensificação da automação nas aeronaves, especialmente no que se refere aos sistemas de navegação e controle de voo.
        
        O avanço tecnológico exige maior especialização na manutenção. Aeronaves fabricadas nos anos 2000-2010 exigem um nível de manutenção mais sofisticado, o que pode ser um desafio para algumas companhias aéreas, especialmente aquelas com menos recursos ou em regiões com infraestrutura deficiente.
        A complexidade das aeronaves fabricadas nos anos 2000 e 2010 pode gerar dificuldades para pilotos que não estão adequadamente treinados para lidar com as novas tecnologias e sistemas. 
        Em alguns casos, falhas humanas podem ser mais relacionadas à gestão do sistema do que ao sistema em si, podendo gerar erros de interpretação e resposta inadequada
        Uma das características também comuns nas aeronaves dessa época (especialmente em modelos mais novos) é a dependência de sistemas automatizados para melhorar a eficiência e segurança. No entanto, a automação não está isenta de falhas. Além disso, a falta de atualização contínua e adaptação do software de sistemas de controle de voo e aviônicos pode ser um fator relevante.
        """
    )
    st.markdown(
        """
        O fato de algumas aeronaves dessa faixa de anos (2000-2010) estarem envolvidas em mais acidentes pode ser parcialmente uma questão de estatísticas e volume de operações.
        À medida que novas aeronaves entram em operação, a probabilidade de envolvimento em acidentes também aumenta simplesmente porque essas aeronaves estão voando mais, atingindo mais horas de voo e mais situações críticas.
        Entre 2000 e 2010, houve uma expansão significativa da aviação comercial, especialmente em mercados emergentes como o Brasil. Isso significou mais aeronaves em operação, mas também mais desafios operacionais e de treinamento para lidar com as novas tecnologias e maiores volumes de passageiros.
        """
    )
    st.markdown('<a name="idadeaero"></a>', unsafe_allow_html=True)
    st.markdown("## Da idade das aeronaves")
    grafico_ano_aeronaves()
    grafico_ano_aeronaves_compacto()
    st.markdown(
        """
        Observando esses dois ultimos gráficos, fica ainda mais visível esse aspecto da idade correlacionada à tecnologia embarcada.
        Levantamos então algumas perguntas:
        - O quão validado estão os sistemas?
        - Qual o nível de manutenção nas novas tecnologias?
        - Já aprendemos a manusear e reparar as novas implementações?
        """
    )
    st.markdown(
        """
        Problemas comuns não vêm do Sistema Fly-By-Wire “puro”, mas de sua integração com:
        - Softwares de controle de estabilidade, como o MCAS
        - Automação de cockpit, onde pilotos às vezes se tornam mais “gestores de sistemas” do que “pilotos ativos”.
        - Interface homem-máquina mal projetada, que pode levar à confusão ou falha na interpretação de alertas

        Além também de aspectos de formação dos pilotos, como confiança excessiva na automação.
        O que acontece com aeronaves modernas não é um problema direto com o fly-by-wire, mas com:
        - Excesso de confiança dos pilotos na automação.
        - Dificuldade de retomar o controle manual em situações críticas.
        - Treinamentos nem sempre preparados para falhas do sistema automatizado.
        """
    )
    st.markdown('<a name="desafiosmanut"></a>', unsafe_allow_html=True)
    st.markdown("## Desafios da Manutenção de Aeronaves Modernas (década de 2010) no Brasil")
    st.markdown(
        """
        Aeronaves modernas têm mais sistemas eletrônicos, aviônicos e software, exigindo mecânicos com capacitação em eletrônica e TI. Muitas peças e componentes, em contrapartida, precisam ser importados, o que encarece e atrasa o processo, especialmente com a variação cambial.
        O Brasil enfrenta uma carência de mecânicos e engenheiros especializados em novas gerações de aeronaves. A formação técnica está concentrada em poucos centros (SENAI, EEAR, algumas universidades) e não acompanha o ritmo da demanda. Algumas empresas optam por terceirizar a manutenção (especialmente a pesada) para locais com menor custo (América Latina, Ásia), para também tentar suprir a demanda. Isso pode prejudicar a autossuficiência técnica nacional e tornar as operações mais vulneráveis a variações externas (crises, logística, diplomacia).
        """
    )
    st.markdown(
        """
        ### Menor exposição dos pilotos a situações reais de manutenção e avarias
        """
    )
    st.markdown(
        """
        Pilotos em formação aprendem como lidar com falhas e emergências — isso depende de ter aeronaves reais operando e interagindo com mecânicos, engenheiros e manutenção em tempo real.
        Com menos contato prático com equipes de manutenção, os pilotos têm menos compreensão técnica dos sistemas da aeronave.
        Pós-pandemia, muitas escolas e operadores reduziram o contato direto entre setores para economizar e evitar aglomerações, o que empobreceu a formação prática e interdisciplinar, o que leva ao enfraquecimento da cultura de segurança operacional.
        A aviação civil depende de uma forte cultura de segurança — algo que se aprende por imersão em operações bem estruturadas, com manutenção rigorosa, feedback constante e diálogo entre áreas técnicas.
        Com escolas e aeroclubes lutando financeiramente após a pandemia, houve redução de instrutores, mecânicos experientes e cortes em programas de segurança e CRM (Crew Resource Management).
        Pilotos recém-formados acabam com formação técnica mínima, pouca vivência com incidentes reais, e menos habilidades para trabalhar em equipe com manutenção, algo vital no dia a dia da aviação.
        """
    )
    st.markdown(
        """
        ### Cenário pós-pandemia: formação mais frágil + frota sobrecarregada
        """
    )
    st.markdown(
        """
        Muitas empresas cortaram investimentos em manutenção durante a pandemia e aceleraram a retomada em 2022–2023. Pilotos formados nesse período tiveram menos tempo de voo, menos voos reais e menos tempo em simuladores de alta complexidade.

        Ao serem contratados, enfrentaram aeronaves exigentes, sob pressão, com maior carga de trabalho técnico — isso aumenta o risco operacional.

        Resultado: aumento de relatos de "incidentes evitáveis", como falhas de checklist, interpretação errada de alertas ou dificuldade em comunicar problemas técnicos à manutenção.
        """
    )
    st.markdown('<a name="conclusoes"></a>', unsafe_allow_html=True)
    st.markdown("## Conclusões da análise")
    st.markdown(
        """
        Concluímos então que a alta demanda por aviação sofrida pós pandemia (em especial podemos destacar o grande aumento que houve no ano passado), fez com que toda a infraestrutura aeroportuária fosse sobrecarregada.
        
        O nível de qualidade das manutenções e formação de mão de obra qualificada não seguiu a mesma demanda. O setor sofreu, em contrapartida, um aumento de custos grande, na qual afeta o ciclo de cuidado das aeronaves.

        Isso somado à falta de qualificação, que não acompanhou a demanda e não acompanhou as mudanças tecnológicas.
        
        A terceirização de algumas partes operacionais, com a intenção de diminuir justamente esses custos de operação das aeronaves, não garante que conseguirá manter esses sistemas em pleno funcionamento e calibrados, visto que não garante que a mão-de-obra é qualificada para mexer em tecnologias mais recentes

        E o problema muitas vezes vem da “base”, visto que o processo de troca de gerações de pilotos não está conseguindo garantir uma exposição às falhas que podem ocorrer no processo de pilotagem, devido aos altos custos operacionais atuais, que faz com que as escolas de aviação ofereçam menos horas de vôo aos alunos, que tem menos exposição à situações atípicas…

        Com escolas e aeroclubes lutando financeiramente após a pandemia, houve redução de instrutores, mecânicos experientes e cortes em programas de segurança e CRM (Crew Resource Management).
        Junto a isso, temos uma frota cada vez mais sobrecarregada, que está precisando ser suprida por aviões cada vez mais perto do limiar de horas de vôo, e que por conta da necessidade da velocidade para se suprir a demanda pós pandemia, pode não ter passado por manutenção e vistorias mais rigorosas que se fazem necessárias em sistemas mecânicos que durante o período pandêmico tiveram pouco uso ou ficaram guardadas (situação essa que expõe todo o sistema mecânico à intempéries).

        O aumento dos incidentes não se dá por conta de um fator apenas individualizado em uma variável, mas sim, em um contexto geral que pode-se ser visualizado dessa forma feita nesta análise de dados, para entendermos como aqui foi feito então de onde vêm esse problema, e poder então pensar soluções e alternativas para se contornar o aumento dos incidentes da aviação civil brasileira.
        """
    )