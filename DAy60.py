#getters and Setters:
# ek function ke return value ko ek object ke trah treet kar sakte ho

class myclass:
    def __init__(self,value):
        self._value =value
        
    def show(self):
        print(f"value is {self._value}")
        
    #getter 
    @property
    def ten_value(self):
        return 10*self._value
    #setter
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
        
    
    
    

    
obj=myclass(10)
 #use setter
obj.ten_value=67  
 
obj.show()
print(obj.ten_value)