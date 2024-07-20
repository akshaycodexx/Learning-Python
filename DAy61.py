#inheritance: it is the very importtant features of oops that inherite the some properitys of other base class

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"The name of Employee: {self.id } is {self.name}")

class programmer(Employee):
    def showlanguage(self):
        print("the default langyuage is python")
    
    
    
    
    
    
        
e=Employee("Akshay",14)
e2=programmer("Lavish",12)
e2.showdetails()
e.showdetails()      

        
        
        
        
        
        
        
        
        