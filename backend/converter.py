"""
Rotas de conversão de imagem para PDF.
Recebe upload de imagem, converte e retorna PDF.
"""

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from fpdf import FPDF
from PIL import Image, UnidentifiedImageError
import os
import io
import tempfile

router = APIRouter()

@router.post("/convert")
async def convert_image_to_pdf(image: UploadFile = File(...)):
    """
    Recebe uma imagem via upload, converte para PDF e retorna o arquivo PDF.
    """

    try:
        # Lê o conteúdo da imagem enviada pelo usuário
        contents = await image.read()

        # Tenta abrir a imagem usando o PIL (Pillow)
        img = Image.open(io.BytesIO(contents))

    except UnidentifiedImageError:
        return JSONResponse(
            content={"error": "Arquivo enviado não é uma imagem válida."},
            status_code=400
        )
    except Exception as e:
        return JSONResponse(
            content={"error": f"Erro ao processar imagem: {str(e)}"},
            status_code=500
        )

    try:
        # Cria um novo PDF
        pdf = FPDF()
        pdf.add_page()

        # Converte a imagem para RGB e salva temporariamente como JPEG
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_img_file:
            img.convert("RGB").save(temp_img_file, "JPEG")
            temp_img_path = temp_img_file.name

        # Adiciona a imagem ao PDF ajustando o tamanho (margem de 10)
        pdf.image(temp_img_path, x=10, y=10, w=pdf.w - 20)

        # Remove o arquivo temporário
        os.remove(temp_img_path)

        # Salva o PDF em memória como bytes
        pdf_bytes = pdf.output(dest='S').encode('latin1')
        pdf_stream = io.BytesIO(pdf_bytes)
        pdf_stream.seek(0)

        # Retorna o PDF como resposta
        return StreamingResponse(
            pdf_stream,
            media_type="application/pdf",
            headers={
                "Content-Disposition": "attachment; filename=convertido.pdf"
            }
        )

    except Exception as e:
        return JSONResponse(
            content={"error": f"Erro ao gerar PDF: {str(e)}"},
            status_code=500
        )
