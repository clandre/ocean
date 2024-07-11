import streamlit as st

mapa = st.selectbox('Escolha a expedição', options=['040181H40 LA PLATA 2004', 'OCEANO NORDESTE II', 'PIRATA VII'])
st.text('Passe o cursor sobre os elementos no mapa para mais informações')

path_to_html = f"html/{mapa}.html"

with open(path_to_html, 'r') as f:
    html_data = f.read()

# Show in webpage
st.components.v1.html(html_data, scrolling=True, height=800, width=800)
