import streamlit as st

st.header("Minha dashboard")
st.text("Meu texto")

# Análise de dados
import pandas as pd
dados_questionario = pd.read_csv(r"C:\Users\Odylon\Desktop\Questionário TEA - Respostas.csv", encoding='utf-8')

st.data_editor(dados_questionario)
