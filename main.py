import time
from random import randint

def start():
    try:
        time.sleep(1)
        print("Enter how many simulations you want to run: ")
        time.sleep(0.5)
        nums = int(input("Input: "))
        coinflip(nums)
    except ValueError:
        print("You must enter a number!")
        start()

def another():
    time.sleep(1)
    print("Do you want to try another? (Y/N)")
    another = input("Input: ").lower()
    
    while another != "n" and another != "y":
        another = input("Input: ").lower()

    start() if another == "y" else exit()

def coinflip(times):
    heads = 0
    tails = 0
    for i in range(times):
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
    print("Heads: ",heads)
    print("Tails: ",tails)
    another()
    

start()