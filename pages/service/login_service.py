from service_db import DatabaseClient
from bson.objectid import ObjectId

class login_service:

    @classmethod
    def add_doc_teacher(cls,doc:dict):
        DatabaseClient.collections['t_reg'].insert_one(doc)

    @classmethod
    def unique(cls,id:str):
        doc =DatabaseClient.collections['t_reg'].find_one({'id':id})
        return not doc
    
    @classmethod
    def cred_valid_teacher(cls,q):
        doc=DatabaseClient.collections['t_reg'].find_one(q)
        return True if doc else False

    @classmethod
    def get_name(cls,q):
        doc=DatabaseClient.collections['t_reg'].find_one(q)
        return doc['name'],doc['user']
    

    #STUDENT SERVICE FUNCTIONS

    @classmethod
    def unique_roll(cls,roll:str):
        doc=DatabaseClient.collections['s_reg'].find_one({'roll':roll})
        return not doc
    
    @classmethod
    def add_doc_student(cls,doc:dict):
        DatabaseClient.collections['s_reg'].insert_one(doc)


    @classmethod
    def cred_valid_student(cls,q):
        doc=DatabaseClient.collections['s_reg'].find_one(q)
        return True if doc else False


    @classmethod
    def find_student_record(cls,query):
        doc=DatabaseClient.collections['s_reg'].find_one(query)
        name=doc['name']
        roll=doc['roll']
        query2={'name':name,'roll':doc['roll']}
        doc=DatabaseClient.collections['s_details'].find_one(query2)
        if doc is not None:
            return doc['roll'],doc['name'],doc['dept'],doc['year'],doc['sem'],doc['dob'],doc['sgpa'],doc['attend']

