import streamlit as st
from cabecalho import cria_cabecalho

def mostra_graficos_interativos():
    cria_cabecalho()

    st.markdown('<a name="grafint"></a>', unsafe_allow_html=True)
    st.markdown("## Gráficos Interativos")
    st.markdown(
        """
        Standby
        """
    )
    st.markdown('<a name="colablink"></a>', unsafe_allow_html=True)
    st.markdown("## Notebook no Colab")
    st.markdown(
        """
        Standby
        """
        )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/cessna_210L.jpg", width=500, caption="Cessna 210L 1975")
