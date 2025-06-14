import requests
from random import randint, choice

BASE_URL = "http://localhost:8000"

# Usuários de exemplo
users = [
    {"name": "Alice Silva", "email": "alice@example.com", "password": "Senha@123"},
    {"name": "Bruno Costa", "email": "bruno@example.com", "password": "Senha@123"},
    {"name": "Carlos Lima", "email": "carlos@example.com", "password": "Senha@123"},
    {"name": "Daniela Souza", "email": "daniela@example.com", "password": "Senha@123"},
]

# Filmes de exemplo
movies = [
    {"title": "A Esperança", "director": "João Mendes", "genre": "Drama", "synopsis": "Um filme sobre superação", "year": 2012},
    {"title": "Viagem no Tempo", "director": "Maria Tavares", "genre": "Ficção Científica", "synopsis": "Aventura em dimensões temporais", "year": 2018},
    {"title": "Segredos do Mar", "director": "Pedro Rocha", "genre": "Aventura", "synopsis": "Mistérios e descobertas submersas", "year": 2020},
    {"title": "Códigos Perdidos", "director": "Ana Martins", "genre": "Suspense", "synopsis": "Mensagens criptografadas e conspirações", "year": 2021},
]

# Comentários exemplo
comments = [
    "Muito bom!",
    "Gostei bastante, recomendaria!",
    "Não é o meu estilo, mas interessante.",
    "Atuação excelente!",
    "Esperava mais do final.",
    "Me surpreendeu!",
]

user_ids = []
movie_ids = []

# Criar usuários
for user in users:
    resp = requests.post(f"{BASE_URL}/users/create_user", json=user)
    if resp.status_code == 201:
        created = resp.json()
        print("[✔] Usuário criado")
        user_ids.append(created["id"])
    else:
        print("[✘] Erro ao criar usuário:", resp.text)

# Criar filmes
for movie in movies:
    resp = requests.post(f"{BASE_URL}/movies/create_movie", json=movie)
    if resp.status_code == 201:
        created = resp.json()
        print("[✔] Filme criado")
        movie_ids.append(created["id"])
    else:
        print("[✘] Erro ao criar filme:", resp.text)
