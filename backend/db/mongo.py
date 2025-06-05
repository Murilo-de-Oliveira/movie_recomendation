import pymongo # pip install pymongo

class Database:
    def __init__(self, connection_string="mongodb://localhost:27017"):
        try:
            self.client = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )
            print("Conectado ao MongoDB com sucesso!")
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            raise

    def get_collection(self, database, collection):
        db = self.client[database]
        return db[collection]

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

