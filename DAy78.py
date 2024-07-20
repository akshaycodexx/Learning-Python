#single inheritsnce



class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"Hii my name is {self.name} and my age is {self.age}")


class child(parent):
    def __init__(self,name,age,child):
        super().__init__(name,age)
        self.child=child
        
# P1=parent("Akshay",21)
# P1.show()

c1=child("Akshay",91,"binod")
c1.show()
        
        



















