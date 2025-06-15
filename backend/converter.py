"""

Rotas de conversão de imagem para PDF.
Recebe upload de imagem, converte e retorna PDF.
"""

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from fpdf import FPDF
from PIL import Image
import os
import io

router = APIRouter()

@router.post("/convert")
async def convert_image_to_pdf(image: UploadFile = File(...)):
    """
    Recebe uma imagem via upload, converte para PDF e retorna o arquivo PDF.
    """
    try:
        # Lê a imagem enviada
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
    except Exception as e:
        return JSONResponse(content={"error": f"Erro ao abrir imagem: {str(e)}"}, status_code=500)

    try:
        pdf = FPDF()
        pdf.add_page()

        # Salva a imagem temporariamente como JPEG
        temp_img_path = 'temp_img.jpg'
        img.convert('RGB').save(temp_img_path, 'JPEG')

        # Adiciona ao PDF e remove a imagem temporária
        pdf.image(temp_img_path, x=10, y=10, w=pdf.w - 20)
        os.remove(temp_img_path)

        # Salva o PDF em memória
        pdf_bytes = pdf.output(dest='S').encode('latin1')
        pdf_output = io.BytesIO(pdf_bytes)
        pdf_output.seek(0)

        return StreamingResponse(pdf_output, media_type="application/pdf", headers={
            "Content-Disposition": "attachment; filename=converted.pdf"
        })
    except Exception as e:
        return JSONResponse(content={"error": f"Erro ao gerar PDF: {str(e)}"}, status_code=500)
