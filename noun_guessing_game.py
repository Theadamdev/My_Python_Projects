name = str(input("Enter your name : "))
print(f"Hello {name} , I'm thinking of a noun , guess which one it is")
noun = str(input("Enter the noun I'm thinking of : "))
while not noun == "design" :
    print(f"Sorry {name} , but that's not it ")
    noun = str(input("Enter another time the noun I'm thinking of : "))
print("Goodbye")