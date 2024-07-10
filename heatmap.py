import streamlit as st
import plotly.express as px

st.header('Heatmap das Correlações')

df_corr = st.session_state.df[['Profundidade [m]', 'Temperatura [°c]', 'Salinidade [psu]']]
fig_corr = px.imshow(df_corr.corr(), text_auto=True)
fig_corr.update_layout(coloraxis_reversescale=True)  # Invertendo a paleta de cores
st.plotly_chart(fig_corr)
