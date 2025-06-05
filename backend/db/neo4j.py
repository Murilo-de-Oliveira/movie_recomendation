import logging
from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError

logging.basicConfig(level=logging.INFO)

class Database:
    def __init__(self, uri="bolt://44.201.242.161:7687", user="neo4j", password="casualties-insignia-tensions"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
        
    def execute_write(self, query, parameters=None):
        logging.info(f"[WRITE] {query} | Params: {parameters}")
        try:
            with self.driver.session() as session:
                return session.execute_write(
                    lambda tx: tx.run(query, parameters).data()
                )
        except Neo4jError as e:
            logging.error(f"[ERROR] {e}")
            return []
        
    def execute_read(self, query, parameters=None):
        logging.info(f"[READ] {query} | Params: {parameters}")
        try:
            with self.driver.session() as session:
                return session.execute_read(
                    lambda tx: tx.run(query, parameters).data()
                )
        except Neo4jError as e:
            logging.error(f"[ERROR] {e}")
            return []
        
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")   