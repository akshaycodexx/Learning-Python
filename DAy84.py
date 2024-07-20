#TIme Module

import time
t=time.localtime()
def oo():
    for i in range(5):
        time.sleep(2)
        print("helloe")
        

init=time.time()
oo()
print(time.time()-init)
print(time.strftime("%H:%M:%S",t))














