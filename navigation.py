from customtkinter import CTkToplevel
class Navigation:
    pages=None

    @classmethod
    def add_root_page(cls,page):
        if cls.pages is None:
            cls.pages={}
        cls.pages['/']=page


    @classmethod
    def get_root_page(cls):
        return cls.pages['/']

    @classmethod
    def add_page(cls,name,page:CTkToplevel):
        if cls.pages is None:
            cls.pages={}
        
        # page.withdraw()
        cls.pages[name]=page
        cls.pages[name].deiconify()
        cls.pages[name].focus()
        cls.pages[name].grab_set()
        # cls.pages[name].withdraw()

    @classmethod
    def run_app(cls):
        cls.pages['/'].mainloop()

    @classmethod
    def open_page(cls,name:str):
        cls.pages[name].deiconify()
        cls.pages[name].focus()
        cls.pages[name].grab_set()