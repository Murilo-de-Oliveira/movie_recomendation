import logging
from repositories.user_repo import create_user_repo, get_user_repo, get_all_users_repo, update_user_repo, delete_user_repo, create_user_node, update_user_node, delete_user_node
from models.user_model import UserCreate, UserUpdate

def create_user_service(user_data: UserCreate):
    user_id = create_user_repo(user_data)

    try:
        create_user_node(user_id, user_data.name)
    except Exception as e:
        logging.warning(f"Erro ao criar nó do usuário no Neo4j: {e}")

    return user_id

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

def get_all_user_service():
    user_list = get_all_users_repo()
    if not user_list:
        return []
    user_list_dict = []
    for user in user_list:
        user_dict = {
            "id":str(user['_id']),
            "name":user['name'],
            "email":user['email']
        }
        user_list_dict.append(user_dict)
    return user_list_dict

def update_user_service(id: str, user: UserUpdate):
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


