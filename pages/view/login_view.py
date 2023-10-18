import customtkinter as ctk
from pages.viewmodel.login_viewmodel import login_viewmodel
class login_view(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.view_model=login_viewmodel()
        self.title("Student Management App")
        self.geometry('450x500')
        # self.minsize(400,500)
        self.resizable(False,False)
        self.frame = ctk.CTkFrame(self, width=450, height=500)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        

        #tab forming:-

        self.tabview = ctk.CTkTabview(self.frame,width=350,height=450)
        self.tabview.pack(padx=20, pady=20)

        self.tabview.add("SIGN IN")
        self.tabview.add("SIGN UP")
        self.tabview.set("SIGN IN")

        self.b1=ctk.CTkButton(self.tabview.tab("SIGN IN"))
        #sign in tab's all functions:-

        self.heading_label = ctk.CTkLabel(self.tabview.tab("SIGN IN"), text='Sign In ', font=('Arial', 28,'bold'))
        self.heading_label.place(relx=0.5, rely=0.1, anchor='center')

        self.signin_dom_label = ctk.CTkLabel(self.tabview.tab("SIGN IN"), text='Sign in as', width=80, height=100, font=('Arial',19,'bold','italic'))
        self.signin_dom_label.place(relx=0.1, rely=0.128)


        self.signin_menu = ctk.CTkOptionMenu(self.tabview.tab("SIGN IN"), values=['Teacher', 'Student'], width=130, height=20,variable=self.view_model.signin_menu)
        self.signin_menu.place(relx=0.45, rely=0.227)


        self.username_label = ctk.CTkLabel(self.tabview.tab("SIGN IN"),text = 'Username:',font=('Arial', 16,'bold'))
        self.username_label.place(relx=0.1,rely=0.415)
        self.usersignin_entry = ctk.CTkEntry(self.tabview.tab("SIGN IN"), height=30, width=160,textvariable=self.view_model.user_signin)
        self.usersignin_entry.place(relx=0.435, rely=0.405)

        self.pwdsignin_label = ctk.CTkLabel(self.tabview.tab("SIGN IN"), text='Password:', font=('Arial', 16, 'bold'))
        self.pwdsignin_label.place(relx=0.1, rely=0.515)
        self.pwdsignin_entry = ctk.CTkEntry(self.tabview.tab("SIGN IN"), height=30, width=160,show='*',textvariable=self.view_model.pwd_signin)
        self.pwdsignin_entry.place(relx=0.435, rely=0.505)
        self.signinstatus=ctk.CTkLabel(self.tabview.tab("SIGN IN"),textvariable=self.view_model.signin_status,font=('Arial', 9.4, 'bold'),text_color="red")
        self.signinstatus.place(relx=0.435,rely=0.58)


        # self.signinstatus.bind("<Return>",lambda event: self.on_esc_clicked(event))
       
        
        # sign in button:-

        self.signin_button = ctk.CTkButton(self.tabview.tab("SIGN IN"),text='Sign in',width=135,height=40,command=self.view_model.signin)
        self.signin_button.place(relx=0.5,rely=0.75,anchor='center')

        self.pwdsignin_entry.bind("<Return>", lambda event: self.on_enter_key_signin(event))
        self.usersignin_entry.bind("<Return>", lambda event: self.on_enter_key_signin(event))

        #sign up tab functions:-

        self.heading_label = ctk.CTkLabel(self.tabview.tab("SIGN UP"), text='Sign up ',font=('Arial', 28,  'bold'))
        self.heading_label.place(relx=0.5, rely=0.09, anchor='center')

        self.signup_dom_label = ctk.CTkLabel(self.tabview.tab("SIGN UP"), text='Sign up as', width=40, height=40,font=('Arial', 19, 'bold','italic'))
        self.signup_dom_label.place(relx=0.1, rely=0.171)
        self.signup_menu = ctk.CTkOptionMenu(self.tabview.tab("SIGN UP"), values=['Teacher', 'Student'], width=130,height=20,variable=self.view_model.signup_menu)
        self.signup_menu.place(relx=0.45, rely=0.195)

        self.name_label = ctk.CTkLabel(self.tabview.tab("SIGN UP"), text='Name:',font=('Arial', 16, 'bold'))
        self.name_label.place(relx=0.1, rely=0.345)
        self.name_entry = ctk.CTkEntry(self.tabview.tab("SIGN UP"), height=30, width=160,textvariable=self.view_model.name_signup)
        self.name_entry.place(relx=0.435, rely=0.335)

        self.id_label = ctk.CTkLabel(self.tabview.tab("SIGN UP"), text='ID/Roll no:', font=('Arial', 16, 'bold'))
        self.id_label.place(relx=0.1, rely=0.445)
        self.id_entry = ctk.CTkEntry(self.tabview.tab("SIGN UP"), height=30, width=160,textvariable=self.view_model.id_signup)
        self.id_entry.place(relx=0.435, rely=0.435)

        self.username_label = ctk.CTkLabel(self.tabview.tab("SIGN UP"), text='Username:', font=('Arial', 16, 'bold'))
        self.username_label.place(relx=0.1, rely=0.545)
        self.usersignup_entry = ctk.CTkEntry(self.tabview.tab("SIGN UP"), height=30, width=160,textvariable=self.view_model.user_signup)
        self.usersignup_entry.place(relx=0.435, rely=0.535)

        self.password_label = ctk.CTkLabel(self.tabview.tab("SIGN UP"), text='Password:', font=('Arial', 16, 'bold'))
        self.password_label.place(relx=0.1, rely=0.645)
        self.pwdsignup_entry = ctk.CTkEntry(self.tabview.tab("SIGN UP"), height=30, width=160,textvariable=self.view_model.pwd_signup)
        self.pwdsignup_entry.place(relx=0.435, rely=0.635)

        self.signupstatus=ctk.CTkLabel(self.tabview.tab("SIGN UP"),textvariable=self.view_model.signup_status,font=('Arial', 9.4, 'bold'),text_color="red")
        self.signupstatus.place(relx=0.435,rely=0.715)

        
        #sign up button:-

        self.signup_button = ctk.CTkButton(self.tabview.tab("SIGN UP"), text='Sign up', width=135, height=40,command=self.view_model.register)
        self.signup_button.place(relx=0.5, rely=0.875, anchor='center')

        self.pwdsignup_entry.bind("<Return>", lambda event: self.on_enter_key_signup(event))
        self.usersignup_entry.bind("<Return>", lambda event: self.on_enter_key_signup(event))
        self.name_entry.bind("<Return>", lambda event: self.on_enter_key_signup(event))
        self.id_entry.bind("<Return>", lambda event: self.on_enter_key_signup(event))

        self.bind('<Control-c>',lambda event: self.delete(event))


    def delete(self,event):
        self.destroy()

    def on_enter_key_signup(self,event):
        self.signup_button.invoke()

       
    def on_enter_key_signin(self,event):
        self.signin_button.invoke()

    def on_esc_clicked(self,event):
        self.view_model.reset_signin_status()

