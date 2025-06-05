from fastapi import HTTPException, status
from services.interaction_service import like_movie_service

def like_movie_controller(user_id, movie_id):
    try:
        like_movie_service(user_id, movie_id)
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            details=e
        )
    return {"message": "Filme {movie_id} avaliado positivamente pelo usuário {user_id}"}

