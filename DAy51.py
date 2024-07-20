# seek and tell
# with open('myfile2.txt','r') as f:
#     print(f)
    
    
#     f.seek(10)
#     print(f.tell())
#     data=f.read(5)
#     print(data)







#truncate:
with open('myfile2.txt','w') as f:
    f.write("Hellow , World!")
    f.truncate(5)
    
with open('myfile2.txt','r') as f:
    print(f.read())