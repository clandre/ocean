import streamlit as st
import plotly.express as px

st.header('Relação entre Temperatura, Salinidade e Profundidade')

if 'df' in st.session_state:
    fig_rel = px.scatter(st.session_state.df, x='Temperatura [°c]', y='Salinidade [psu]', color='Profundidade [m]')
    fig_rel.update_layout(coloraxis_reversescale=True)  # Invertendo a paleta de cores
    st.plotly_chart(fig_rel)
else:
    st.text('Primeiro, escolha um arquivo de dados na tela inicial')