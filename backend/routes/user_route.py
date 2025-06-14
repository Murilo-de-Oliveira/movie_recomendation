from typing import List
from fastapi import APIRouter, status
from models.user_model import UserCreate, UserOut, UserUpdate
from controllers.user_controller import create_user_controller, get_user_controller, get_all_users_controller, update_user_controller, delete_user_controller

router = APIRouter()

@router.post(
    "/create_user",
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo usuário",
    description="Cria um novo usuário com nome, email e senha.",
    response_description="Mensagem de sucesso e ID do novo usuário"
)
def create_user_route(user: UserCreate) -> dict:
    """Rota de criação de usuários"""
    user_id = create_user_controller(user)
    return {"message": "Usuário criado com sucesso!", "id": str(user_id)}

@router.get(
    "/all_users",
    response_model=List[UserOut],
    summary="Obter todos os usuários",
    description="Retorna os dados públicos (nome e email) de um usuário."
)
def get_all_user_route():
    """Rota de buscar todos os usuários"""
    users = get_all_users_controller()
    return users

@router.get(
    "/{id}",
    response_model=UserOut,
    summary="Obter usuário por ID",
    description="Retorna os dados públicos (nome e email) de um usuário."
)
def get_user_route(id: str):
    """Rota de busca de usuário"""
    user = get_user_controller(id)
    return user

@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Atualizar usuário",
    description="Atualiza um ou mais campos de um usuário existente.",
    response_description="Mensagem de sucesso"
)
def update_user_route(
    id: str,
    user: UserUpdate
):
    """Rota de alteração de usuário"""
    return update_user_controller(id, user)

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Deletar usuário",
    description="Remove permanentemente um usuário com o ID informado.",
    response_description="Mensagem de sucesso"
)
def delete_user(id: str):
    """Rota de deleção de usuário"""
    return delete_user_controller(id)