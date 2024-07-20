#constractors:


class person:
    #type parameter only self is known as default constractor
    def __init__(self,n,o):
       self.name=n
       self.occuption=o
       
    # name="Akshay"
    # occuption="Software Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occuption}")

a=person("Akshay","Alsi Developer")
a.info()