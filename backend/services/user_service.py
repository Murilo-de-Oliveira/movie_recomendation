import logging
from repositories.user_repo import create_user_repo, get_user_repo, update_user_repo, delete_user_repo, create_user_node, update_user_node, delete_user_node
from models.user_model import UserCreate, UserUpdate
import re

def create_user_service(user_data: UserCreate):
    user_id = create_user_repo(user_data)

    try:
        create_user_node(user_id, user_data.name)
    except Exception as e:
        logging.warning(f"Erro ao criar nó do usuário no Neo4j: {e}")

    return user_id

def _verify_email(email: str) -> bool:
    regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
    result = re.search(regex, email)
    
    if result:
        return True
    return False

def _verify_password(password: str) -> bool:
    special_characters_pattern = r'[^a-zA-Z0-9\s]'

    if len(password) < 8:
        raise ValueError('Senha muito curta')
    if not any(char.isdigit() for char in password):
        raise ValueError('A senha precisa ter pelo menos um número')
    if not any(char.isupper() for char in password):
        raise ValueError('A senha precisa ter pelo menos uma letra maiúscula')
    if not re.search(special_characters_pattern, password):
        raise ValueError('A senha precisa ter pelo menos um caractere especial')
    
    return True

def get_user_service(id: str):
    user = get_user_repo(id)
    if not user:
        return None
    user_dict = {
        "id":str(user['_id']),
        "name":user['name'],
        "email":user['email']
    }
    return user_dict

def update_user_service(id: str, user: UserUpdate):
    if user.password:
        _verify_password(user.password)
    #if user.email and not _verify_email(user.email):
    #    raise ValueError("Email inválido")

    updated = update_user_repo(id, user)
    if not updated:
        raise ValueError("Não foi possível atualizar o usuário.")
    
    try:
        update_user_node(id, user.name)
    except Exception as e:
        logging.warning(f"Erro ao atualizar nó do usuário no Neo4j: {e}")

    return {"message": "Usuário atualizado com sucesso."}

def delete_user_service(id):
    deleted = delete_user_repo(id)
    if not deleted:
        raise ValueError("Não foi possível deletar o usuário.")

    try:
        delete_user_node(id)
    except Exception as e:
        logging.warning(f"Erro ao deletar nó do usuário no Neo4j: {e}")
    return {"message": "Usuário deletado com sucesso."}


