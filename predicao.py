import streamlit as st
from cabecalho import cria_cabecalho

def tela_predicao():
    cria_cabecalho()

    st.markdown('<a name="predict"></a>', unsafe_allow_html=True)
    st.markdown("## Predição com Aprendizado de Máquina")
    st.markdown(
        """
        Standby
        """
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/cessna_210L.jpg", width=500, caption="Cessna 210L 1975")
