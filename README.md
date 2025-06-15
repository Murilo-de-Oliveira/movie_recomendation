# 🎬 Movie Recommender Backend

Backend desenvolvido em Python com FastAPI, utilizando MongoDB e Neo4J para construção de um sistema de recomendação de filmes baseado em avaliações de usuários.

## 🚧 Status do Projeto

📦 Funcionalidades básicas: cadastro de usuários, filmes e relacionamentos de avaliação (RATED) entre eles.

## 🛠️ Tecnologias Utilizadas

- FastAPI
- MongoDB (armazenamento de dados)
- Neo4J (modelagem e análise de relacionamentos)
- Pydantic (validação de dados)
- Uvicorn (servidor ASGI)

## 📦 Pontos importante para rodar o projeto localmente

O python precisa estar na versão 3.8 para funcionar, visto que o driver do neo4j apresentado pelo professor
funciona nessa versão.
No __init__ database do neo4j é necessário trocar as credenciais de acesso para o ambiente local.
def __init__(self, uri="colocar o ip gerado pelo neo4j sandbox", user="neo4j", password="colocar a senha gerada pelo neo4j sandbox"):
É necessário ter os seguintes módulos para rodar o projeto: fastapi, neo4j, pymongo, bson, pydantic e uvicorn
Para iniciar o servidor, é necessário estar na pasta backend e rodar o comando: uvicorn main:app --reload
O projeto conta com dumps para usuários, filmes e reviews iniciais para testes, basta copiar os valores e colocar no MongoDB e no Neo4J Sandbox