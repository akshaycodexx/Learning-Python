#file Handling......


'''
#reading the file 


f=open('myfile.txt','r')
# print(f)
text=f.read()
f.close()
print(text)

'''

#writing a file

f=open('myfile.txt','w')
f.write(" hey how are you! ")
f.close()

with open('myfile.txt','a') as f:
    f.write("Hey i am Akshay")




