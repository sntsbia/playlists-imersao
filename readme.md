# API de Playlists - Imersão DevOps Alura & Google Cloud

Este projeto é uma API desenvolvida com FastAPI para gerenciar uma coleção de playlists musicais.

## Pré-requisitos

- [Python 3.10 ou superior instalado](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Passos para subir o projeto

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/sntsbia/playlists-imersao.git
   cd playlists-imersao
   ```

2. **Crie um ambiente virtual:**
   ```sh
   python3 -m venv ./venv
   ```

3. **Ative o ambiente virtual:**
   - No Linux/Mac:
     ```sh
     source venv/bin/activate
     ```
   - No Windows, abra um terminal no modo administrador e execute o comando:
   ```sh
   Set-ExecutionPolicy RemoteSigned
   ```

     ```sh
     venv\Scripts\activate
     ```

4. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Execute a aplicação:**
   - Para acesso **local** (apenas na sua máquina):
   ```sh
   uvicorn app:app --reload
   ```
   - Para acesso **pela rede** (outros dispositivos na mesma rede Wi-Fi/cabeada):
   ```sh
   uvicorn app:app --reload --host 0.0.0.0
   ```

6. **Acesse a documentação interativa:**

   Abra o navegador e acesse:  
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

   Aqui você pode testar todos os endpoints da API de forma interativa.

---

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação FastAPI.
- `models.py`: Modelo da tabela `playlists` (SQLAlchemy).
- `schemas.py`: Schemas de validação de dados para playlists (Pydantic).
- `database.py`: Configuração do banco de dados SQLite.
- `routers/playlists.py`: Arquivo com as rotas (endpoints) para o CRUD de playlists.
- `requirements.txt`: Lista de dependências do projeto.

---

- O banco de dados SQLite será criado automaticamente como `playlist.db` na primeira execução.
- Para reiniciar o banco, basta apagar o arquivo `playlist.db` (isso apagará todos os dados).

---
