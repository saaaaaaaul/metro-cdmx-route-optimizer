# 1.- ---------------- Encabezado ----------------------------------------------
# Autor       : Jorge Anzaldo
# Fecha       : 4-Marzo-2026
# Proyecto    : Manejo de archivos con estructuras dinamicas
# ------------------------------------------------------------------------------

# 2.- ---------------- Importación de Módulos ----------------------------------
import os
import csv
import json

# 3.- ---------------- Clases de Programador -----------------------------------
class ArchivosTXT:
    def _estructura_a_lista(self, estructura):
        lista_aux = []
        if isinstance(estructura, list): return estructura
        actual = getattr(estructura, 'inicio',
                 getattr(estructura, 'cima',
                 getattr(estructura, 'frente', None)))
        while actual:
            lista_aux.append(actual.dato)
            actual = actual.siguiente
        return lista_aux

    def exportar_txt(self, archivo, estructura):
        datos = self._estructura_a_lista(estructura)
        with open(archivo, 'w') as f:
            for item in datos:
                f.write(str(item) + "\n")
        print(f"Éxito: Datos convertidos de estructura dinámica a TXT.")

    def importar_txt(self, archivo):
        if not os.path.exists(archivo):
            print(f"No se encontró '{archivo}'.")
            return []
        with open(archivo, 'r') as f:
            lineas = f.readlines()
        datos = [eval(linea.strip()) for linea in lineas]
        print(f"Datos importados de '{archivo}' en formato TXT.")
        return datos

class ArchivosCSV:
    def exportar_csv(self, archivo, estructura):
        datos = ArchivosTXT()._estructura_a_lista(estructura)
        if not datos: return
        with open(archivo, 'w', newline='') as f:
            escritor = csv.DictWriter(f, fieldnames=datos[0].keys())
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"Éxito: CSV generado desde estructura dinámica.")

    def importar_csv(self, archivo):
        if not os.path.exists(archivo): return []
        with open(archivo, 'r') as f:
            return list(csv.DictReader(f))

class ArchivosJSON:
    def exportar_json(self, archivo, estructura):
        datos = ArchivosTXT()._estructura_a_lista(estructura)
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
        print(f"Éxito: JSON generado correctamente.")

    def importar_json(self, archivo):
        if not os.path.exists(archivo): return {}
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
