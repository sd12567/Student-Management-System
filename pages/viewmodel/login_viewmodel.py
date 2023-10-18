from pages.service.login_service import login_service
from pages.view.teacher_view import StudentManagementApp
from pages.view.student_view import StudentView
from navigation import Navigation
from tkinter import StringVar


class login_viewmodel:
    def __init__(self):
     self.name_signup=StringVar()
     self.id_signup=StringVar()
     self.user_signup=StringVar()
     self.pwd_signup=StringVar()
     self.user_signin=StringVar()
     self.pwd_signin=StringVar()

     self.signin_status=StringVar()
     self.signup_status=StringVar()

     self.signin_menu=StringVar(value='Teacher')
     self.signup_menu=StringVar(value='Teacher')

     


    def register(self):
     
       v=self.signup_menu.get()
       if v=='Teacher':
         name=self.name_signup.get().strip().title()
         id=self.id_signup.get().upper().strip()
         user=self.user_signup.get().strip()
         pwd=self.pwd_signup.get().strip()
         self.signup_status.set("")
         if self.valid_regdetails(name,id,user,pwd):
            if self.valid_pass():
               if self.uteacher_isvalid():
                if  login_service.unique(id):   
                  doc={'name':name,'id':id,'user':user,'pwd':pwd}
                  login_service.add_doc_teacher(doc)
                  self.name_signup.set('')
                  self.id_signup.set('')
                  self.user_signup.set('')
                  self.pwd_signup.set('')
                  self.signup_status.set('Registered Succesfully!')
                else:
                  self.signup_status.set('ID already exists.Cannot register')
               else:
                  self.signup_status.set("same username exists.Cannot register")
            else:
               self.signup_status.set('Password should be atleast 4 characters')         
         else:
            self.signup_status.set('fill in all fields to register')

       else:
         name=self.name_signup.get().strip().title()
         roll=self.id_signup.get().upper().strip().upper()
         user=self.user_signup.get().strip()
         pwd=self.pwd_signup.get().strip()
         self.signup_status.set("")
         if self.valid_regdetails(name,roll,user,pwd):
          if self.valid_pass():
            if self.ustudent_isvalid():
               if login_service.unique_roll(roll):
                  doc={'name':name,'roll':roll,'user':user,'pwd':pwd}
                  login_service.add_doc_student(doc)
                  self.name_signup.set('')
                  self.id_signup.set('')
                  self.user_signup.set('')
                  self.pwd_signup.set('')
                  self.signup_status.set('Registered Succesfully!')
               else:
                  self.signup_status.set('account with same id exists.Cannot register')
            else:
                  self.signup_status.set("same username exists.Cannot register")
          else:
             self.signup_status.set('Password should be atleast')
         else:
            self.signup_status.set('fill in all fields to register')
       
    def signin(self):
       
       v=self.signin_menu.get()
       if v=='Teacher':
         self.signin_status.set('')
         user=self.user_signin.get().strip()
         pwd=self.pwd_signin.get()
         
         query={'user':user,'pwd':pwd}
         if self.no_mt_sign():
            if len(self.pwd_signin.get())>=4:
               if login_service.cred_valid_teacher(query):
                  if Navigation.pages.get('teacher_view')==None:
                     Navigation.add_page('teacher_view',StudentManagementApp(login_service.get_name(query)))
                     self.user_signin.set('')
                     self.pwd_signin.set('')
                  #  self.open_page()
               else:
                  self.signin_status.set('Account not registered')
            else:
               self.signin_status.set('Password should be atleast 4 characters')
         else:
            self.signin_status.set('Fill in all fields')
       else:
         self.signin_status.set('')
         user=self.user_signin.get().strip()
         pwd=self.pwd_signin.get()

         query={'user':user,'pwd':pwd}
         if self.no_mt_sign():
            if login_service.cred_valid_student(query):
               if Navigation.pages.get('student_view')==None:
                  x=login_service.find_student_record(query)
                  Navigation.add_page('student_view',StudentView(x))
                  self.user_signin.set('')
                  self.pwd_signin.set('')
                  self.signin_status.set('')
            else:
                   self.signin_status.set('User does not exist')
         else:
               self.signin_status.set('Fill in all fields')

    def valid_pass(self):
       return len(self.pwd_signup.get())>=4
         
    def valid_regdetails(self,n,i,u,p):
         if (n=="") or (i=="") or (u=="") or (p==""):
               return False
         return True

    def uteacher_isvalid(self):
      u=self.user_signup.get()
      query={'user':u}
      if login_service.cred_valid_teacher(query):
         return False
      return True
    
    def ustudent_isvalid(self):
      u=self.user_signup.get()
      query={'user':u}
      if login_service.cred_valid_student(query):
         return False
      return True
    
    def no_mt_sign(self):
       p=self.pwd_signin.get()
       u=self.user_signin.get()
       if p=="" or u=="":
          return False
       else:
          return True
              
    def reset_signin_status(self):
       self.signin_status.set('')

    


