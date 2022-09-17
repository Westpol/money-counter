import json
from count_money import count_the_money
import add_to_balance

while 1:
    mode = input("What do you want to do?\n 1: Count money from 0€\n 2: Add to your current balance")
    if mode.isdigit():
        if mode == 1:
            count_the_money()
        elif mode == 2:
            add_to_balance.add_the_balance()
    else:
        print("Wrong Input you Cocksucker")

