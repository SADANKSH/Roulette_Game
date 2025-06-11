# Impoorting Random  Module to grnerate choices and numbers
import random

# Initializong Empty list to store numbers in two categories(Red and Black)
RED=[]
BLACK=[]


# Adding EVEN numbers to the Red list and ODD numbers to the Black List
for i in range(1,101):
    if i%2==0:
        RED.append(i)
    else:
        BLACK.append(i)


# Function to take deposit from the Player
def deposit():
    while True:
        amount=(input("Enter the amount to deposit: "))
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Invalid amount")

    return amount


# Function to update the wallet balance after every activity.
def update_balance(balance,bet,winnings):
    if winnings>0:
        balance=balance-bet+winnings
    else:
        balance=balance-bet
    return balance


# Function to withdraw the balance
def withdraw(balance):
    choice=input("Do you want to withdraw? (y/n): ")
    if choice.lower()=="y":
        while True:
            amount=input("Enter the amount to withdraw: ")
            if amount.isdigit():
                amount=int(amount)
                if amount<=balance:
                    balance=balance-amount
                    print(f"You withdrew ${amount}")
                    break
                else:
                    print("Insufficient balance")
    else:
        print("You are not withdrawing")
    return balance


# Function to set the Multiplier based on the Player's choice of the betting range
def bet_style():
    multiplier =1
    while True:
        style=input("Enter your bet style: ")
        if  style.lower()=="low":
            multiplier =1.5
        elif style.lower()=="high":
            multiplier =3
        else:
            print("Invalid bet style")
            bet_style()
        return multiplier


# Function to set the num that player choosess to play bet on
def get_number():
    while True:
        num=input("Enter the number: ")
        if num.isdigit():
            num=int(num)
            break
        else:
            print("Invalid number")

    return num


# Function to take the Bet Amount from the Player and cross examine it with the current wallet balance.
def place_bet(balance):
    while True:
        bet=input("Enter your bet: ")
        if bet.isdigit():
            bet=int(bet)
            if 0<bet<=balance:
                break
            elif bet>balance:
                print("Not enough balance")

        else:
            print("Invalid bet")

    return bet


# Function to Roll the Dice randomly using the Random Module imported above
def dice_roll():
    return random.randint(1,6)


# Function to spin the Roulette using the Random Module.
def roulette_spin():
#    It first selects a choice randomly choosing between Red and Black and then choosing a number randomly from that list.
   choice = random.randint(1,2)
   if choice==1:
       return random.choice(RED)
   else:
       return random.choice(BLACK)


# Function to set the Rules for the winning conditions and calculating the winnings.
def winning_conditions(bet,multiplier,roll,spin,num,balance):
    winnings=0
    # If the dice roll is 1 or 6 the player has already lost. No need for the spin.
    while roll != 1 or roll != 6:
        # If the dice spin is not 1 or 6 then if he has choosen low style betting the multiplier is 0.5x and the number in the  spin should be less than the number he chose.
        if multiplier==1.5 and num>=spin:
            winnings = bet*multiplier
            break
        # If he chose high style for the betting the multiplier is 1.5x and the number in the spin should be more than the number he chose.
        elif multiplier==3 and num<=spin:
            winnings = bet*multiplier
            break
        # If the Dice Roll is 1 or 6 and the spin is 0, this calls for a Double Bet fromt eh Dealer.If the player fails to meet he losses.
        elif spin==0 and roll ==1 or spin==0 and roll ==6:
            bet = bet*2
            if bet>balance:
                print("You lost all your money")
                break
        else:
            print("You lost")
            break
    if roll ==1 or roll ==6:
        winnings = 0
        print("You lost")
    return winnings


# Basic Game Function Loop for the game to run and easy to ammend in future.
def game():
    balance = deposit()
    while balance>0:
        bet=place_bet(balance)
        multiplier=bet_style()
        num=get_number()
        roll=dice_roll()
        spin=roulette_spin()
        print(f"You rolled a {roll} and the spin is {spin}")
        winnings = winning_conditions(bet,multiplier,roll,spin,num,balance)
        print(f"You won ${winnings}")
        balance=update_balance(balance,bet,winnings)
        print(f'Your balance is ${balance}')
        balance=withdraw(balance)
        if balance==0:
            balance=deposit()


# It is added so that this code can be used as a module in further projects if required.
if __name__=="__main__":
    game()
