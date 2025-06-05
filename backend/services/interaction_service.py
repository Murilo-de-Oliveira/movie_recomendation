from user_service import get_user_service
from movie_service import get_movie_service
from repositories.interaction_repo import like_movie_repo

def like_movie_service(user_id, movie_id) -> None:
    user = get_user_service(user_id)
    if not user:
        raise ValueError("Usuário não encontrado")
    movie = get_movie_service(movie_id)
    if not movie:
        raise ValueError("Filme não encontrado")
    like_movie_repo(user_id, movie_id)

    