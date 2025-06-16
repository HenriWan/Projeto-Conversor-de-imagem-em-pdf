# Projeto Conversor de Imagem em PDF

## Descrição
Conversor de imagens (PNG/JPG) para PDF, com frontend web e backend FastAPI.

## Como rodar

### Backend
1. Instale as dependências:
   ```
   pip install fastapi uvicorn fpdf pillow
   ```
2. Execute o backend:
   ```
   uvicorn app:app --reload
   ```
   (Execute dentro da pasta `backend`)

### Frontend
Abra o arquivo `frontend/index.html` no navegador.

## Como contribuir

- Crie uma branch a partir da `dev`:
  ```
  git checkout dev
  git checkout -b feature/nome-da-sua-feature
  ```
- Faça commits claros e objetivos.
- Abra um Pull Request para a branch `dev`.

## Versionamento

- Usamos versionamento semântico (ex: v1.0.0).
- As versões são marcadas com tags no GitHub.
