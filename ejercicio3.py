import requests
from zipfile import ZipFile
from io import BytesIO

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as f:
            f.write(response.content)
        print("Imagen descargada correctamente como", nombre_archivo)
        return True
    else:
        print("Error al descargar la imagen")
        return False

def comprimir_zip(nombre_archivo):
    nombre_archivo_zip = nombre_archivo + '.zip'
    with ZipFile(nombre_archivo_zip, 'w') as zipf:
        zipf.write(nombre_archivo)
    print("Archivo comprimido como", nombre_archivo_zip)
    return nombre_archivo_zip

def descomprimir_zip(nombre_archivo_zip):
    with ZipFile(nombre_archivo_zip, 'r') as zipf:
        zipf.extractall()
    print("Archivo descomprimido")

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_imagen = "imagen_descargada.jpg"

    if descargar_imagen(url_imagen, nombre_imagen):
        nombre_zip = comprimir_zip(nombre_imagen)
        descomprimir_zip(nombre_zip)

if __name__ == "__main__":
    main()
