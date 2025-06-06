from .user_service import get_user_service
from .movie_service import get_movie_service
from models.review_model import ReviewCreate
from repositories.interaction_repo import like_movie_repo, recommendation_repo

def like_movie_service(review: ReviewCreate) -> None:
    user = get_user_service(review.user_id)
    if not user:
        raise ValueError("Usuário não encontrado")
    movie = get_movie_service(review.movie_id)
    if not movie:
        raise ValueError("Filme não encontrado")
    review_dict = review.model_dump()
    like_movie_repo(review_dict)

def recommendation_service(movie_id: str) -> dict:
    movie = get_movie_service(movie_id)
    if not movie:
        raise ValueError("Filme não encontrado")
    recommendation = recommendation_repo(movie_id)
    return recommendation
    