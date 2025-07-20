from rich.console import Console
terminal = Console()
import streamlit as st

terminal.print(f"Ejecucion de Streamlit Exitosa")

st.write("Este texto deberia mostrarse en Streamlit")
st.write("AHORA Skell's Sint TIENE DESARROLLO GRAFICO BASADO EN STREAMLIT, TOMA PERRO")

# Prueba de widgets de streamlit

col1, col2, col3 = st.columns(3)

with col1:
    valor1 = st.text_input("Valor 1")

with col2:
    valor2 = st.text_input("Valor 2")

with col3:
    boton = st.button("Sumar")

if boton:
    suma = int(valor1) + int(valor2)
    titulo = "".join(["Resultado: ", str(suma)])
    st.title(titulo)