from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator

# insere no banco
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator('name')
    def name_not_empty(cls, value):
        if not value.strip():
            raise ValueError("Nome não pode estar vazio")
        return value
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao@email.com",
                "password": "Senha@123"
            }
        }

# recebe do banco
class UserOut(BaseModel):
    id: str
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    @field_validator('name')
    def name_not_empty(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Nome não pode estar vazio")
        return value
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Atualizado",
                "email": "novo@email.com"
            }
        }