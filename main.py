import random
from art import logo

print(logo)
print(
    """Welcome to the Number Guessing Game! I am thinking of a number from 1 and 100. """
)
answer = random.randint(1, 100)
print(f"My guess is {answer}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attemps = 0

if difficulty == 'easy':
    attemps = 10
    print(f" You have {attemps} attemps remaning to guess the number. ")
else:
    attemps = 5
    print(f"You have {attemps} attemps remaining to guess the nubmer. ")


continue_the_game = True

while continue_the_game:
    guess = int(input("Take a guess: "))
    if attemps == 1:
        continue_the_game = False
        print("Game over.")
    elif answer > guess:
        print("Too low.")
        attemps -= 1
        print(f"You have {attemps} attmps remaining to guess the number.")
        
    elif answer < guess:
        print("Too high.")
        attemps -= 1
        print(f"You have {attemps} attmps remaining to guess the number.")
    else:
        print("Good job, you guessed correctly!")
        continue_the_game = False

