import streamlit as st
from cabecalho import cria_cabecalho

def mostra_graficos_interativos():
    cria_cabecalho()

    st.markdown('<a name="grafint"></a>', unsafe_allow_html=True)
    st.markdown("## Gráficos Interativos")
    st.markdown(
        """
        Devido à complexidade e ao peso dos gráficos interativos, aliados às limitações de desempenho da máquina utilizada pelo Streamlit para o deploy, optei por separá-los e disponibilizá-los em um notebook no Google Colab, permitindo que sejam executados de forma independente.
        """
    )
    st.markdown('<a name="colablink"></a>', unsafe_allow_html=True)
    st.markdown("## Notebook no Colab")
    st.markdown(
        """
        Segue aqui o link para acesso do mesmo:
        <a href="https://colab.research.google.com/drive/1-yp7rRLk2yB2C9mB9kRxvfQnkfWmapmh?usp=sharing" target="_blank">
        <button style="
            background-color:#4285F4;
            color:white;
            padding:10px 20px;
            border:none;
            border-radius:5px;
            text-align:center;
            text-decoration:none;
            display:inline-block;
            font-size:16px;
            margin-top:10px;
            cursor:pointer;">
            Abrir no Google Colab 🚀
        </button>
        </a>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("images/cessna_210L.jpg", width=500, caption="Cessna 210L 1975")

