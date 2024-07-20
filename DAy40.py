#secret Code
import random

S=['A','B','C','D','E','F','G','H','I','J','K','L','M','N']

a=input("Enter the Word as You want:  ")
if(len(a)<3):
    print(a[::-1])
else:
    rev=a[1:]+a[0]
    
    x=random.choice(S)+random.choice(S)+random.choice(S)+rev+random.choice(S)+random.choice(S)+random.choice(S)
    print(f"Your Secret Code is : {x}")
       
       
    print()

































