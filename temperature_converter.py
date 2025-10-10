temp =  float(input("Enter the temperature : "))
while True :
    unit = str(input("What unit do you want ? (Celsius or Fahrenheit) ): "))
    if unit == "Celsius" or unit == "celsius":
        temp = (temp * 9) / 5 + 32
        print(f"The temperature is {temp} Celsius.")
        break
    elif unit == "Fahrenheit" or unit == "fahrenheit":
         temp = (temp - 32) * 5/9
         print(f"The temperature is {temp} Fahrenheit.")
         break
    else :
        print("Please enter a valid unit")