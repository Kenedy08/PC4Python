import requests
import sqlite3
import time

# Función para obtener los datos de la API y almacenarlos en la base de datos
def obtener_y_guardar_datos(fecha, cursor):
    try:
        response = requests.get(API_URL, params={"fecha": fecha})
        response.raise_for_status()
        data = response.json()
        cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)",
                       (fecha, data.get("compra"), data.get("venta")))
    except requests.RequestException as e:
        print(f"Error en la solicitud a la API: {e}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error al decodificar la respuesta JSON: {e}")

# API URL
API_URL = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

# Fechas
FECHAS = ["2023-01-01", "2023-12-31"]

# Conexión a la base de datos
with sqlite3.connect("base.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS sunat_info (fecha DATE, compra FLOAT, venta FLOAT)")

    # Obtener datos de la API y guardarlos en la base de datos
    for fecha in FECHAS:
        obtener_y_guardar_datos(fecha, cursor)
        time.sleep(1)

    # Mostrar contenido de la tabla
    cursor.execute("SELECT * FROM sunat_info")
    for row in cursor.fetchall():
        print(f"Fecha: {row[0]}\nCompra: {row[1]}\nVenta: {row[2]}\n")

