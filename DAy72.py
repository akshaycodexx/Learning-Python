#supper keywords:

'''

A supper keyword in pythoon is used to refer to the parrent class.
It is especially useful when a classs inherites from multiple parent classes and you want to call a method fromone of the parent classws


'''
'''

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")
class Childclass(ParentClass):
    def  parent_method(self):
        print("Akshay")
    def child_method(self):
        print("This is the Child Method.")
        
        super().parent_method()


child_object=Childclass()
child_object.child_method()
child_object.parent_method()


'''



class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class Programmer(Employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language

Akshay=Employee("Akshay",123)
print(Akshay.name)
















