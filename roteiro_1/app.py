import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")

input = st.text_input(label="Escreva aqui")

if st.button("Clique-me"):
    st.write("Texto do input: " + input)