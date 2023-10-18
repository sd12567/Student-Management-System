from pymongo import MongoClient 
from pymongo.database import Database 
from pymongo.collection import Collection

class DatabaseClient:
    client=None
    db=None
    collections=None

    @classmethod
    def init_client(cls,db_url,db_port,db_name):
        cls.client=MongoClient(db_url,db_port)
        cls.db=cls.client[db_name]
        cls.collections=dict()
    
    @classmethod
    def add_collection(cls,collection_name):
        cls.collections[collection_name]=cls.db[collection_name]
    
    @classmethod
    def close(cls):
        cls.client.close()
