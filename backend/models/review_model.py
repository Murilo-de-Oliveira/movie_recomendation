from typing import Annotated, Optional
from pydantic import BaseModel, Field

class ReviewCreate(BaseModel):
    user_id: str
    movie_id: str
    rate: Annotated[int, Field(gt=0)]
    comment: Optional[str]