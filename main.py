import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título do aplicativo
st.title('Análise de Dados.csv Oceanográficos')

# Carregar o arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=";", na_values=None)

    st.header('Dados.csv Carregados')
    st.write(df.head(50))

    st.header('Tipos de Dados.csv')
    st.write(df.dtypes)

    # Adicionando coluna de profundidade em km
    df['Profundidade [km]'] = df['Profundidade [m]'] / 1000

    st.header('Estatísticas Descritivas')
    st.write(df.describe())

    st.header('Porcentagem de Valores Nulos')
    st.write(df.isnull().sum() / len(df))

    st.header('Histograma da Profundidade')
    fig, ax = plt.subplots()
    df['Profundidade [km]'].plot(kind='hist', bins=10, title='Histograma da Profundidade', ax=ax)
    plt.xlabel('Profundidade [km]')
    st.pyplot(fig)

    st.header('Colunas do DataFrame')
    st.write(df.columns)

    st.header('Mapa de Calor das Correlações')
    df_corr = df[['Profundidade [m]', 'Temperatura [°c]', 'Salinidade [psu]']]
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', linewidths=.5, ax=ax)
    plt.title('Heatmap das Correlações')
    st.pyplot(fig)

    st.header('Relação entre Temperatura, Salinidade e Profundidade')
    palette = sns.color_palette("crest", as_cmap=True)
    fig = sns.relplot(data=df, x='Temperatura [°c]', y='Salinidade [psu]', hue='Profundidade [m]', palette=palette)
    st.pyplot(fig)
