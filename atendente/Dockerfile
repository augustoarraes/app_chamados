FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    sqlite \
    sqlite-dev \
    bash \
    curl \
    && rm -rf /var/cache/apk/*

COPY requirements.txt .

#COPY . .

# Instala dependências Python
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copia o código do projeto
COPY . .

# Expor a porta do Django
EXPOSE 8000

# Comando para rodar o servidor de desenvolvimento
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
