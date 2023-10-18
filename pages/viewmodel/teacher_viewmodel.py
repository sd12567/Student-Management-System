from pages.service.teacher_service import teacher_service
from navigation import Navigation
from tkinter import StringVar

class teacher_viewmodel:
    def __init__(self,delegate_table_values):
        self.roll=StringVar()
        self.name=StringVar()
        self.dept=StringVar()
        self.year=StringVar()
        self.sem=StringVar()
        self.dob=StringVar()
        self.sgpa=StringVar()
        self.attend=StringVar()
        self.entry_status=StringVar()
        self.search_status=StringVar()
        self.current_id=''
        self.current_roll=''


        self.field_search_var=StringVar()
        self.search_menu=StringVar(value='Roll No.')

        self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
        self.delegate_table_values=delegate_table_values



    def refresh(self):
         self.field_search_var.set('')
         self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
         self.table_values.extend(teacher_service.get_table_values())
         self.delegate_table_values()
         self.search_status.set('')
         self.entry_status.set('')
         self.roll.set('')
         self.name.set('')
         self.sem.set('')
         self.attend.set('')
         self.dob.set('')
         self.year.set('')
         self.sgpa.set('')
         self.dept.set('')

    def table_row_clicked(self,data):
         if data['row']!=0:
              self.roll.set(self.table_values[data['row']][0])
              self.name.set(self.table_values[data['row']][1]) 
              self.dept.set(self.table_values[data['row']][2])
              self.year.set(self.table_values[data['row']][3])
              self.sem.set(self.table_values[data['row']][4])
              self.dob.set(self.table_values[data['row']][5])
              self.sgpa.set(self.table_values[data['row']][6])
              self.attend.set(self.table_values[data['row']][7])
              self.current_roll=self.table_values[data['row']][0]
              doc={'roll':self.roll.get(),
                    'name':self.name.get(),
                    'dept':self.dept.get(),
                    'year':self.year.get(),
                    'sem':self.sem.get(),
                    'dob':self.dob.get(),
                    'sgpa':self.sgpa.get(),
                    'attend':self.attend.get()}
              
              self.current_id=teacher_service.get_id(doc)




    def update(self):
        if self.all_fields_filled() :
                if self.current_roll==self.roll.get()  or teacher_service.unique_roll(self.roll.get()):
                    self.entry_status.set('')
                    doc={'roll':self.roll.get().upper(),
                        'name':self.name.get().title(),
                        'dept':self.dept.get().upper(),
                        'year':self.year.get().lower(),
                        'sem':self.sem.get().lower(),
                        'dob':self.dob.get(),
                        'sgpa':self.sgpa.get(),
                        'attend':self.attend.get()}
                    teacher_service.update(self.current_id,doc,self.current_roll)
                    self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
                    self.table_values.extend(teacher_service.get_table_values())
                    self.delegate_table_values()
                    self.roll.set('')
                    self.name.set('')
                    self.sem.set('')
                    self.attend.set('')
                    self.dob.set('')
                    self.year.set('')
                    self.sgpa.set('')
                    self.dept.set('')
                else:
                    self.entry_status.set('Roll exists')
             
        else:
              self.entry_status.set('Fill in all fields!')

    def delete(self):
         if self.all_fields_filled():
              self.entry_status.set('')
              teacher_service.delete(self.current_id)
              self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
              self.table_values.extend(teacher_service.get_table_values())
              self.delegate_table_values()
              self.roll.set('')
              self.name.set('')
              self.sem.set('')
              self.attend.set('')
              self.dob.set('')
              self.year.set('')
              self.sgpa.set('')
              self.dept.set('')
         else:
              self.entry_status.set('Fill in all fields!')



    def search(self):
     if self.field_search_var.get()!="":
         x=self.search_menu.get()
         if x=='Name':
              self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
              self.table_values.extend(teacher_service.get_student_by_name(self.field_search_var.get()))
              if len(self.table_values)!=1:
                   self.search_status.set('')
                   self.delegate_table_values()
                   self.field_search_var.set('')
              else:
                   print('Not found')
                   self.search_status.set('Not found')
                   self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
                   self.delegate_table_values()
         else:
              self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
              self.table_values.extend(teacher_service.get_student_by_roll(self.field_search_var.get()))
              if len(self.table_values)!=1:
                   self.search_status.set('')
                   self.delegate_table_values()
                   self.field_search_var.set('')
              else:
                   print('Not found')
                   self.search_status.set('Not found')
                   self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
                   self.delegate_table_values()
     else:
          self.search_status.set('Empty field!')

    def get_table_values(self):
         self.table_values.extend(teacher_service.get_table_values())
         self.delegate_table_values()

    def add(self):
        self.entry_status.set('')
        roll=self.roll.get().strip().upper()
        name=self.name.get().strip().title()
        dept=self.dept.get().strip().upper()
        year=self.year.get().strip().lower()
        sem=self.sem.get().strip().lower()
        dob=self.dob.get().strip()
        sgpa=self.sgpa.get().strip()
        attend=self.attend.get().strip()
        if self.all_fields_filled():
            if teacher_service.unique_roll(roll):
                doc={'roll':roll,
                    'name':name,
                    'dept':dept,
                    'year':year,
                    'sem':sem,
                    'dob':dob,
                    'sgpa':sgpa,
                    'attend':attend}
                teacher_service.add_doc(doc)
                self.table_values=[['ROLL NO','NAME','DEPARTMENT','YEAR','SEMESTER','DATE OF BIRTH','SGPA','ATTENDANCE']]
                self.table_values.extend(teacher_service.get_table_values())
                self.delegate_table_values()
                self.roll.set('')
                self.name.set('')
                self.sem.set('')
                self.attend.set('')
                self.dob.set('')
                self.year.set('')
                self.sgpa.set('')
                self.dept.set('')
            else:
                self.entry_status.set('Roll number already exists!!')
                print('Student with same Roll number exists')
        else:
             self.entry_status.set('Fill in all fields')
             print('Fill in all fields')
        
        


    def all_fields_filled(self):
            if (self.roll.get().strip()=='' or self.name.get().strip()=='' or self.dept.get().strip()=='' or self.year.get().strip()=='' or self.sem.get().strip()=='' or self.dob.get().strip()=='' or self.sgpa.get().strip()=='' or self.attend.get().strip()==''):
                 return False
            return True
        
        
