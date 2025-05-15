# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

import sys

no_dup = set()
points = 5

while True:
    user_input = int(input('enter a figure between 1 and 50 : '))
    while user_input > 50:
        user_input = int(input('Not between 1 and 50. Try again : '))
    if user_input in no_dup:
        print('You already used this number. You loose 1 point.')
        points -= 1
        if points == 0:
            print('All 5 points used. You loose!')
            print(f"Content of 'set' : {no_dup}")
            sys.exit()
    elif user_input not in no_dup:
        no_dup.update([user_input]) #update adds multiple items, 'add' adds only one.  # de haakjes '([]) om de 'user_input' om te zetten naar immutable eigenschap. Anders gaat die niet in de set()
        if len(no_dup) == 11:
            print('You win!')
            print(f"Content of 'set' : {no_dup}")
            sys.exit()  
    print()
    print(f"Points left : {points}")
    print(f"Items in 'set' : {len(no_dup)}")
    print()