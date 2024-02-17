def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as file:
            file.writelines([f"{numero} x {i} = {numero * i}\n" for i in range(1, 11)])
        print(f"Tabla de multiplicar {numero} guardada en el archivo tabla-{numero}.txt")
    except Exception as e:
        print(f"Error al guardar la tabla de multiplicar: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al mostrar la tabla de multiplicar: {e}")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()
            if 1 <= linea <= len(lineas):
                print(lineas[linea - 1], end='')
            else:
                print(f"La línea {linea} no está en el rango de la tabla.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al mostrar la línea de la tabla de multiplicar: {e}")

def main():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("Número fuera del rango permitido.")
        elif opcion in ("2", "3"):
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if opcion == "2":
                mostrar_tabla_multiplicar(numero)
            else:
                linea = int(input("Ingrese el número de línea a mostrar: "))
                mostrar_linea_tabla_multiplicar(numero, linea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
