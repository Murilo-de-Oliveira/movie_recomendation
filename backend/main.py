from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_route, movie_route, interaction_route

#app = FastAPI(
#    title="Movie App API",
#    description="API para gerenciamento de usuários da Movie App.",
#    version="1.0.0",
#)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para testes. Em produção, restrinja!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_route.router, prefix="/users", tags=["Usuários"])
app.include_router(movie_route.router, prefix="/movies", tags=["Filmes"])
app.include_router(interaction_route.router, prefix="/interactions", tags=["Interactions"])

@app.get("/")
def read_root():
    return {'Hello': 'World!'}