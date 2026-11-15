# Taller 3 - APIs Públicas, MongoDB y EDA

**Autor:** Juan Manuel Silva Medina  
**Materia:** Bases de Datos  
**Profesor:** Miguel Ramos García  
**Fecha:** Noviembre 2026  

## Descripción
Este proyecto consume la API pública de **Rick and Morty**, almacena los datos crudos en MongoDB y realiza un Análisis Exploratorio de Datos (EDA).

## API utilizada
- **Nombre:** Rick and Morty API
- **URL:** https://rickandmortyapi.com/api/character
- **Registros descargados:** 100+
- **Sin autenticación requerida**

## Estructura del proyecto
```
Taller3_MongoDB/
├── ingesta.py                       # Script de extracción y carga a MongoDB
├── analisis.ipynb                   # Notebook con el EDA completo
├── grafica_torta_status.png         # Gráfica: distribución por estado
├── grafica_barras_especies.png      # Gráfica: top especies
├── grafica_histograma_episodios.png # Gráfica: episodios por personaje
├── requirements.txt                 # Librerías necesarias
├── .gitignore                       # Archivos excluidos
└── README.md                        # Este archivo
```


## Cómo ejecutar
1. `pip install -r requirements.txt`
2. Asegurarse que MongoDB está corriendo en localhost:27017
3. `python ingesta.py`
4. `jupyter notebook analisis.ipynb`

## Base de datos
- **Base de datos:** taller3_db
- **Colección:** raw_data

## Repositorio
https://github.com/juanmanuelsilva-prog/Taller3_MongoDB
