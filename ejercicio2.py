import requests
from pyfiglet import Figlet
import random

def obtener_fuente_aleatoria():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente_seleccionada = random.choice(fuentes_disponibles)
    return fuente_seleccionada

def obtener_imagen_random():
    response = requests.get("https://picsum.photos/200/300")
    if response.status_code == 200:
        return response.content
    else:
        print("Error al obtener la imagen")
        return None

def main():
    opcion = input("¿Qué desea hacer? (figlet / imagen): ").strip().lower()

    if opcion == "figlet":
        # Solicitar al usuario el nombre de la fuente
        fuente_usuario = input("Ingrese el nombre de la fuente (deje en blanco para seleccionar aleatoriamente): ").strip()

        # Seleccionar aleatoriamente la fuente si no se proporciona una
        if not fuente_usuario:
            fuente_usuario = obtener_fuente_aleatoria()

        # Solicitar al usuario el texto
        texto_imprimir = input("Ingrese el texto que desea imprimir: ")

        # Crear el objeto Figlet y establecer la fuente
        figlet = Figlet()
        figlet.setFont(font=fuente_usuario)

        # Imprimir el texto utilizando la fuente seleccionada
        print(figlet.renderText(texto_imprimir))

    elif opcion == "imagen":
        imagen = obtener_imagen_random()
        if imagen:
            with open("imagen_random.jpg", "wb") as f:
                f.write(imagen)
            print("Imagen descargada correctamente como imagen_random.jpg")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()



