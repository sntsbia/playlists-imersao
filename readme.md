# playlists-imersao

Este projeto é uma adaptação da aula de Imersão CloudDevOps da Alura em parceria com o Google, com o objetivo de demonstrar o processo de containerização e publicação de um banco de dados para utilização em outros projetos.

## Sobre

O repositório contém scripts e configurações para subir um banco de dados em ambiente Docker, facilitando o uso e integração com aplicações externas. O foco é a praticidade para desenvolvimento, testes e integração contínua, sem depender de infraestrutura externa.

## Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Como rodar o projeto

### Usando Docker Compose

1. Clone o repositório:

   ```bash
   git clone https://github.com/sntsbia/playlists-imersao.git
   cd playlists-imersao
   ```

2. Suba os containers com Docker Compose:

   ```bash
   docker compose up
   ```

   Isso irá criar e iniciar todos os serviços definidos no arquivo `docker-compose.yml`.

3. Para acompanhar os logs dos containers:

   ```bash
   docker compose logs -f
   ```

4. Para parar e remover os containers, redes e volumes criados pelo Compose:

   ```bash
   docker compose down
   ```

### Usando apenas Docker

Se preferir rodar o banco de dados manualmente, utilize os comandos abaixo (ajuste conforme a imagem e configurações do seu banco):

```bash
docker build -t playlists-imersao-db .
docker run -d --name playlists-db -p 8000:8000 playlists-imersao-db
```

## Publicação e Integração

Após subir o banco de dados, você pode conectar aplicações externas utilizando as credenciais e portas configuradas (consulte o `docker-compose.yml` para detalhes).

Se desejar expor o banco para uso em outro projeto, basta fornecer as informações de conexão conforme configurado.

## Estrutura do Projeto

- `Dockerfile` - Define a imagem Docker do banco de dados.
- `docker-compose.yml` - Orquestra os containers necessários.
- Scripts de inicialização e configuração do banco, se aplicável.

## Observações

- Para buildar e rodar o projeto, deve-se verificar se todas as permissões de leitura e escrita estão corretas.

## Créditos

Adaptação baseada na Imersão CloudDevOps da [Alura](https://www.alura.com.br/) em parceria com o Google.

---

Sinta-se à vontade para contribuir ou sugerir melhorias!

---

Beatriz Santos, 2025
