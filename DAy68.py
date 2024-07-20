#Os module 
import os
os.rename('myfile',"myfile.txt")

files=os.listdir('myfile.txt')

for i in files:
   if i.endswith(".png"):
       print(i)
       