# This script simulates a coin flip. It randomly returns either "heads" or "tails."
import random

def coin_flip():
    if random.randint(0, 1) == 0:
        return "Heads"
    else:
        return "Tails"
    
print(coin_flip())

