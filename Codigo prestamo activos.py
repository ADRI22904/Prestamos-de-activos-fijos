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
    de_que = st.text_input("¿De qué unidad o proyecto?")

    st.subheader("Información de los activos")
    placa = st.text_input("Placa")
    descripcion = st.text_input("Descripción del activo")
    marca = st.text_input("Marca")
    modelo = st.text_input("Modelo")
    serie = st.text_input("Serie")

    st.subheader("Entrega")
    unidad_custodio = st.text_input("Unidad Custodio")
    encargado = st.text_input("Encargado de Bienes Institucionales")
    encargado_cedula = st.text_input("Cédula del encargado")

    st.subheader("Recepción")
    fecha_devolucion = st.date_input("Fecha de devolución")

    submitted = st.form_submit_button("Generar PDF")

# --- GENERACIÓN DEL PDF ---
if submitted:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica", 11)

    y = 750

    def write(text):
        nonlocal y
        c.drawString(40, y, text)
        y -= 20

    write("UNIVERSIDAD DE COSTA RICA – UNIDAD DE BIENES INSTITUCIONALES")
    write("PRÉSTAMO DE ACTIVOS FIJOS")
    write("")
    write(f"Fecha: {fecha}")
    write("")
    write(f"Yo: {nombre}")
    write(f"Cédula o carné: {cedula}")
    write(f"En calidad de: {calidad}")
    write(f"Unidad/Proyecto: {de_que}")
    write("")
    write("Activo en préstamo:")
    write(f"  Placa: {placa}")
    write(f"  Descripción: {descripcion}")
    write(f"  Marca: {marca}")
    write(f"  Modelo: {modelo}")
    write(f"  Serie: {serie}")
    write("")
    write("ENTREGA")
    write(f"Unidad Custodio: {unidad_custodio}")
    write(f"Encargado de Bienes Institucionales: {encargado}")
    write(f"Cédula del encargado: {encargado_cedula}")
    write("")
    write("RECEPCIÓN")
    write(f"Fecha de devolución: {fecha_devolucion}")
    write("")
    write("Firmas:")
    write("  ________________________________    ________________________________")
    write("             Solicitante                          Encargado")
    write("")
    write("Nota: El original de este documento será entregado al solicitante después de")
    write("que se haya recibido satisfactoriamente el o los equipos.")

    c.save()

    st.success("PDF generado con éxito. Puede descargarlo abajo:")

    st.download_button(
        "Descargar PDF",
        data=buffer.getvalue(),
        file_name="prestamo_activos_fijos.pdf",
        mime="application/pdf"
    )

