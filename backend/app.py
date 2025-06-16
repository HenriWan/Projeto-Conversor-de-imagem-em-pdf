"""
Arquivo principal do backend FastAPI.
Responsável por iniciar o servidor, configurar CORS e incluir as rotas de conversão.
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from converter import router as converter_router  # Importa o roteador de conversão

# Criação da instância do app FastAPI
app = FastAPI(
    title="ImageMaster API",
    description="API para conversão de imagens (PNG/JPG) em PDF.",
    version="1.0.0"
)

# Configuração de CORS (Cross-Origin Resource Sharing)
# Permite requisições de qualquer origem (para ambiente local ou frontend separado)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, defina apenas os domínios confiáveis
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho absoluto para a pasta do frontend
BASE_DIR = os.path.dirname(os.path.abspath(__file__))        # Caminho atual (backend/)
frontend_path = os.path.join(BASE_DIR, "..", "frontend")     # Caminho relativo ao diretório "frontend"

# Servir os arquivos estáticos do frontend (HTML, CSS, JS)
if os.path.isdir(frontend_path):  # Verifica se o diretório existe
    app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")
else:
    print(f"[AVISO] Diretório de frontend não encontrado: {frontend_path}")

# Inclusão das rotas de conversão (ex: /convert)
app.include_router(converter_router)
