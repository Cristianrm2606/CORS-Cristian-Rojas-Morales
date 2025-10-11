from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz
@app.get("/", response_class=PlainTextResponse)
def raiz():
    return "RAIZ – API, método GET"

# Ruta /hello/
@app.get("/hello/", response_class=PlainTextResponse)
def hello():
    return "Esta es la API inicial de Cristian"

# Ruta /api/personas
@app.get("/api/personas")
def personas():
    return {
        "id": 1,
        "nombre": "Cristian Rojas",
        "telefono": "8765-4321"
    }