import streamlit as st
from componentes import remove_espaco_sup

#Funcao para criacao do cabecalho; chamada em todo inicio de página ✈️
def cria_cabecalho():
    remove_espaco_sup()

    st.image("images/aviao2.jpg" ,use_column_width=True)
    st.markdown(
        "<h1 style='text-align: center;'>Estudo de falhas em aeronaves no espaço aéreo brasileiro</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: right;'>Por Kawan Oliveira</h3>",
        unsafe_allow_html=True
    )
    st.markdown("---")