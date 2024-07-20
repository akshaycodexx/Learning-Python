# method overriding; prent class me method ko inherit karna child class me or uska soubhaw  change kar dena 

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def area(self):
        return self.x * self.y

class circle(Shape):
    def __init__(self,radii):
        self.radii=radii
        super().__init__(radii,radii)
        
    def area(self):
        return 3.14 * super().area()
    
c=circle(5)
print(c.area())