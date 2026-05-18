# 1.- ---------------- Encabezado ----------------------------------------------
# Autor : Jorge Anzaldo
# Editor: Lopez Alvarez Alan Saul
# Fecha : Mayo 2026

# 2.- ---------------- Importación de Módulos ----------------------------------
import networkx as nx
import matplotlib.pyplot as plt

# 3.- ---------------- Definición de Clases ------------------------------------

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        if self.frente is None:
            print("La cola está vacía")
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def esta_vacia(self):
        return self.frente is None


class ListaSimplementeEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    def contiene(self, identificador_buscar):
        actual = self.inicio
        while actual:
            objeto, peso = actual.dato
            if objeto.nombre == identificador_buscar:
                return True
            actual = actual.siguiente
        return False

    def obtener_identificadores(self):
        actual = self.inicio
        elementos = []
        while actual:
            objeto, peso = actual.dato
            elementos.append(f"{objeto.nombre}({peso})")
            actual = actual.siguiente
        return " -> ".join(elementos) if elementos else "Sin conexiones"


class Grafo:
    def __init__(self):
        self.almacen_objetos = []
        self.lista_identificadores = []
        self.listas_adyacencia = {}
        self.matriz = []

    def agregar_vertice(self, objeto):
        if objeto.nombre not in self.lista_identificadores:
            self.almacen_objetos.append(objeto)
            self.lista_identificadores.append(objeto.nombre)
            self.listas_adyacencia[objeto.nombre] = ListaSimplementeEnlazada()
            for fila in self.matriz:
                fila.append(0)
            self.matriz.append([0] * len(self.lista_identificadores))

    def _buscar_posicion(self, nombre):
        try:
            return self.lista_identificadores.index(nombre)
        except ValueError:
            return None

    def agregar_arista(self, origen, destino, peso=1):
        pos_o = self._buscar_posicion(origen)
        pos_d = self._buscar_posicion(destino)
        if pos_o is not None and pos_d is not None:
            if not self.listas_adyacencia[origen].contiene(destino):
                self.listas_adyacencia[origen].insertar(
                    (self.almacen_objetos[pos_d], peso)
                )
                self.matriz[pos_o][pos_d] = peso
        else:
            print("Error: vértice inexistente.")

    def mostrar_grafo(self):
        print("\n" + "="*70)
        print("LISTA DE ADYACENCIA DEL GRAFO")
        print("="*70)
        for vertice in self.lista_identificadores:
            print(f"{vertice:10} -> {self.listas_adyacencia[vertice].obtener_identificadores()}")

    def mostrar_matriz(self):
        print("\n" + "="*70)
        print("MATRIZ DE ADYACENCIA")
        print("="*70)
        print("            ", end="")
        for nombre in self.lista_identificadores:
            print(f"{nombre[:3]:>5}", end="")
        print()
        for i, fila in enumerate(self.matriz):
            print(f"{self.lista_identificadores[i]:10}", end=" ")
            for valor in fila:
                print(f"{valor:>5}", end="")
            print()

    def bfs(self, inicio):
        visitados = set()
        cola = Cola()
        cola.encolar(inicio)
        recorrido = []
        while not cola.esta_vacia():
            actual = cola.desencolar()
            if actual not in visitados:
                visitados.add(actual)
                recorrido.append(actual)
                nodo_actual = self.listas_adyacencia[actual].inicio
                while nodo_actual:
                    objeto, peso = nodo_actual.dato
                    vecino = objeto.nombre
                    if vecino not in visitados:
                        cola.encolar(vecino)
                    nodo_actual = nodo_actual.siguiente
        return recorrido

    def dfs(self, inicio, visitados=None, recorrido=None):
        if visitados is None:
            visitados = set()
        if recorrido is None:
            recorrido = []
        visitados.add(inicio)
        recorrido.append(inicio)
        nodo_actual = self.listas_adyacencia[inicio].inicio
        while nodo_actual:
            objeto, peso = nodo_actual.dato
            vecino = objeto.nombre
            if vecino not in visitados:
                self.dfs(vecino, visitados, recorrido)
            nodo_actual = nodo_actual.siguiente
        return recorrido

    def dijkstra(self, inicio):
        distancias = {v: float('inf') for v in self.lista_identificadores}
        distancias[inicio] = 0
        anteriores = {v: None for v in self.lista_identificadores}
        visitados = set()

        while len(visitados) < len(self.lista_identificadores):
            actual = None
            menor = float('inf')
            for vertice in self.lista_identificadores:
                if vertice not in visitados and distancias[vertice] < menor:
                    menor = distancias[vertice]
                    actual = vertice
            if actual is None:
                break
            visitados.add(actual)
            nodo_actual = self.listas_adyacencia[actual].inicio
            while nodo_actual:
                objeto, peso = nodo_actual.dato
                vecino = objeto.nombre
                nueva_distancia = distancias[actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual
                nodo_actual = nodo_actual.siguiente

        return distancias, anteriores

    def bellman_ford(self, inicio):
        distancias = {v: float('inf') for v in self.lista_identificadores}
        anteriores = {v: None for v in self.lista_identificadores}
        distancias[inicio] = 0

        for _ in range(len(self.lista_identificadores) - 1):
            for origen in self.lista_identificadores:
                nodo_actual = self.listas_adyacencia[origen].inicio
                while nodo_actual:
                    objeto, peso = nodo_actual.dato
                    destino = objeto.nombre
                    if distancias[origen] != float('inf'):
                        nueva = distancias[origen] + peso
                        if nueva < distancias[destino]:
                            distancias[destino] = nueva
                            anteriores[destino] = origen
                    nodo_actual = nodo_actual.siguiente

        # Detectar ciclos negativos
        for origen in self.lista_identificadores:
            nodo_actual = self.listas_adyacencia[origen].inicio
            while nodo_actual:
                objeto, peso = nodo_actual.dato
                destino = objeto.nombre
                if distancias[origen] != float('inf'):
                    if distancias[origen] + peso < distancias[destino]:
                        print("\nExiste un ciclo negativo.")
                        return None, None
                nodo_actual = nodo_actual.siguiente

        return distancias, anteriores

    def reconstruir_camino(self, anteriores, inicio, destino):
        camino = []
        actual = destino
        while actual is not None:
            camino.insert(0, actual)
            actual = anteriores[actual]
        if camino and camino[0] == inicio:
            return camino
        return []

    def visualizar(self, camino_dijkstra=None, camino_bellman=None):
        g = nx.Graph()  # No dirigido para layout más limpio
        for nombre in self.lista_identificadores:
            g.add_node(nombre)
        for origen in self.lista_identificadores:
            nodo = self.listas_adyacencia[origen].inicio
            while nodo:
                obj, peso = nodo.dato
                g.add_edge(origen, obj.nombre, weight=peso)
                nodo = nodo.siguiente

        fig, ax = plt.subplots(figsize=(26, 20))
        fig.patch.set_facecolor('#1a1a2e')
        ax.set_facecolor('#1a1a2e')

        # Kamada-Kawai produce un layout mucho más ordenado que spring
        pos = nx.kamada_kawai_layout(g, weight='weight')

        # --- Aristas base ---
        nx.draw_networkx_edges(g, pos, ax=ax,
                               edge_color='#4a4a6a', width=0.8, alpha=0.5)

        # --- Nodos ---
        nx.draw_networkx_nodes(g, pos, ax=ax,
                               node_color='#16213e', node_size=350,
                               edgecolors='#4fc3f7', linewidths=1.2)

        # --- Etiquetas ---
        nx.draw_networkx_labels(g, pos, ax=ax,
                                font_size=5, font_color='white',
                                font_weight='bold')

        def obtener_aristas(camino):
            return [(camino[i], camino[i+1]) for i in range(len(camino)-1)] if camino else []

        # --- Ruta Dijkstra (rojo) ---
        if camino_dijkstra:
            nx.draw_networkx_edges(g, pos, ax=ax,
                                   edgelist=obtener_aristas(camino_dijkstra),
                                   edge_color='#ff4757', width=4, alpha=0.9)
            nx.draw_networkx_nodes(g, pos, ax=ax,
                                   nodelist=camino_dijkstra,
                                   node_color='#ff4757', node_size=500,
                                   edgecolors='white', linewidths=1.5)

        # --- Ruta Bellman-Ford (azul punteado) ---
        if camino_bellman:
            nx.draw_networkx_edges(g, pos, ax=ax,
                                   edgelist=obtener_aristas(camino_bellman),
                                   edge_color='#2ed573', width=2.5,
                                   style='dashed', alpha=0.85)

        # --- Leyenda ---
        from matplotlib.lines import Line2D
        leyenda = [
            Line2D([0], [0], color='#ff4757', linewidth=3, label='Dijkstra'),
            Line2D([0], [0], color='#2ed573', linewidth=2,
                   linestyle='dashed', label='Bellman-Ford'),
        ]
        ax.legend(handles=leyenda, loc='lower right',
                  facecolor='#16213e', edgecolor='#4fc3f7',
                  labelcolor='white', fontsize=11)

        origen = camino_dijkstra[0] if camino_dijkstra else ""
        destino = camino_dijkstra[-1] if camino_dijkstra else ""
        ax.set_title(f"Red Metro CDMX  |  {origen} → {destino}",
                     color='white', fontsize=16, fontweight='bold', pad=15)
        ax.axis("off")
        plt.tight_layout()
        plt.savefig("metro.png", dpi=150, bbox_inches='tight',
                    facecolor=fig.get_facecolor())
        plt.close()
        print("\nImagen guardada como 'metro.png' en tu carpeta.")


class Estacion:
    def __init__(self, nombre=""):
        self.nombre = nombre

    def __repr__(self):
        return self.nombre