# decorators are the function ,those function chnage the other function Asap
# how @ symbol in python]


def greet(fx):
    def mxf():
        print("Good Morning!")# function fun hone ke pahle print karega(like: Hadder)
        fx()# ye ek seprator hai jo function ke call honbe ke bad run hoga (like: footer)
        print("Thanks for using this function")
    return mxf
    


@greet
def hello():
    print("hello World")

hello()

