from fastapi import APIRouter
from controllers.interaction_controller import like_movie_controller

router = APIRouter()

@router.post("/user/{user_id}/liked/{movie_id}")
def like_movie_router(user_id: str, movie_id: str):
    return like_movie_controller(user_id, movie_id)