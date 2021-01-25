import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if random_number > guess:
            print("It's higher")
        elif random_number < guess:
            print("It's lower")
    print(f"Yes, it is {random_number}!")

guess(1000)