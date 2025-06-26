import streamlit as st
from sidebar import menu_lateral

st.set_page_config(
    page_title="Falhas em Aeronaves",
    page_icon="✈️",                 
    layout="wide"
)

menu_lateral()