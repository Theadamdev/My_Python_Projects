#this outputs a rectangle
columns = int(input("How many columns do you want? "))
rows = int(input("How many rows do you want? "))
symbol = input("What symbol do you want? ")
for i in range (rows) :
    for x in range (columns) :
        print(symbol , end = "")

    print(" ")
