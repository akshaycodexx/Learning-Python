# function Argument and return statement


'''def Avg(a,b):
    print("the avg is ",(a+b)/2)



Avg(2,5)
'''
'''
def Avg(*Numbers):
    sum=0
    for i in Numbers:
        sum=sum+i
    print("Avg is :",sum/len(Numbers))
        


Avg(5,6)

'''


def name(**name):
    print("Hellow, ",name["fname"],name['mname'],name['lname'])
    
    
    
    
name(fname="Akshay",mname="Kumar",lname="Mandal")

def Add(a,b):
    return a+b

c=Add(3,4)

print(c)


















