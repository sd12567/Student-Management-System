import customtkinter as ctk
from navigation import Navigation
from CTkTable import CTkTable
from pages.viewmodel.teacher_viewmodel import teacher_viewmodel


class StudentManagementApp(ctk.CTkToplevel):
    def __init__(self,x):
        super().__init__()
        self.view_model=teacher_viewmodel(self.update_table)
        title = "TEACHER'S PANE            "+str(x[0]) + ' (' + str(x[1])+')'
        self.title(title)
        self._set_appearance_mode("Dark")
        self.geometry('1900x830')
        self.minsize(1900,830)
        self.maxsize(1900,830)


        #1st frame of the teacher page:-

        self.frame = ctk.CTkFrame(self,width=500,height=750)
        self.frame.place(relx=0.0175,rely=0.035)


        #widgets in the teachers page:-

        self.roll_label = ctk.CTkLabel(self.frame,text = 'Roll No',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.roll_label.place(relx=0.02,rely=0.075)
        self.roll_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.roll)
        self.roll_entry.place(relx=0.255,rely=0.075)


        self.name_label = ctk.CTkLabel(self.frame,text = 'Name',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.name_label.place(relx=0.02,rely=0.175)
        self.name_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.name)
        self.name_entry.place(relx=0.255,rely=0.175)


        self.dept_label = ctk.CTkLabel(self.frame,text = 'Department',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.dept_label.place(relx=0.02,rely=0.275)
        self.dept_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.dept   )
        self.dept_entry.place(relx=0.255,rely=0.275)


        self.year_label = ctk.CTkLabel(self.frame,text = 'Year',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.year_label.place(relx=0.02,rely=0.375)
        self.year_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.year)
        self.year_entry.place(relx=0.255,rely=0.375)


        self.sem_label = ctk.CTkLabel(self.frame,text = 'Semester',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.sem_label.place(relx=0.02,rely=0.475)
        self.sem_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.sem)
        self.sem_entry.place(relx=0.255,rely=0.475)


        self.dob_label = ctk.CTkLabel(self.frame,text = 'DOB',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.dob_label.place(relx=0.02,rely=0.575)
        self.dob_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.dob)
        self.dob_entry.place(relx=0.255,rely=0.575)


        self.sgpa_label = ctk.CTkLabel(self.frame,text = 'SGPA',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.sgpa_label.place(relx=0.02,rely=0.675)
        self.sgpa_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.sgpa)
        self.sgpa_entry.place(relx=0.255,rely=0.675)


        self.attend_label = ctk.CTkLabel(self.frame,text = 'Attendance',corner_radius=10,width=50,height=35,font=("Century Gothic", 15, "bold"))
        self.attend_label.place(relx=0.02,rely=0.775)
        self.attend_entry = ctk.CTkEntry(self.frame,height=40,width=250,textvariable=self.view_model.attend)
        self.attend_entry.place(relx=0.255,rely=0.775)

        self.entry_status_label=ctk.CTkLabel(self.frame,textvariable=self.view_model.entry_status,text_color='red',font=('Arial', 10, 'bold'))
        self.entry_status_label.place(relx=0.255,rely=0.830)


        #button widgets in the teachers page:-

        self.add_button = ctk.CTkButton(self.frame,text='ADD',width=125,height=35,command=self.view_model.add)
        self.add_button.place(relx=0.045,rely=0.9)

        self.update_button = ctk.CTkButton(self.frame,text='UPDATE',width=125,height=35,command=self.view_model.update)
        self.update_button.place(relx=0.345,rely=0.9)

        self.del_button = ctk.CTkButton(self.frame,text='DELETE',width=125,height=35,command=self.view_model.delete)
        self.del_button.place(relx=0.645,rely=0.9)


            #2nd frame starts here for the search section:-

        self.frame2 = ctk.CTkFrame(self,width=1325,height=750)
        self.frame2.place(relx=0.29,rely=0.035)


        #widgets in the search section of teachers page:-

        self.search_label = ctk.CTkLabel(self.frame2,text='Search by ',corner_radius=10,width=100,height=15,font=("Century Gothic", 15, "bold"))
        self.search_label.place(relx=0.08,rely=0.11, anchor='center')

        self.optionmenu = ctk.CTkOptionMenu(self.frame2,values=['Name','Roll No.'],width=110,height=25,variable=self.view_model.search_menu)
        self.optionmenu.place(relx=0.135,rely=0.09)


        self.search_entry = ctk.CTkEntry(self.frame2,height=35,width=250,textvariable=self.view_model.field_search_var,corner_radius=5)
        self.search_entry.place(relx=0.375,rely=0.0865)

        self.search_status=ctk.CTkLabel(self.frame2,textvariable=self.view_model.search_status,text_color='red',font=('Arial', 10, 'bold'))
        self.search_status.place(relx=0.375,rely=0.136)

        self.search_button = ctk.CTkButton(self.frame2, text='Search',width=50,height=34,corner_radius=5,command=self.view_model.search)
        self.search_button.place(relx=0.565, rely=0.0865)
        self.search_entry.bind("<Return>", lambda event: self.on_enter_key_search(event))
        self.name_entry.bind("<Insert>",lambda event:self.on_insert_key(event))
        self.roll_entry.bind("<Insert>",lambda event:self.on_insert_key(event))
        self.year_entry.bind("<Insert>",lambda event:self.on_insert_key(event))
        self.sem_entry.bind("<Insert>",lambda event:self.on_insert_key(event))
        self.dept_entry.bind("<Insert>",lambda event:self.on_insert_key(event))
        self.sgpa_entry.bind("<Insert>",lambda event:self.on_insert_key(event))
        self.dept_entry.bind("<Insert>",lambda event:self.on_insert_key(event))
        self.attend_entry.bind("<Insert>",lambda event:self.on_insert_key(event))

        self.name_entry.bind("<Delete>",lambda event:self.on_del_key(event))
        self.roll_entry.bind("<Delete>",lambda event:self.on_del_key(event))
        self.year_entry.bind("<Delete>",lambda event:self.on_del_key(event))
        self.sem_entry.bind("<Delete>",lambda event:self.on_del_key(event))
        self.dept_entry.bind("<Delete>",lambda event:self.on_del_key(event))
        self.sgpa_entry.bind("<Delete>",lambda event:self.on_del_key(event))
        self.dept_entry.bind("<Delete>",lambda event:self.on_del_key(event))
        self.attend_entry.bind("<Delete>",lambda event:self.on_del_key(event))

        self.name_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        self.roll_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        self.year_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        self.sem_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        self.dept_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        self.sgpa_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        self.dept_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        self.attend_entry.bind("<Return>",lambda event:self.on_enter_key(event))
        
        #refresh button:-

        self.refresh_button = ctk.CTkButton(self.frame2,text='Refresh',width=120,height=35,command=self.view_model.refresh)
        self.refresh_button.place(relx=0.85,rely=0.025)


        #3rd frame for the teachers page table:-

        self.scrollable_frame = ctk.CTkScrollableFrame(self.frame2, width=1250, height=500)
        self.scrollable_frame.place(relx=0.02,rely=0.25)

       
        self.table = CTkTable( self.scrollable_frame,hover_color='gray',header_color='gray',values=self.view_model.table_values,command=(lambda data: self.view_model.table_row_clicked(data)))
        self.table.pack(expand=True, fill="both", padx=15, pady=15)
        self.table.bind('<Up>', lambda e: self.on_key(e, 0))
        self.table.bind('<Down>', lambda e: self.on_key(e, 0))

        self.protocol("WM_DELETE_WINDOW",self.on_close)
        self.bind('<Control-c>',lambda event:self.on_close(event))
        self.view_model.get_table_values()

    
    def update_table(self):
        self.table.destroy()
        self.table = CTkTable( self.scrollable_frame,header_color='gray',hover_color='white',values=self.view_model.table_values,command=(lambda data: self.view_model.table_row_clicked(data)))
        self.table.pack(expand=True, fill="both", padx=15, pady=15)
        # self.table.bind('<Up>', lambda e: self.on_key(e, 0))
        # self.table.bind('<Down>', lambda e: self.on_key(e, 0))

    def on_close(self,event=None):
            self.destroy()
            Navigation.pages['teacher_view']=None

    def on_enter_key_search(self,event):
        self.search_button.invoke() 

    def on_insert_key(self,event):
         self.add_button.invoke()

    def on_del_key(self,event):
         self.del_button.invoke()
    
    def on_enter_key(self,event):
         self.update_button.invoke()


    # def on_key(self,event, current_row):
    #     if event.keysym == 'Down' and current_row < len(self.view_model.table_values) - 1:
    #         current_row += 1
    #         self.table.select_row(current_row)
    #     elif event.keysym == 'Up' and current_row > 0:
    #         current_row -= 1
    #         self.table.select_row(current_row)

 
