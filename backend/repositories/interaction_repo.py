import logging
from db import neo4j

def get_neo4j_session():
    return neo4j.Database()

def like_movie_repo(user_id, movie_id):
    session = get_neo4j_session()
    session.execute_write(
        query="""
            MATCH (u:User {id: $user_id} & m:Movie {id: $movie_id})
            MERGE (u)-[:LIKED]->(m)
        """,
        parameters={"user_id": user_id, "movie_id": movie_id}
    )