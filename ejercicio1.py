

import requests

def obtener_precio_bitcoin():
    try:
        # Realizar la solicitud a la API de CoinDesk
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Lanza una excepción en caso de error en la solicitud

        # Parsear la respuesta JSON y extraer el precio en USD
        data = response.json()
        precio_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))  # Eliminar comas del número

        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    # Solicitar la cantidad de bitcoins al usuario
    while True:
        try:
            cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        # Calcular el costo en USD de la cantidad de bitcoins
        costo_usd = cantidad_bitcoins * precio_bitcoin

        # Mostrar el resultado con cuatro decimales y separador de miles
        print(f"El costo actual de {cantidad_bitcoins:,.0f} Bitcoins es: ${costo_usd:,.4f}")

if __name__ == "__main__":
    main()


