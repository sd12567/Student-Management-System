from service_db import DatabaseClient
from bson.objectid import ObjectId


class teacher_service:

    @classmethod
    def add_doc(self,doc:dict):
        DatabaseClient.collections['s_details'].insert_one(doc)

    @classmethod
    def unique_roll(self,roll:str):
        query={'roll':roll}
        doc=DatabaseClient.collections['s_details'].find_one(query)
        if doc:
            return False
        return True
    
    @classmethod
    def get_table_values(self):
        docs=DatabaseClient.collections['s_details'].find({}).sort('roll')
        doc_list=[]
        for doc in docs:
            doc_list.append([doc['roll'],doc['name'],doc['dept'],doc['year'],doc['sem'],doc['dob'],doc['sgpa'],doc['attend']])
        return doc_list
    

    @classmethod
    def get_student_by_name(self,name:str):
        docs=DatabaseClient.collections['s_details'].find({'name':{'$regex':name,'$options':'i'}})
        doc_list=[]
        for doc in docs:
            doc_list.append([doc['roll'],doc['name'],doc['dept'],doc['year'],doc['sem'],doc['dob'],doc['sgpa'],doc['attend']])
        return doc_list
    
    @classmethod
    def get_student_by_roll(self,roll:str):
        docs=DatabaseClient.collections['s_details'].find({'roll':{'$regex':roll,'$options':'i'}})
        doc_list=[]
        for doc in docs:
            doc_list.append([doc['roll'],doc['name'],doc['dept'],doc['year'],doc['sem'],doc['dob'],doc['sgpa'],doc['attend']])
        return doc_list
    
    @classmethod
    def get_id(self,doc:dict):
        doc=DatabaseClient.collections['s_details'].find_one(doc)
        if doc:
            return str(doc['_id'])        

    @classmethod
    def update(self,id:str,doc:dict,roll:str):
        DatabaseClient.collections['s_details'].update_one({'_id':ObjectId(id),'roll':roll},{'$set':doc})


    @classmethod
    def delete(self,id):
        DatabaseClient.collections['s_details'].delete_one({'_id':ObjectId(id)})