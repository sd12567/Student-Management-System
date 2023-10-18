import customtkinter as ctk
from CTkTable import CTkTable
from navigation import Navigation

class StudentView(ctk.CTkToplevel):
    def __init__(self,x=None):
        super().__init__()
        if x:
            title="Student's Pane - "+str(x[1])+" ("+str(x[0])+")"
            self.title(title)
        else:
            self.title('No Record Found')
        self.maxsize(950, 550)
        self.geometry('450x550')
        self.minsize(450,550)
        self.frame = ctk.CTkFrame(self, width=400, height=480)
        self.frame.place(relx=0.05, rely=0.05)

        self.label = ctk.CTkLabel(self.frame, text='STUDENT DETAILS PAGE', font=('Century Gothic', 16,'underline','bold'))
        self.label.place(relx=0.5, rely=0.1,anchor='center')

        if x:
            value=[['Name',str(x[1])],['Roll No.',str(x[0])],
                   ['Department',str(x[2])],['Year',str(x[3])],
                   ['Semester',str(x[4])],['Date of Birth',str(x[5])],
                   ['SGPA',str(x[6])],['Attendance',str(x[7])]]

            self.table=CTkTable(self.frame,row=8,column=2,values=value,font=('Century Gothic',14),orientation='horizontal')
            self.table.place(relx=0.5,rely=0.5,anchor='center')
        else:
            l=ctk.CTkLabel(self.frame,text='NO RECORD EXISTS',font=('Century Gothic',16))
            l.place(relx=0.5,rely=0.5,anchor="center")
        
        self.close_button = ctk.CTkButton(self.frame,text='Close',width=80,font=("Century Gothic", 10, "bold"),command=self.close)
        self.close_button.place(relx=0.5,rely=0.85,anchor='center')

        self.bind('<Control-c>',(lambda event: self.close(event)))

        self.protocol("WM_DELETE_WINDOW",self.close)


    def close(self,event=None):
        self.destroy()
        Navigation.pages['student_view']=None


