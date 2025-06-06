from fastapi import APIRouter
from models.review_model import ReviewCreate
from controllers.interaction_controller import like_movie_controller, recommendation_controller

router = APIRouter()

@router.post("/user/{user_id}/liked/{movie_id}")
def like_movie_router(
    review: ReviewCreate
):
    return like_movie_controller(review)

@router.post("/users/also_liked/{movie_id}")
def recommendation_router(
    movie_id: str
):
    return recommendation_controller(movie_id)