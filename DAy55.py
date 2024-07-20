#snake Water Gun
import math
import random

select_Options=["Snake","Water","Gun"]

usser=input("S-Sname , W-Water ,G-Gun")

ans=random.choice(select_Options)

def game(usser,ans):
    if((usser=='S' or 's' or "Snake" or "snake")==(ans=="Gun")):
        print("congratulations! you win")














