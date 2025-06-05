from fastapi import APIRouter, status
from models.movie_model import MovieCreate, MovieOut, MovieUpdate
from controllers.movie_controller import create_movie_controller, get_movie_controller, update_movie_controller, delete_movie_controller

router = APIRouter()

@router.post(
    "/create_movie",
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo filme",
    description="Cria um novo filme com título, gênero, duração e classificação indicativa.",
    response_description="Mensagem de sucesso e ID do novo filme."
)
def create_movie_route(movie: MovieCreate) -> dict:
    """Rota de criação de filmes"""
    movie_id = create_movie_controller(movie)
    return {"message": "Filme criado com sucesso!", "id": str(movie_id)}

@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=MovieOut,
    summary="Buscar um filme por ID",
    description="Retorna os dados de um filme específico com base no ID fornecido.",
    response_description="Dados do filme encontrado."
)
def get_movie_route(id: str) -> dict:
    """Rota de leitura de filmes"""
    movie = get_movie_controller(id)
    return movie

@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Altera um filme por ID",
    description="Retorna os dados de um filme específico com base no ID fornecido.",
    response_description="Mensagem de sucesso."
)
def update_movie_route(
    id: str,
    movie: MovieUpdate 
):
    """Rota de alteração de filmes"""
    return update_movie_controller(id, movie)

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Deletar um filme por ID",
    description="Remove um filme do sistema e do banco de dados com base no ID fornecido.",
    response_description="Mensagem de sucesso."
)
def delete_movie_route(
    id: str
):
    """Rota de deleção de filmes"""
    return delete_movie_controller(id)
