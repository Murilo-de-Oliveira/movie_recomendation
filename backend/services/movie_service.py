import logging
from models.movie_model import MovieCreate, MovieUpdate
from repositories.movie_repo import create_movie_repo, get_all_movies_repo, get_movie_repo, update_movie_repo, delete_movie_repo, create_movie_node, update_movie_node, delete_movie_node

def create_movie_service(movie_data: MovieCreate) -> str:
    movie_id = create_movie_repo(movie_data)
    
    try:
        create_movie_node(movie_id, movie_data.title)
    except Exception as e:
        logging.warning(f"Erro ao criar nó do filme no Neo4j: {e}")

    return movie_id

def get_movie_service(id: str) -> dict:
    movie = get_movie_repo(id)
    if not movie:
        return None
    movie_dict = {
        "id":str(movie['_id']),
        "title":movie['title'],
        "director":movie['director'],
        "genre":movie['genre'],
        "rate":movie['rate'],
        "year":movie['year'],
        "synopsis":movie['synopsis']
    }
    return movie_dict

def get_all_movie_service():
    movie_list = get_all_movies_repo()
    if not movie_list:
        return []
    movie_list_dict = []
    for movie in movie_list:
        movie_dict = {
            "id":str(movie['_id']),
            "title":movie['title'],
            "director":movie['director'],
            "genre":movie['genre'],
            "rate":movie['rate'],
            "year":movie['year'],
            "synopsis":movie['synopsis']
        }
        movie_list_dict.append(movie_dict)
    return movie_list_dict

def update_movie_service(id: str, movie_data: MovieUpdate) -> str:
    updated = update_movie_repo(id, movie_data)
    if not updated:
        raise ValueError("Não foi possível atualizar o filme.")
    
    try:
        update_movie_node(id, movie_data)
    except Exception as e:
        logging.warning(f"Erro ao atualizar nó do filme no Neo4j: {e}")

    return {"message": "Filme atualizado com sucesso."}

def delete_movie_service(id: str) -> str:
    deleted = delete_movie_repo(id)
    if not deleted:
        raise ValueError("Não foi possível deletar o filme.")

    try:
        delete_movie_node(id)
    except Exception as e:
        logging.warning(f"Erro ao deletar nó do filme no Neo4j: {e}")
    return {"message": "Filme deletado com sucesso."}