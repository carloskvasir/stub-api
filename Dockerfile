# Stage 1: Build and install dependencies
FROM python:3-slim-bookworm AS builder

WORKDIR /install

# Instala dependências em um diretório separado
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install/deps -r requirements.txt

# Stage 2: Final image
FROM python:3-slim-bookworm

ENV PORT=8000
WORKDIR /app

# Copia as dependências da imagem anterior
COPY --from=builder /install/deps /usr/local

# Copia apenas o código da aplicação
COPY app.py .

EXPOSE 8000

CMD ["python", "app.py"]
