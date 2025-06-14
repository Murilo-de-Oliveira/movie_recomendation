from typing import Optional
from pydantic import BaseModel, field_validator

valid_genres = ['Ação', 'Comédia', 'Drama', 'Terror', 'Ficção Científica', 'Romance', 'Aventura', 'Suspense']

class MovieCreate(BaseModel):
    title: str
    director: str
    genre: str
    synopsis: str
    year: int
    rate: float

    @field_validator('genre')
    def validate_genre(cls, genre):
        if not genre in valid_genres:
            raise ValueError('Gênero não listado')
        return genre
    
    @field_validator('year')
    def validate_year(cls, year):
        if year <= 1880 or year >= 2025:
            raise ValueError('Ano de Lançamento inválido')
        return year
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Título do filme",
                "director": "Diretor",
                "genre": "Drama",
                "synopsis": "This is a short synopsis",
                "year": 2000, 
                "rate":5
            }
        }
    
class MovieOut(BaseModel):
    id: str
    title: str
    director: str
    genre: str
    synopsis: str
    year: int
    rate: float

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    director: Optional[str] = None
    genre: Optional[str] = None
    synopsis: Optional[str] = None
    year: Optional[int] = None
    rate: Optional[float] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Título do filme",
                "director": "Diretor",
                "genre": "Drama",
                "synopsis": "This is a short synopsis",
                "year": 2000,
                "rate": 5
            }
        }