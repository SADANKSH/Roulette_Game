import random

RED=[]
BLACK=[]


for i in range(1,101):
    if i%2==0:
        RED.append(i)
    else:
        BLACK.append(i)


def deposit():
    amount=(input("Enter the amount to deposit: "))
    if amount.isdigit():
        amount=int(amount)
    else:
        print("Invalid amount")
    return amount


def bet_style():
    multiplier =1
    style=input("Enter your bet style: ")
    if  style.lower()=="low":
        multiplier =0.5
    elif style.lower()=="high":
        multiplier =1.5
    else:
        print("Invalid bet style")
    return multiplier


def place_bet(balance):
    bet=input("Enter your bet: ")
    if bet.isdigit():
        bet=int(bet)
        if 0<bet<=balance:
            pass
        elif bet>balance:
            print("Not enough balance")
        else:
            print("Invalid bet")
    else:
        print("Invalid bet")
    return bet

def dice_roll():
    return random.randint(1,6)

def roulette_spin():
   choice = random.randint(1,2)
   if choice==1:
       return random.choice(RED)
   else:
       return random.choice(BLACK)


def game():
    balance = deposit()
    while balance>0:
        bet=place_bet(balance)
        multiplier=bet_style()
        balance-=bet
        roll=dice_roll()
        spin=roulette_spin()
        print(f"You rolled a {roll} and the spin is {spin}")

if __name__=="__main__":
    game()
