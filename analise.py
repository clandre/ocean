import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from st_pages import Page, show_pages, add_page_title
import plotly.express as px
import plotly.graph_objects as go

# Título do aplicativo
st.title('Análise de Dados Oceanográficos')

# Carregar o arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo csv", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=";", na_values=None)

    st.header('Amostra')
    st.dataframe(df.head(50))

    st.header('Tipos de Dados')
    st.dataframe(df.dtypes)

    st.header('Colunas do DataFrame')
    st.write(df.columns)

    # Adicionando coluna de profundidade em km
    df['Profundidade [km]'] = df['Profundidade [m]'] / 1000

    st.header('Estatísticas Descritivas')
    st.dataframe(df.describe())

    st.header('Porcentagem de Valores Nulos')
    st.dataframe(df.isnull().sum() / len(df))

    st.header('Histograma da Profundidade, Temperatura e Salinidade')
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df['Profundidade [km]'], nbinsx=10, name='Profundidade [km]'))
    fig.add_trace(go.Histogram(x=df['Temperatura [°c]'], nbinsx=10, name='Temperatura [°c]'))
    fig.add_trace(go.Histogram(x=df['Salinidade [psu]'], nbinsx=10, name='Salinidade [psu]'))
    # Sobreposição dos histogramas
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    fig.update_layout(title_text='Histogramas de Profundidade, Temperatura e Salinidade', xaxis_title='Valor',
                      yaxis_title='Contagem')

    st.plotly_chart(fig)

    st.header('Heatmap das Correlações')

    df_corr = df[['Profundidade [m]', 'Temperatura [°c]', 'Salinidade [psu]']]
    fig_corr = px.imshow(df_corr.corr(), text_auto=True)
    fig_corr.update_layout(coloraxis_reversescale=True)  # Invertendo a paleta de cores
    st.plotly_chart(fig_corr)

    st.header('Relação entre Temperatura, Salinidade e Profundidade')
    fig_rel = px.scatter(df, x='Temperatura [°c]', y='Salinidade [psu]', color='Profundidade [m]')
    fig_rel.update_layout(coloraxis_reversescale=True)  # Invertendo a paleta de cores
    st.plotly_chart(fig_rel)

    st.header('Boxplot das Variáveis Numéricas')
    selected_boxplot_column = st.selectbox('Selecione a coluna para o boxplot', options=df.select_dtypes(include=['number']).columns)
    fig_box = px.box(df, y=selected_boxplot_column, title=f'Boxplot de {selected_boxplot_column}')
    st.plotly_chart(fig_box)