#Welcome to my theatre ladies and gentlmen
print("Hello , Welcome to the Adam Theatre , the best theatre in the world ")
name = str(input("So , what is your name ? : "))
menu = {"pizza":5.50 ,
        "soda":2.25 ,
        "water":1.00 ,
        "nachos":4.00 ,
        "popcorn":3.00 ,}
cart=[]
total = 0
print("-----------MENU------------")
for key , value in menu.items():
    print(f"{key:10} : ${value}")
print("---------------------------")
while True:
    food = input("What food do you wanna buy (q to quit)? : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------Your Order----------------")
for food in cart:
    total += menu.get(food)
    print(food , end = " ")
print( )
print(f"So ,{name} , your total is  ${total}")

print("------------------------------------")
