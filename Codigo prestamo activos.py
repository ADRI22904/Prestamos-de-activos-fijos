import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import date

st.title("Formulario de Préstamo de Activos Fijos - UCR")

st.write("Complete los datos para generar el documento PDF.")

# --- FORMULARIO ---
with st.form("prestamo_form"):
    fecha = st.date_input("Fecha", value=date.today())

    st.subheader("Datos del solicitante")
    nombre = st.text_input("Nombre completo")
    cedula = st.text_input("Cédula o carné")
    calidad = st.text_input("En calidad de (puesto o relación con la UCR)")
    de_que = st.text_input("¿De qué unidad o proyecto?

