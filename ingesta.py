"""
ingesta.py
Taller 3 - APIs Públicas, MongoDB y EDA
Autor: Juan Manuel Silva Medina
Descripción: Descarga datos de la API Rick and Morty y los almacena en MongoDB
"""

import requests
from pymongo import MongoClient
from datetime import datetime

# ── Conexión a MongoDB ──────────────────────────────────────────────────────
client = MongoClient("mongodb://localhost:27017/")
db = client["taller3_db"]
collection = db["raw_data"]

print("✓ Conectado a MongoDB")
print(f"  Base de datos : taller3_db")
print(f"  Colección     : raw_data")

# ── Descarga de datos desde la API ─────────────────────────────────────────
BASE_URL = "https://rickandmortyapi.com/api/character"

def descargar_personajes():
    personajes = []
    url = BASE_URL
    pagina = 1

    while url:
        print(f"  Descargando página {pagina}...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        for p in data["results"]:
            p["_id"] = p["id"]  # Usar ID de la API como _id en MongoDB
            personajes.append(p)

        url = data["info"]["next"]
        pagina += 1

        if len(personajes) >= 100:
            break

    return personajes

# ── Inserción en MongoDB ───────────────────────────────────────────────────
print("\n📥 Iniciando descarga de personajes...")
personajes = descargar_personajes()

insertados = 0
duplicados = 0

for p in personajes:
    try:
        collection.insert_one(p)
        insertados += 1
    except Exception:
        duplicados += 1

print(f"\n✓ Proceso completado")
print(f"  Registros descargados : {len(personajes)}")
print(f"  Insertados en MongoDB : {insertados}")
print(f"  Duplicados omitidos   : {duplicados}")
print(f"  Total en colección    : {collection.count_documents({})}")
print(f"\n  Base de datos: taller3_db | Colección: raw_data")