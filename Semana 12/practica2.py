# grafos_semana12.py
# Samuel Martínez


def agregar_lugar(grafo, lugar):
    if lugar not in grafo:
        grafo[lugar] = []


def conectar(grafo, origen, destino):
    agregar_lugar(grafo, origen)
    agregar_lugar(grafo, destino)

    # Conexión no dirigida: se registra en ambos sentidos.
    if destino not in grafo[origen]:
        grafo[origen].append(destino)

    if origen not in grafo[destino]:
        grafo[destino].append(origen)


def mostrar_conexiones(grafo):
    for lugar, vecinos in grafo.items():
        texto = ", ".join(vecinos) if vecinos else "Sin conexiones"
        print(f"{lugar}: {texto}")


def mostrar_vecinos(grafo, lugar):
    if lugar in grafo:
        texto = ", ".join(grafo[lugar]) or "Sin vecinos"
        print(f"Vecinos de {lugar}: {texto}")
    else:
        print(f"{lugar} no existe en el grafo.")


def contar_conexiones(grafo):
    cantidades = {}

    for lugar, vecinos in grafo.items():
        cantidades[lugar] = len(vecinos)

    return cantidades


def consultar_conexion(grafo, origen, destino):
    return destino in grafo.get(origen, [])


def eliminar_conexion(grafo, origen, destino):
    if not consultar_conexion(grafo, origen, destino):
        print(f"No existe conexión entre {origen} y {destino}.")
        return False

    grafo[origen].remove(destino)
    grafo[destino].remove(origen)

    print(f"Conexión eliminada: {origen} - {destino}")
    return True


def actividad_7():
    print("\nACTIVIDAD 7: RED DE LABORATORIOS")

    laboratorios = {}

    conectar(laboratorios, "Redes", "Software")
    conectar(laboratorios, "Software", "Datos")
    conectar(laboratorios, "Software", "Robótica")
    conectar(laboratorios, "Robótica", "Electrónica")
    conectar(laboratorios, "Datos", "Electrónica")

    print("\nConexiones iniciales:")
    mostrar_conexiones(laboratorios)

    print("\nAgregamos Seguridad conectado a Redes:")
    conectar(laboratorios, "Seguridad", "Redes")

    print("\nConsulta de vecinos:")
    mostrar_vecinos(laboratorios, "Seguridad")

    print("\nCantidad de conexiones directas:")
    cantidades = contar_conexiones(laboratorios)

    for laboratorio, cantidad in cantidades.items():
        print(f"{laboratorio}: {cantidad}")

    print("\nGrafo final:")
    mostrar_conexiones(laboratorios)


def actividad_8():
    print("\nACTIVIDAD 8: SISTEMA DE TRANSPORTE")

    ciudades = {}

    # Ejemplo de conexiones, no representa rutas reales.
    for ciudad in ["Managua", "Masaya", "Granada", "León", "Estelí"]:
        agregar_lugar(ciudades, ciudad)

    conectar(ciudades, "Managua", "Masaya")
    conectar(ciudades, "Masaya", "Granada")
    conectar(ciudades, "Managua", "León")
    conectar(ciudades, "León", "Estelí")

    print("\nEstructura inicial:")
    mostrar_conexiones(ciudades)

    print("\nConsulta de vecinos:")
    mostrar_vecinos(ciudades, "Managua")

    print("\n¿Existe conexión directa entre Managua y Granada?")
    existe = consultar_conexion(ciudades, "Managua", "Granada")
    print("Sí" if existe else "No")

    print("\nOperación 1: conectar Managua con Granada.")
    conectar(ciudades, "Managua", "Granada")

    print("\nOperación 2: eliminar la conexión León - Estelí.")
    eliminar_conexion(ciudades, "León", "Estelí")

    print("\nResultado final:")
    mostrar_conexiones(ciudades)

    print("\nEs un grafo NO DIRIGIDO.")
    print("Cada conexión permite viajar en ambos sentidos.")


def main():
    actividad_7()
    actividad_8()


if __name__ == "__main__":
    main()