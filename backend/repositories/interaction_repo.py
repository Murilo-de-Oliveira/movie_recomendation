import logging
from db import neo4j

def get_neo4j_session():
    return neo4j.Database()

def like_movie_repo(review: dict):
    session = get_neo4j_session()
    session.execute_write(
        query="""
            MATCH (u:User {id: $user_id}), (m:Movie {id: $movie_id})
            MERGE (u)-[r:RATED]->(m)
            SET r.rate = $rate, r.comment = $comment
        """,
        parameters={
            "user_id": review['user_id'],
            "movie_id": review['movie_id'],
            "rate": review['rate'],
            "comment": review['comment']
        }
    )