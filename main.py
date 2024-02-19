############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

# IMPORT LIBRARIES
import time
from random import randint

def start():
    try:
        time.sleep(1)
        print("Enter how many simulations you want to run: ")
        time.sleep(0.5)
        # USER INPUTS THE NUMBER OF SIMULATIONS
        nums = int(input("Input: "))
        coinflip(nums)
    # HANDLE NOT NUMERIC INPUTS
    except ValueError:
        print("You must enter a number!")
        start()

def another():
    time.sleep(1)
    # THE PROGRAM STOPS IF THE USER INPUTS "N"
    print("Do you want to try another? (Y/N)")
    another = input("Input: ").lower()
    
    while another != "n" and another != "y":
        another = input("Input: ").lower()

    start() if another == "y" else exit()

# THE COINFLIP SIMULATION FUNCTION
def coinflip(times):
    heads = 0
    tails = 0
    # A FOR LOOP TILL THE AMOUNT OF TIMES WE WANT TO RUN THESE SIMULATIONS
    for i in range(times):
        # 50-50 CHANCE OF HEAD/TAIL
        x = randint(1,2)
        if x == 1:
            heads += 1
        else:
            tails += 1
    time.sleep(0.5)
    print("The simulation ended!")
    time.sleep(0.5)
    print("The overall scores are:")
    time.sleep(1)
    # PRINTS THE DATA OF THESE SIMULATIONS AKA: HOW MANY HEADS/TAILS
    print("Heads: ",heads)
    print("Tails: ",tails)
    another()

start()
