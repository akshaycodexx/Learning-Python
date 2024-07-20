#Access Modifiers:no available in python

class Employee:
    def __init__(self) :
        self.__name="AKshay"
        
        
a=Employee()
# print(a.__name)--cannot Access Directly
print(a._Employee__name)#but ACCESSin direclty
        
    