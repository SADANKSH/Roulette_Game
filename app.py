# Importing Random Module to random generate choices
import random
 
# Initializing two empty list for two categories of numbers
RED=[]
BLACK=[]


# Adding Even Numbers to Red and Odd to Black Category List
for i in range(0,101):
    if i%2==0:
        RED.append(i)
    else:
        BLACK.append(i)


# Deposit Function to take deposits from the User
def deposit():
    amount=(input("Enter the amount to deposit: "))
    if amount.isdigit():
        amount=int(amount)
    else:
        print("Invalid amount")
    return amount


# Updates the wallet based on previous activities
def update_balance(balance,bet,winnings):
    balance=balance-bet+winnings
    return balance


# Asks for the Betting Style the user want to have and return effective multiplier
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


# Takes the Betting Number from the User
def get_number():
    num=input("Enter the number: ")
    if num.isdigit():
        num=int(num)
    else:
        print("Invalid number")
    return num


# Takes the BET Amount from the User
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


# Randomly genrates the Roll of the dice using the Random Module imported previously
def dice_roll():
    return random.randint(1,6)


# Randomdly Spins the Roulette using the Random Module.
def roulette_spin():
   # If first chooses between the two lists randomly
   choice = random.randint(1,2)
   # Then chooses the number fromt eh selcted randomly.
   if choice==1:
       return random.choice(RED)
   else:
       return random.choice(BLACK)


# Defines the winning conditions.
def winning_conditions(bet,multiplier,roll,spin,num,balance):
    winnings=0
    # If the roll of the Dice is 1 or 6 the Player has alread lost.No need for checking Roulette.
    while roll != 1 or roll != 6:
        # If Roll is not 1 or 6  and the player chose Low style betting then the multiplier will be 0.5x and the number should be between 0 and the number of the player.
        if multiplier==0.5 and num>=spin:
            winnings = bet*multiplier
            break
        # If the Roll is not 1 or 6 and the player chhose High style betting thenn the multiplier will be 1.5x and the number should be greater than the number of the player.
        elif multiplier==1.5 and num<=spin:
            winnings = bet*multiplier
            break
        # If the spin  of the roulette is 0 the it calls for a Bet Double from the Dealer.
        elif spin==0 and roll ==1 or spin==0 and roll ==6:
            bet = bet*2
            # If the Balnce falls short the player has lost.
            if bet>balance:
                print("You lost all your money")
                break
            else:
                pass
        else:
            print("You lost")
            break
    if roll ==1 or roll ==6:
        winnings = 0
        print("You lost")
    return winnings


# Basic Game Loop
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


# Using it so that it can be used as a module in further projects if required
if __name__=="__main__":
    game()
