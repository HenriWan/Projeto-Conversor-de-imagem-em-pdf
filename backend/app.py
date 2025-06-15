"""
Arquivo principal do backend FastAPI.
Responsável por iniciar o servidor, configurar CORS e incluir as rotas de conversão.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from converter import router as converter_router

app = FastAPI()
app.include_router(converter_router)

# CORS liberado para qualquer origem (ajuste conforme necessidade)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir arquivos estáticos (frontend)
app.mount(
    "/frontend",
    StaticFiles(directory="c:/Users/henri/OneDrive/Área de Trabalho/Projeto conversor/Projeto-Conversor-de-imagem-em-pdf/backend"),
    name="frontend"
)
