import streamlit as st
import plotly.graph_objects as go


st.header('Histograma da Profundidade, Temperatura e Salinidade')

if 'df' in st.session_state:
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=st.session_state.df['Profundidade [km]'], nbinsx=10, name='Profundidade [km]'))
    fig.add_trace(go.Histogram(x=st.session_state.df['Temperatura [°c]'], nbinsx=10, name='Temperatura [°c]'))
    fig.add_trace(go.Histogram(x=st.session_state.df['Salinidade [psu]'], nbinsx=10, name='Salinidade [psu]'))
    # Sobreposição dos histogramas
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    fig.update_layout(title_text='Histogramas de Profundidade, Temperatura e Salinidade', xaxis_title='Valor',
                      yaxis_title='Contagem')

    st.plotly_chart(fig)
else:
    st.text('Primeiro, escolha um arquivo de dados na tela inicial')