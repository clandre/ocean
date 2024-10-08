import streamlit as st
import plotly.express as px

st.header('Boxplot das Variáveis Numéricas')

if 'df' in st.session_state:
    selected_boxplot_column = st.selectbox('Selecione a coluna para o boxplot', options=st.session_state.df.select_dtypes(include=['number']).columns)
    fig_box = px.box(st.session_state.df, y=selected_boxplot_column, title=f'Boxplot de {selected_boxplot_column}')
    st.plotly_chart(fig_box)
else:
    st.text('Primeiro, escolha um arquivo de dados na tela inicial')
