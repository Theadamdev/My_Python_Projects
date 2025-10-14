name = str(input("Hello , What is your name ? "))
foods = []
prices = []
total = 0
while True :
    food = str(input(f"Hy {name} what food would you like to buy (q to quit) ?  "))
    if food.lower() == "q" :
        print(f"You didn't buy anything {name} !")
        break
    else :
        foods.append(food)
        price = float(input(f"Enter the price of a {food} : $"))
        prices.append(price)

print("----- Your Cart -----")
for food in foods :
    print(food)

for price in prices :
    total += price
print()
print(f"So , {name} , your total is: ${total}")