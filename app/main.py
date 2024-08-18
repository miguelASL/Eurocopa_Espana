from fastapi import FastAPI, Body, Path, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Any, Coroutine, Optional, List, Dict
from starlette.requests import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config.database import Session, engine, Base
from router.seleccion_router import seleccion_router
from db.seed import insertar_datos_iniciales
from config.database import Session

# Creación de la app con título y descripción mejorados
app = FastAPI(
    title="🇪🇸 My Project Spain",
    description="⚽ Bienvenido a la API de la Selección Española 🇪🇸. Aquí puedes encontrar información detallada sobre los jugadores y sus estadísticas. ¡Vamos, España! 🎉",
    version="1.0.0"
)

# Inclusión del router
app.include_router(seleccion_router)

# Creación de las tablas en la base de datos
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    db = Session()
    try:
        insertar_datos_iniciales(db)
    finally:
        db.close()

# Ruta de bienvenida
@app.get("/", tags=["home"])
def message():
    return HTMLResponse(content="<h1>🏠 ¡Bienvenido a la API de la Selección Española! 🇪🇸</h1>", status_code=200)

# uvicorn main:app --reload