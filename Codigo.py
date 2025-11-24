import streamlit as st
from openpyxl import load_workbook
from io import BytesIO

EXCEL_PATH = "formulario.xlsx"  # archivo incluido en el proyecto

def llenar_excel(datos, activos):
    wb = load_workbook(EXCEL_PATH)
    ws = wb.active

    # --- Asignación de datos fijos ---
    ws["H9"] = datos["fecha"]
    ws["C12"] = datos["nombre"]
    ws["J12"] = datos["cedula"]
    ws["D14"] = datos["calidad"]

    # --- Activos (máximo 6) ---
    for idx, activo in enumerate(activos):
        row = 20 + idx
        ws[f"B{row}"] = activo["placa"]
        ws[f"D{row}"] = activo["descripcion"]
        ws[f"G{row}"] = activo["marca"]
        ws[f"I{row}"] = activo["modelo"]
        ws[f"K{row}"] = activo["serie"]

    # Unidad custodio
    ws["E32"] = datos["unidad_custodio"]
    ws["E34"] = datos["encargado_bienes"]
    ws["E36"] = datos["cedula_uc"]

    # Nombre en D45–E45
    ws["D45"] = datos["nombre"]

    # Guardar en memoria
    output = BytesIO()
    wb.save(output)
    output.seek(0)
    return output

st.title("Formulario de Préstamo de Bienes")

nombre = st.text_input("Nombre completo")
cedula = st.text_input("Cédula o carné")
fecha = st.date_input("Fecha del préstamo")
calidad = st.text_input("Calidad del solicitante (estudiante, funcionario…)")

num_activos = st.number_input("Cantidad de activos", 0, 6, 1)

activos = []
for i in range(num_activos):
    st.subheader(f"Activo {i+1}")
    placa = st.text_input(f"Placa {i+1}")
    descripcion = st.text_input(f"Descripción {i+1}")
    marca = st.text_input(f"Marca {i+1}")
    modelo = st.text_input(f"Modelo {i+1}")
    serie = st.text_input(f"Serie {i+1}")

    activos.append({
        "placa": placa,
        "descripcion": descripcion,
        "marca": marca,
        "modelo": modelo,
        "serie": serie
    })

unidad_custodio = st.text_input("Unidad custodio")
encargado_bienes = st.text_input("Encargado de bienes institucionales")
cedula_uc = st.text_input("Cédula unidad custodio")

if st.button("Generar archivo"):
    datos = {
        "nombre": nombre,
        "cedula": cedula,
        "fecha": fecha.strftime("%d/%m/%Y"),
        "calidad": calidad,
        "unidad_custodio": unidad_custodio,
        "encargado_bienes": encargado_bienes,
        "cedula_uc": cedula_uc
    }

    excel_file = llenar_excel(datos, activos)
    st.download_button(
        "Descargar formulario",
        data=excel_file,
        file_name="formulario_prestamo_filled.xlsx"
    )



