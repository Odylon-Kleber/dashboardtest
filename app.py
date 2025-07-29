
import streamlit as st
import pandas as pd
import numpy as np



st.header("Minha dashboard")
st.text("Meu texto")

# Análise de dados
dados_questionario = pd.read_csv(r"C:\Users\Odylon\Desktop\Questionário TEA - Respostas.csv", encoding='utf-8')

st.data_editor(dados_questionario)


