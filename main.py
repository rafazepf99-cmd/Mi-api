from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos
class Incubadora(BaseModel):
    temperatura: float
    humedad: float
    encendida: bool

# Estado inicial
estado = Incubadora(
    temperatura=37.5,
    humedad=60.0,
    encendida=False
)

historial = []

# Ruta raíz
@app.get("/")
def inicio():
    return {"mensaje": "API de Incubadora funcionando"}

# Obtener estado
@app.get("/estado")
def obtener_estado():
    return estado

# Actualizar estado
@app.post("/estado")
def actualizar_estado(nuevo_estado: Incubadora):
    global estado
    estado = nuevo_estado
    historial.append(nuevo_estado)
    return {"mensaje": "Estado actualizado", "estado": estado}

# Encender incubadora
@app.put("/encender")
def encender():
    estado.encendida = True
    return {"mensaje": "Incubadora encendida"}

# Apagar incubadora
@app.put("/apagar")
def apagar():
    estado.encendida = False
    return {"mensaje": "Incubadora apagada"}

# Ver historial
@app.get("/historial")
def ver_historial():
    return historial