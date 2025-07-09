import streamlit as st
from cabecalho import cria_cabecalho
from componentes import contact_style, sobre_link

def sobre_mim():
    st.markdown("## 👋 Sobre mim")
    
    # Colunas para layout
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Imagem de perfil (opcional)
        st.image("images/kawan.jpeg" ,use_container_width=True)
    
    with col2:
        # Informações básicas
        st.markdown("""
        ### **Kawan Oliveira**  
        _Estudante de Engenharia da Computação_  
        UFRN, Departamento de Engenharia da Computação e Automação  
        
        ---
        """)
        
        st.markdown("""
        - 👀 Tenho interesse em Sistemas Embarcados, IoT, Robótica e sistemas de mobilidade, como sistemas automotivos, aeronaves e foguetes.
        - 🌱 Atualmente, estou focado em aprender mais sobre Microcontroladores, RTOS e Visão Computacional.
        - 💞️ Buscando colaborar em novos desafios.

        Olá 👋! Meu nome é Kawan, tenho 21 anos e sou um estudante de Engenharia da Computação na UFRN em busca de oportunidades em sistemas embarcados e software embarcado, especialmente com OpenCV e técnicas aplicadas de Visão Computacional.

        Também aprecio aprendizado de máquina e aprendizado profundo, pois podem ser muito valiosos para aplicações em sistemas/software embarcados.

        ---

        🚀🚀 Atualmente membro do setor de eletrônica da :rainbow[Potiguar Rocket Design (PRD)] 
        
        """)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            sobre_link()
        
        st.markdown("""
        ---

        Com o objetivo de aprimorar minha proficiência em aprendizado de máquina, visão computacional e aprendizado profundo para aplicar essas habilidades em sistemas embarcados e softwares em geral, estou aberto a oportunidades de aprender sobre tecnologias relevantes e colaborar nesta área.

        Sinta-se à vontade para entrar em contato se tiver alguma oportunidade interessante ou sugestões! 😉

                    
        ---
        
        """)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.markdown("""""")
            st.markdown("""**Conecte-se comigo:** """)
        with col2:
            contact_style()
        
