import random
low = 1
high = 100
answer = random.randint(low, high)
is_Running = True
print("------Number Guessing Game------")
while is_Running:
    guess = input(f"Guess a number between {low} and {high} (q to quit): ")
    if guess == answer :
        print("Correct , You're amazing!")
    elif guess == "q":
        print("Thank you for playing")
        is_Running = False
    else :
        print("Sorry, you didn't guess the right number")
print(f"The right number was {answer}")