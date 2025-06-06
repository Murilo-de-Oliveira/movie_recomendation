from fastapi import APIRouter
from models.review_model import ReviewCreate
from controllers.interaction_controller import like_movie_controller

router = APIRouter()

@router.post("/user/{user_id}/liked/{movie_id}")
def like_movie_router(
    review: ReviewCreate
):
    return like_movie_controller(review)