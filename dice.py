import random
name = str(input("What is your name? "))
print(f"Hello {name}, we will play a game of dice together and from that we will get 3 random numbers")
number1= random.randint(1,6)
number2 = random.randint(1,6)
number3 = random.randint(1,6)
print(f"Your first number is {number1}")
print(f"Your second number is {number2}")
print(f"Your third number is {number3}")