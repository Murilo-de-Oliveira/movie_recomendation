# 🎬 Movie Recommender Backend

Backend desenvolvido em Python com FastAPI, utilizando MongoDB e Neo4J para construção de um sistema de recomendação de filmes baseado em avaliações de usuários.

## 🚧 Status do Projeto

🚀 Em desenvolvimento — MVP em construção  
📦 Funcionalidades básicas: cadastro de usuários, filmes e relacionamentos de avaliação (RATED) entre eles.

## 🛠️ Tecnologias Utilizadas

- FastAPI
- MongoDB (armazenamento de dados)
- Neo4J (modelagem e análise de relacionamentos)
- Pydantic (validação de dados)
- Pytest (testes unitários)
- Uvicorn (servidor ASGI)

## 📂 Estrutura de Pastas (parcial)

.
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── main.py
├── tests/
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore

## 🔄 Funcionalidades Implementadas

- [x] CRUD de usuários
- [x] CRUD de filmes
- [x] Relacionamento user-[RATED]->movie com nota e comentário
- [ ] Sistema de recomendação (em planejamento)
- [ ] Relacionamentos entre usuários e entre filmes (futuros)

## 📦 Como rodar o projeto localmente

1. Clone o repositório:
   git clone https://github.com/seu-usuario/movie-recommendation.git
   cd movie-recommender-backend

2. Crie e ative um ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Configure as variáveis de ambiente:
   - Copie .env.example para .env e preencha os valores.

5. Inicie o servidor:
   uvicorn main:app --reload

## 🧪 Rodando os testes

pytest tests/

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🙋‍♂️ Autor

Desenvolvido por Murilo de Oliveira.
