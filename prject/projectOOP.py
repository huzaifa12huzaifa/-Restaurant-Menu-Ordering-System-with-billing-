class Name:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        return f">>>>>>>>>>>> Welcome To <<<<<<<<<<<<<<\n{self.name}"
name= "****************************** \n*       Taste Junction       *\n******************************"
restaurent_name =Name(name)



class Menu(Name):
    def __init__(self,name,menu):
        Name.__init__(self,name)
        self.menu = menu
    def starter(self):
        pass
menu= "Menu of the restaurent"
ob=Menu(name,menu)
print(ob.print_name())
