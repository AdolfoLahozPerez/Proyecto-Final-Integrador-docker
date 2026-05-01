from fastapi import FastAPI, HTTPException
import json

app = FastAPI(title="Glosario Tech API", description="API REST para consultar términos tecnológicos")

with open("app/glosario.json", encoding="utf-8") as f:
    glosario_data = json.load(f)

@app.get("/")
def raiz():
    return {"mensaje": "Bienvenido a la API del Glosario Tech. Usa /terminos o /termino/{nombre}"}

@app.get("/terminos")
def obtener_terminos():
    return {"terminos": glosario_data}

@app.get("/termino/{nombre}")
def obtener_termino(nombre: str):
    nombre_lower = nombre.lower()
    for item in glosario_data:
        if item["termino"].lower() == nombre_lower:
            return item
    raise HTTPException(status_code=404, detail="Término no encontrado")

@app.get("/buscar")
def buscar_termino(q: str):
    resultados = [
        item for item in glosario_data
        if q.lower() in item["termino"].lower() or q.lower() in item["definicion"].lower()
    ]
    return {"resultados": resultados}
