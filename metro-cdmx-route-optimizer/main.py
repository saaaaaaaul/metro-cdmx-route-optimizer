# 1.- ---------------- Encabezado ----------------------------------------------
# Autor : Jorge Anzaldo
# Editor: Lopez Alvarez Alan Saul
# Fecha : Mayo 2026
# Descripcion: Comparativa Dijkstra vs Bellman-Ford - Red Metro CDMX

# 2.- ---------------- Importación de Módulos ----------------------------------
from grafo import Grafo, Estacion
from archivos import ArchivosJSON

# 3.- ---------------- Variables u Objetos Globales ----------------------------
manejador_archivos = ArchivosJSON()
datos_importados = manejador_archivos.importar_json("datos_metro.json")

# 4.- ---------------- Funciones -----------------------------------------------
def cargar_red_metro():
    metro = Grafo()

    estaciones_json = datos_importados.get("estaciones", [])
    conexiones_json = datos_importados.get("conexiones", [])

    estaciones_u = sorted(list(set(estaciones_json)))
    for nombre_estacion in estaciones_u:
        metro.agregar_vertice(Estacion(nombre_estacion))

    for origen, destino, tiempo in conexiones_json:
        metro.agregar_arista(origen, destino, tiempo)
        metro.agregar_arista(destino, origen, tiempo)

    return metro

# 5.- ---------------- Bloque Principal ----------------------------------------
if __name__ == "__main__":

    if not datos_importados:
        print("ERROR: No se encontró el archivo 'datos_metro.json' o está vacío.")
    else:
        red_metro = cargar_red_metro()

        print("="*80)
        print("      COMPARATIVA DE ALGORITMOS DE RUTA - METRO CDMX")
        print("="*80)

        origen_entrada = input("Estación de Origen: ").strip()
        destino_entrada = input("Estación de Destino: ").strip()

        if origen_entrada not in red_metro.lista_identificadores or \
           destino_entrada not in red_metro.lista_identificadores:
            print("\nERROR: Estación no encontrada. Verifica la ortografía.")
        else:
            print("\n" + "*"*80)
            print(f" CARGANDO RUTA: {origen_entrada.upper()} -> {destino_entrada.upper()}")
            print("*"*80)

            # --- DIJKSTRA ---
            tiempos_dijkstra, padres_dijkstra = red_metro.dijkstra(origen_entrada)

            # --- BELLMAN-FORD ---
            tiempos_bellman, padres_bellman = red_metro.bellman_ford(origen_entrada)

            # ------------------------------------------------------------------
            # RESULTADOS DE DIJKSTRA
            # ------------------------------------------------------------------
            print("\n[ RESULTADOS ALGORITMO DIJKSTRA ]")
            if tiempos_dijkstra.get(destino_entrada) == float('inf'):
                print("Status: No se encontró un camino posible.")
            else:
                camino_dijkstra = red_metro.reconstruir_camino(
                    padres_dijkstra, origen_entrada, destino_entrada)
                print(f"Tiempo total: {tiempos_dijkstra[destino_entrada]} minutos")
                print(f"Ruta: {' -> '.join(camino_dijkstra)}")

            # ------------------------------------------------------------------
            # RESULTADOS DE BELLMAN-FORD
            # ------------------------------------------------------------------
            print("\n[ RESULTADOS ALGORITMO BELLMAN-FORD ]")
            if tiempos_bellman is None or tiempos_bellman.get(destino_entrada) == float('inf'):
                print("Status: No se encontró un camino o existe un ciclo negativo.")
                camino_bellman = []
            else:
                camino_bellman = red_metro.reconstruir_camino(
                    padres_bellman, origen_entrada, destino_entrada)
                print(f"Tiempo total: {tiempos_bellman[destino_entrada]} minutos.")
                print(f"Ruta: {' -> '.join(camino_bellman)}")

            # ------------------------------------------------------------------
            # VISUALIZACIÓN
            # ------------------------------------------------------------------
            print("\nGenerando imagen del grafo...")
            red_metro.visualizar(
                camino_dijkstra=camino_dijkstra,
                camino_bellman=camino_bellman
            )

    print("\n" + "="*80)