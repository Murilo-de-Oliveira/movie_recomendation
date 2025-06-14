import logging
from db import mongo, neo4j
from bson.objectid import ObjectId
from bson.errors import InvalidId
from models.user_model import UserCreate, UserUpdate

def get_mongo_session():
    return mongo.Database().get_collection("movie_app", "users")

def get_neo4j_session():
    return neo4j.Database()

def create_user_repo(user_data: UserCreate) -> str:
    session = get_mongo_session()
    user_dict = user_data.model_dump()
    result = session.insert_one(user_dict)
    return str(result.inserted_id)

def get_user_repo(id: str):
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return None
    session = get_mongo_session()
    return session.find_one({"_id": object_id})

def get_all_users_repo():
    session = get_mongo_session()
    users_list = list(session.find())
    return users_list

def update_user_repo(id: str, user_data: UserUpdate) -> bool:
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return None
    
    session = get_mongo_session()
    update_fields = user_data.model_dump(exclude_unset=True)

    if not update_fields:
        return False

    result = session.update_one(
        {"_id": object_id},
        {"$set": update_fields}
    )

    return result.matched_count > 0

def delete_user_repo(id: str) -> bool:
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return None
    
    session = get_mongo_session()
    result = session.delete_one({"_id":object_id})
    return result.deleted_count > 0

def create_user_node(user_id, user_name) -> None:
    session = get_neo4j_session()
    session.execute_write(
        query="CREATE (:User {id: $id, name: $name})",
        parameters={"id": user_id, "name": user_name}
    )
    logging.info(f"Usuário criado com id {user_id}")

def update_user_node(user_id, new_user_name) -> None:
    session = get_neo4j_session()
    session.execute_write(
        query="MATCH (u:User) WHERE u.id = $id SET u.name = $name",
        parameters={"id": user_id, "name": new_user_name}
    )
    logging.info(f"Usuário com id {user_id} alterado com sucesso. Novo nome: {new_user_name}")

def delete_user_node(user_id) -> None:
    session = get_neo4j_session()
    session.execute_write(
        query="MATCH (u:User) WHERE u.id = $id DETACH DELETE u",
        parameters={"id": user_id}
    )
    logging.info(f"Usuário com id {user_id} deletado com sucesso")