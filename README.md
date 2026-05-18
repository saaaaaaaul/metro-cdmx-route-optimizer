## English

# Metro CDMX Route Optimizer (Graph Algorithms Project)

## Overview

This project models the Mexico City Metro system as a **weighted graph** and computes the shortest path between any two stations using classical graph algorithms.

It compares the performance and results of:

- Dijkstra’s Algorithm
- Bellman-Ford Algorithm

Additionally, it generates a **visual representation of the computed route** and exports it as a PNG image.

---

## Key Features

- Full graph representation of the Mexico City Metro system
- Weighted edges representing travel time between stations
- Shortest path computation between any two stations
- Implementation of:
  - Dijkstra Algorithm (efficient shortest path)
  - Bellman-Ford Algorithm (robust against negative weights)
- Path reconstruction using predecessor tracking
- Graph visualization with highlighted optimal routes
- Automatic PNG export of computed metro routes

---

## Technical Concepts

This project demonstrates applied knowledge of:

- Graph Theory (weighted graphs)
- Adjacency List and Adjacency Matrix representations
- Custom data structures (Queue, Linked List)
- Greedy algorithms (Dijkstra)
- Dynamic programming / edge relaxation (Bellman-Ford)
- Path reconstruction algorithms
- Graph visualization using NetworkX and Matplotlib

---

## Project Structure

```
metro-cdmx-route-optimizer/
│
├── main.py                # Entry point (user interaction and algorithm comparison)
├── grafo.py              # Graph structure and algorithm implementations
├── archivos.py           # File handling utilities (JSON, CSV, TXT)
├── datos_metro.json      # Metro network dataset (stations and weighted connections)
├── metro.png             # Generated route visualization output
└── README.md
```

---

## How It Works

1. The metro network is loaded from a JSON dataset.
2. A weighted graph is constructed using stations and connections.
3. The user inputs:
   - Origin station
   - Destination station
4. The system computes the shortest path using:
   - Dijkstra Algorithm
   - Bellman-Ford Algorithm
5. Results are displayed:
   - Total travel time
   - Optimal route
6. A visual representation of the graph is generated and saved as a PNG file.

---

## Example

**Input:**

```
Origin: Lindavista  
Destination: Ciudad Deportiva
```

**Output:**

```
Shortest path using Dijkstra:
Lindavista → Deportivo 18 de Marzo → La Raza → Hidalgo → Balderas → Chabacano → Jamaica → Mixiuhca → Velódromo → Ciudad Deportiva

Total travel time: XX minutes
```

A visualization image (`metro.png`) is generated showing the computed route.

---

## Technologies Used

- Python 3
- NetworkX (graph modeling)
- Matplotlib (data visualization)
- JSON (data persistence)

---

## Why This Project Matters

This project demonstrates the ability to:

- Design and implement complex data structures from scratch
- Apply classical graph algorithms to real-world problems
- Model and process large-scale transportation networks
- Build complete systems: data → algorithm → visualization pipeline

---

## Author

Alan Saul López Álvarez  
Electronic and Communications Engineering Student — ESIME Zacatenco




## Español

---

## Descripción general

Este proyecto modela el sistema del Metro de la Ciudad de México como un **grafo ponderado** y calcula la ruta más corta entre dos estaciones utilizando algoritmos clásicos de teoría de grafos.

Se comparan los resultados y el comportamiento de:

- Algoritmo de Dijkstra
- Algoritmo de Bellman-Ford

Además, el sistema genera una **visualización de la ruta obtenida** y la exporta como una imagen PNG.

---

## Características principales

- Representación completa del Metro de la Ciudad de México mediante grafos
- Aristas ponderadas que representan el tiempo de traslado entre estaciones
- Cálculo de la ruta más corta entre cualquier par de estaciones
- Implementación de:
  - Algoritmo de Dijkstra (eficiente para caminos mínimos)
  - Algoritmo de Bellman-Ford (robusto ante pesos negativos en teoría)
- Reconstrucción de rutas mediante seguimiento de predecesores
- Visualización del grafo con rutas resaltadas
- Exportación automática de la ruta en formato PNG

---

## Conceptos técnicos

Este proyecto demuestra la aplicación de:

- Teoría de grafos (grafos ponderados)
- Representación mediante lista de adyacencia y matriz de adyacencia
- Estructuras de datos personalizadas (cola, listas enlazadas)
- Algoritmos voraces (Dijkstra)
- Programación dinámica / relajación de aristas (Bellman-Ford)
- Reconstrucción de caminos
- Visualización de grafos con NetworkX y Matplotlib

---

## Estructura del proyecto

```
metro-cdmx-route-optimizer/
│
├── main.py                # Punto de entrada (interacción y comparación de algoritmos)
├── grafo.py              # Estructura del grafo e implementación de algoritmos
├── archivos.py           # Utilidades de lectura/escritura de archivos (JSON, CSV, TXT)
├── datos_metro.json      # Dataset del metro (estaciones y conexiones ponderadas)
├── metro.png             # Imagen generada de la ruta
└── README.md
```

---

## Funcionamiento

1. Se carga la red del metro desde un archivo JSON.
2. Se construye un grafo ponderado con estaciones y conexiones.
3. El usuario introduce:
   - Estación de origen
   - Estación de destino
4. El sistema calcula la ruta más corta usando:
   - Algoritmo de Dijkstra
   - Algoritmo de Bellman-Ford
5. Se muestran resultados:
   - Tiempo total de recorrido
   - Ruta óptima
6. Se genera una visualización del grafo con la ruta resaltada y se guarda como imagen PNG.

---

## Ejemplo

**Entrada:**

```
Origen: Lindavista  
Destino: Ciudad Deportiva
```

**Salida:**

```
Ruta más corta con Dijkstra:
Lindavista → Deportivo 18 de Marzo → La Raza → Hidalgo → Balderas → Chabacano → Jamaica → Mixiuhca → Velódromo → Ciudad Deportiva

Tiempo total de recorrido: XX minutos
```

Se genera una imagen (`metro.png`) mostrando la ruta calculada.

---

## Tecnologías utilizadas

- Python 3
- NetworkX (modelado de grafos)
- Matplotlib (visualización de datos)
- JSON (persistencia de datos)

---

## Importancia del proyecto

Este proyecto demuestra la capacidad de:

- Diseñar e implementar estructuras de datos complejas desde cero
- Aplicar algoritmos clásicos a problemas reales
- Modelar redes de transporte a gran escala
- Construir sistemas completos: datos → algoritmos → visualización

---

## Autor

Alan Saul López Álvarez
Estudiante de Ingeniería en Comunicaciones y Electrónica — ESIME Zacatenco
