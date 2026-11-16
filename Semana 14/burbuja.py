import random
import time


# Genera intervalos
def genera_intervalos(cantidad):
    elementos = [
        max(1, cantidad // 4),
        max(1, cantidad // 2),
        cantidad
    ]
    return sorted(set(elementos))


# Genera números
def genera_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 1_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo


# Ordena por el método de burbuja
def burbuja(datos):
    inicio = time.perf_counter()

    for i in range(len(datos) - 1):
        for j in range(len(datos) - 1 - i):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo


# Programa principal
while True:
    try:
        cantidad = int(input("Cantidad de elementos: "))

        if cantidad > 0:
            break

        print("La cantidad debe ser mayor que cero.")

    except ValueError:
        print("Ingrese un número entero.")


intervalos = genera_intervalos(cantidad)

for intervalo in intervalos:
    print(f"\n===== {intervalo} ELEMENTOS =====")

    datos, tiempo_generacion = genera_numeros(intervalo)
    print("Datos originales:", datos)

    datos, tiempo_burbuja = burbuja(datos)
    print("Datos ordenados:", datos)

    print(f"Tiempo de generación: {tiempo_generacion:.6f} segundos")
    print(f"Tiempo de burbuja: {tiempo_burbuja:.6f} segundos")
