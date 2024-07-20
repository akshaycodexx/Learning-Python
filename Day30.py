# Recursions

#factorial

'''
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
    
print(f"The factorial of 5 is {fact(5)}")

'''

#fibonachi

def fibo(n):
    if(n==0):
        return 0
    elif n==1:
        return 1
    else:
      return fibo(n-1)+fibo(n-2)
  
n=int(input("Enter the number\n"))

print(fibo(n))
for i in range(1,n):
    print(f"Fibonachi of {i}: {fibo(i)}")













