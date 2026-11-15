# Taller 3 - APIs Públicas, MongoDB y EDA

**Autor:** Juan Manuel Silva Medina  
**Materia:** Bases de Datos  
**Profesor:** Miguel Ramos García  
**Fecha:** Noviembre 2026  

## Descripción

Este proyecto consume la API pública de **Rick and Morty** (https://rickandmortyapi.com), 
almacena los datos crudos en MongoDB y realiza un Análisis Exploratorio de Datos (EDA).

## API utilizada

- **Nombre:** Rick and Morty API
- **URL:** https://rickandmortyapi.com/api/character
- **Registros descargados:** 100+
- **Sin autenticación requerida**

## Estructura del proyecto

Taller3_MongoDB/
├── ingesta.py         # Descarga datos de la API y los guarda en MongoDB
├── analisis.ipynb     # Notebook con EDA: insights y visualizaciones
├── requirements.txt   # Dependencias del proyecto
├── .gitignore         # Archivos ignorados por git
└── README.md          # Este archivo

## Cómo ejecutar

### 1. Instalar dependencias
pip install -r requirements.txt

### 2. Asegurarse que MongoDB está corriendo
El servicio MongoDB debe estar activo en mongodb://localhost:27017

### 3. Ejecutar la ingesta
python ingesta.py

### 4. Abrir el notebook de análisis
jupyter notebook analisis.ipynb

## Base de datos

- **Base de datos:** taller3_db  
- **Colección:** raw_data