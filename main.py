import streamlit as st
from sidebar import menu_lateral

import importlib, sys, pkgutil

print("=== DEBUG AMBIENTE ===")
print("Python version:", sys.version)
print("sys.path:", sys.path)
print("plotly encontrado?", importlib.util.find_spec("plotly"))
print("plotly.express encontrado?", importlib.util.find_spec("plotly.express"))
print("pacotes instalados (10 primeiros):", list(sys.modules.keys())[:10])


st.set_page_config(
    page_title="Falhas em Aeronaves",
    page_icon="✈️",                 
    layout="wide"
)

menu_lateral()