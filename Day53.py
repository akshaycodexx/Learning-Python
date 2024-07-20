#map , filter , reduce :
from functools import reduce
l=[1,2,3,4,5]
# new=[]

# for i in l:
#     new.append(i**2)

# print(new)

def cube(x):
    return x*x*x

new=list(map(cube,l))
# print(new)

# filter
def filter_function(a):
    return a>4

newl=list(filter(filter_function,l))
print(newl)












