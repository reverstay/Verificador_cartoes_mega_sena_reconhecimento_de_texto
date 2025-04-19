import cv2
import pytesseract
import re

def reconhecer_numeros(imagem_path):
    # 1. Carrega e converte em escala de cinza
    img = cv2.imread(imagem_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Binarização simples / threshold
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # 3. Chama Tesseract, configurado para dígitos apenas
    config = "--psm 6 outputbase digits"
    texto = pytesseract.image_to_string(thresh, config=config)

    # 4. Extrai sequências de dois dígitos (Mega‑Sena tem números de 01 a 60)
    nums = re.findall(r'\b([0-5]?\d)\b', texto)
    # filtra 1–60 e formata com zero à esquerda
    jogos = sorted({f"{int(n):02d}" for n in nums if 1 <= int(n) <= 60})
    return jogos
