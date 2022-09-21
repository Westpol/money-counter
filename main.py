import json
import count_money
import add_to_balance

coins = '{"twoeuro":0, "oneeuro":0, "fiftycent":0, "twentycent":0, "tencent":0, "fivecent":0, "twocent":0, "onecent":0}'
paper = '{"fiveeuro":0, "teneuro":0, "twentyeuro":0, "fiftyeuro":0, "onehundredeuro":0, "twohundrereuro":0, "fivehundrereuro":0}'

jsoncoins = json.loads(coins)
jsonpaper = json.loads(paper)

jsoncoins["oneeuro"] = 3

print(jsoncoins["oneeuro"])

while 1:
    mode = input("What do you want to do?\n 1: Count money from 0€\n 2: Add to your current balance")
    if mode.isdigit():
        mode = int(mode)
        if mode == 1:
            count_money.count_the_money()
        elif mode == 2:
            add_to_balance.add_the_balance()
    else:
        print("Wrong Input you Cocksucker")

