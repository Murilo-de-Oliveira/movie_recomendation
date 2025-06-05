from typing import Optional
from pydantic import BaseModel, field_validator

valid_genres = ['Ação', 'Comédia', 'Drama']
valid_classification = ['0','3','10','12','14','16','18']

class MovieCreate(BaseModel):
    title: str
    duration: str
    genre: str
    classification: str

    @field_validator('duration')
    def validate_duration(cls, duration):
        return duration

    @field_validator('genre')
    def validate_genre(cls, genre):
        if not genre in valid_genres:
            raise ValueError('Gênero não listado')
        return genre
    
    @field_validator('classification')
    def validate_classfication(cls, classification):
        if not classification in valid_classification:
            raise ValueError('Classificação não listada')
        return classification
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Título do filme",
                "duration": "01:30:00",
                "genre": "Drama",
                "classification": "10"
            }
        }
    
class MovieOut(BaseModel):
    title: str
    duration: str
    rate: float
    genre: str
    classification: str

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    duration: Optional[str] = None
    genre: Optional[str] = None
    classification: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Título do filme",
                "duration": "01:30:00",
                "genre": "Drama",
                "classification": "10"
            }
        }