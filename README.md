# Poblado Automático de Ontología - Mitología Griega

Este proyecto implementa un script en Python que utiliza la biblioteca **RDFlib** para instanciar automáticamente individuos en una ontología OWL/RDF a partir de un archivo CSV. Cumple con el ejerecicio de implementación de la Práctica 4.

## Descripción de los archivos

* `poblar_ontologia.py`: Script principal debidamente documentado con *docstrings*.
* `datos_mitologia.csv`: Base de datos tabular con los individuos a instanciar.
* `mitologia_base.rdf`: Ontologia original exportada desde Protégé.
* `mitologia_poblada.rdf`: Archivo resultante generado por el script.

## Replicación del entorno

Para asegurar la replicabilidad del proyecto y aislar las dependencias, he utilizado un entorno virutal con `virtualenv`.

### 1. Clonar el repositorio
Descarga los archivos del proyecto y sitúate en el directorio raíz:
```bash
git clone https://github.com/jmc00187/Poblaci-n-Autom-tica-de-una-ontologia.git
cd <NOMBRE_DE_LA_CARPETA>
```

### 2. Crear el entorno virtual
Crea un entorno virtual local llamado venv:
```bash
python -m venv venv
```

### 3. Activar el entorno virtual
* `En macOS y Linux`:
```bash
source venv/bin/activate
```

* `En Windows`:
```bash
venv\Scripts\activate
```

(Sabrás que está activado porque aparecerá (venv) al principio de tu línea de comandos).

### 4. Instalar las dependencias
El proyecto requiere la biblioteca rdflib para manipular el grafo de la ontología. Instálala ejecutando:
```bash
pip install rdflib
```

## Ejecución de la aplicación

Una vez que el entorno está activado y las dependencias instaladas, asegúrate de que el archivo mitologia_base.rdf y el datos_mitologia.csv están en la misma carpeta que el script.

Ejecuta el siguiente comando:
```bash
python poblar_ontologia.py
```
