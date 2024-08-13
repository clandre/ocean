import streamlit as st
import pandas as pd
from st_pages import add_page_title, show_pages, Page

st.set_page_config(layout="wide")

def load_data(uploaded_file):
    dtype_spec = {
        9: 'str',
        19: 'str'
    }
    return pd.read_csv(uploaded_file, dtype=dtype_spec, sep=";", na_values=None)

def transformations():
    # Adicionando coluna de profundidade em km
    st.session_state.df['Profundidade [km]'] = st.session_state.df['Profundidade [m]'] / 1000

# Título do aplicativo
st.title('Análise de Dados Oceanográficos')

if 'df' not in st.session_state:
    # uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    st.session_state.df = load_data("data/Dados.csv")
    transformations()

    # if uploaded_file is not None:
    #     st.session_state.df = load_data(uploaded_file)
    #     transformations()

if 'df' in st.session_state:
    st.header('Amostra')
    st.dataframe(st.session_state.df.head(50))

    st.header('Tipos de Dados')
    st.dataframe(st.session_state.df.dtypes)

    st.header('Colunas do DataFrame')
    st.write(st.session_state.df.columns)

    st.header('Estatísticas Descritivas')
    st.dataframe(st.session_state.df.describe())

    st.header('Porcentagem de Valores Nulos')
    st.dataframe(st.session_state.df.isnull().sum() / len(st.session_state.df))

show_pages(
    [
        Page("main.py", "Home"),
        Page("mapa.py", "Mapas das Comissões"),
        Page("histograma.py", "Histograma"),
        Page("heatmap.py", "Heatmap"),
        Page("dispersao.py", "Dispersão"),
        Page("boxplot.py", "Boxplot")
    ]
)
