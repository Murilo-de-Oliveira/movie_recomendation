import logging
from bson import ObjectId
from bson.errors import InvalidId
from db import mongo, neo4j
from models.movie_model import MovieCreate, MovieUpdate

def get_mongo_session():
    return mongo.Database().get_collection("movie_app", "movies")

def get_neo4j_session():
    return neo4j.Database()

def create_movie_repo(movie_data: MovieCreate) -> str:
    collection = get_mongo_session()
    movie_dict = movie_data.model_dump()
    result = collection.insert_one(movie_dict)
    return str(result.inserted_id)

def get_movie_repo(id: str):
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return None
    session = get_mongo_session()
    return session.find_one({"_id": object_id})

def get_all_movies_repo():
    session = get_mongo_session()
    movies_list = list(session.find())
    return movies_list

def update_movie_repo(id: str, movie_data: MovieUpdate):
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return None
    
    session = get_mongo_session()
    update_fields = movie_data.model_dump(exclude_unset=True)

    if not update_fields:
        return False

    result = session.update_one(
        {"_id": object_id},
        {"$set": update_fields}
    )

    return result.matched_count > 0

def delete_movie_repo(id: str) -> bool:
    try:
        object_id = ObjectId(id)
    except InvalidId:
        logging.warning(f"ID inválido: {id}")
        return None
    
    session = get_mongo_session()
    result = session.delete_one({"_id":object_id})
    return result.deleted_count > 0

def create_movie_node(movie_id: str, movie_title: str) -> None:
    session = get_neo4j_session()
    session.execute_write(
        query="CREATE (:Movie {id: $id, title: $title})",
        parameters={"id": movie_id, "title": movie_title}
    )
    logging.info(f"Filme criado com id {movie_id} e título {movie_title}")

def update_movie_node(movie_id, movie_data: MovieUpdate) -> None:
    session = get_neo4j_session()

    updates = []
    parameters = {"id": movie_id}

    if movie_data.title:
        updates.append("m.title = $title")
        parameters["title"] = movie_data.title
    if movie_data.genre:
        updates.append("m.genre = $genre")
        parameters["genre"] = movie_data.genre
    if movie_data.classification:
        updates.append("m.classification = $classification")
        parameters["classification"] = movie_data.classification

    if not updates:
        logging.info(f"Nenhuma alteração realizada para o filme com id {movie_id}")
        return

    set_clause = ", ".join(updates)

    session.execute_write(
        query=(f"MATCH (m:Movie) WHERE m.id = $id SET {set_clause}"), 
        parameters=parameters
    )
    logging.info(f"Filme com id {movie_id} atualizado com sucesso.")

def delete_movie_node(movie_id: str):
    session = get_neo4j_session()
    session.execute_write(
        query="MATCH (m:Movie {id: $id}) DETACH DELETE m",
        parameters={"id": movie_id}
    )
    logging.info(f"Filme com id {movie_id} deletado com sucesso.")
