"""
Script para poblar automáticamente la ontología de Mitología Griega.
Utiliza la biblioteca RDFlib para leer datos tabulares de un CSV y
generar las aserciones (tripletas) correspondientes en formato RDF.
"""

import csv
from rdflib import Graph, URIRef, Namespace
from rdflib.namespace import RDF, OWL

def poblar_ontologia(archivo_base, archivo_csv, archivo_salida):
    """
    Carga una ontología base en formato XML/RDF, añade individuos desde un CSV
    y exporta la ontología resultante.
    """
    # 1. Crear el grafo y cargar la ontología base
    g = Graph()
    g.parse(archivo_base, format="xml")

    # 2. Definir el Namespace exacto de tu ontología en Protégé
    MITO = Namespace("http://www.semanticweb.org/golfeno/ontologies/2026/2/untitled-ontology-4#")
    g.bind("mito", MITO)

    # 3. Leer el CSV y construir las tripletas
    with open(archivo_csv, mode='r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')
        
        # Esto imprimirá las columnas que detecta Python. Si sale todo junto, cambiaremos la coma por punto y coma.
        print("Cabeceras detectadas:", lector_csv.fieldnames)
        
        for fila in lector_csv:
            # Crear la URI del individuo
            sujeto_uri = URIRef(MITO + fila['Nombre'])
            
            # Asignar la Clase (ej: Zeus es un DiosOlimpico)
            clase_uri = URIRef(MITO + fila['Clase'])
            g.add((sujeto_uri, RDF.type, clase_uri))
            g.add((sujeto_uri, RDF.type, OWL.NamedIndividual))
            
            # Añadir propiedad: esHijoDe
            if fila['Progenitor']:
                progenitor_uri = URIRef(MITO + fila['Progenitor'])
                g.add((sujeto_uri, MITO.esHijoDe, progenitor_uri))
            
            # Añadir propiedad: habitaEn
            if fila['Lugar']:
                lugar_uri = URIRef(MITO + fila['Lugar'])
                g.add((sujeto_uri, MITO.habitaEn, lugar_uri))
                
            # Añadir propiedad: tienePoderSobre
            if fila['Poder']:
                poder_uri = URIRef(MITO + fila['Poder'])
                g.add((sujeto_uri, MITO.tienePoderSobre, poder_uri))
                
            print(f"Individuo procesado: {fila['Nombre']} ({fila['Clase']})")

    # 4. Guardar la nueva ontología
    g.serialize(destination=archivo_salida, format="xml")
    print(f"\n¡Éxito! Ontología poblada y guardada en: {archivo_salida}")

if __name__ == "__main__":
    ARCHIVO_ONTOLOGIA_BASE = "mitologia_base.rdf" 
    ARCHIVO_DATOS_CSV = "datos_mitologia.csv"
    ARCHIVO_NUEVO = "mitologia_poblada.rdf"
    
    poblar_ontologia(ARCHIVO_ONTOLOGIA_BASE, ARCHIVO_DATOS_CSV, ARCHIVO_NUEVO)