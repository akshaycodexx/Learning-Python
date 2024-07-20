#class methid and alternatives Constractors


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
        
#make a instance
e=Employee("Harry",1200)
print(e.name)
print(e.salary)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def from_string(cls,string):
        name,age=string.split(',')
        return cls(name,int(age))
    
Person=person.from_string("jhon sena,30")
print(Person.name, Person.age)


