from fastapi import HTTPException, status
from models.movie_model import MovieCreate, MovieUpdate
from services.movie_service import create_movie_service, get_movie_service, update_movie_service, delete_movie_service

def create_movie_controller(movie_data: MovieCreate) -> str:
    return create_movie_service(movie_data)

def get_movie_controller(id: str):
    movie = get_movie_service(id)
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado"
        )
    return movie

def update_movie_controller(id: str, movie_data: MovieUpdate) -> str:
    try:
        result = update_movie_service(id, movie_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return {
        "success": True,
        "message": result,
        "data": None
    }

def delete_movie_controller(id: str) -> str:
    try:
        result = delete_movie_service(id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return {
        "success": True,
        "message": result,
        "data": None
    }