weight = float(input("Enter your official weight : "))
while True :
    unit = str(input("What unit do you want ? (Kilograms or Pounds): "))
    if unit == "kilograms" or unit == "Kilograms":
        weight *= 2.205
        print(f"Your weight is {weight} Kilograms.")
        break
    elif unit == "Pounds" or unit == "pounds":
        weight /= 2.205
        print(f"Your weight is {weight} Pounds.")
        break
    else:
        print("Please enter a valid unit")