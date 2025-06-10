from fastapi import HTTPException, status
from services.interaction_service import like_movie_service, recommendation_service

def like_movie_controller(review):
    try:
        like_movie_service(review)
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            details=e
        )
    return {"message": f"Filme {review.movie_id} avaliado positivamente pelo usuário {review.user_id}"}

def recommendation_controller(movie_id) -> dict:
    try:
        recommendation = recommendation_service(movie_id)
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filme errado, mané"
        )
    return recommendation
