#math case stattement ----
x=int(input("enter the value of x:"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case 45:
        print("x is 45")
    case _:
        print("this is the difult case")
    