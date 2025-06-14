from fastapi import HTTPException, status
from models.user_model import UserCreate, UserUpdate
from services.user_service import create_user_service, get_user_service, get_all_user_service, update_user_service, delete_user_service

def create_user_controller(user_data: UserCreate) -> str:
    return create_user_service(user_data)

def get_user_controller(id: str):
    user = get_user_service(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    return user

def get_all_users_controller():
    user_list = get_all_user_service()
    if not user_list:
        return []
    return user_list

def update_user_controller(id: str, user: UserUpdate):
    try:
        result = update_user_service(id, user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return result

def delete_user_controller(id: str):
    try:
        result = delete_user_service(id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return result