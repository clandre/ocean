import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from st_pages import Page, show_pages, add_page_title

# Título do aplicativo
st.title('Análise de Dados Oceanográficos')

st.text("Análise inicial ...")

show_pages(
    [
        Page("main.py", "Home"),
        Page("analise.py", "Análise"),
        Page("mapa.py", "Expedição")
    ]
)