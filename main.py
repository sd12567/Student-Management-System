from service_db import DatabaseClient
from navigation import Navigation
from pages.view.login_view import login_view


if __name__ == "__main__":
    DatabaseClient.init_client('mongodb+srv://admin:1979@aws-prod.sm2rtye.mongodb.net/',27017,'students_db')
    DatabaseClient.add_collection('t_reg')  #  teachers'  registration details
    DatabaseClient.add_collection('s_reg')  #  students' registration details
    DatabaseClient.add_collection('s_details') # students' documents 

    Navigation.add_root_page( login_view())
    # Navigation.add_page('teacher_view',StudentManagementApp())
    Navigation.run_app()
    DatabaseClient.close()
