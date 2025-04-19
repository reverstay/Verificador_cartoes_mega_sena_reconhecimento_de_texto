FROM python:3.10-slim

# instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      tesseract-ocr libsm6 libxrender1 libxext6 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# dependências Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copiar o código
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
