# Etapa 1: Imagem base
# Usamos uma imagem slim do Python para um bom equilíbrio entre tamanho e funcionalidade.
# É uma boa prática usar a mesma versão do Python que você usa em desenvolvimento (3.12).
FROM python:3.12-slim

# Etapa 2: Definir o diretório de trabalho
# Isso define o diretório padrão para todos os comandos subsequentes.
WORKDIR /app

# Etapa 3: Variáveis de ambiente
# Evita que o Python crie arquivos .pyc e garante que os logs sejam enviados diretamente para o console.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Etapa 4: Copiar e instalar as dependências
# Copiamos o requirements.txt primeiro para aproveitar o cache de camadas do Docker.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: Copiar o código da aplicação
COPY . .

# Etapa 6: Expor a porta
# Informa ao Docker que o contêiner escutará na porta 8000.
EXPOSE 8000

# Etapa 7: Comando de execução
# Inicia o servidor Uvicorn. O host 0.0.0.0 é essencial para que a API seja acessível de fora do contêiner.
CMD ["uvicorn", "app:app", "--reload","--host", "0.0.0.0", "--port", "8000"]
