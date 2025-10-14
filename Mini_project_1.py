#First game
print("------------- The Traveler Of The Abyss -------------")
print("Welcome traveler , you have achieved a massive feat by coming here , congrats ")
print("So traveler , what's your name ?")
name = str(input("Enter your name here : "))
health_bar=100
dragon_health=100
starting_gold = 0
while True :
    level = int(input("Enter your level as a number ( Easy=50 / Medium=100 / Hard=200) "))
    if level == 50:
        starting_gold += 50
        print("You have started your mission with 50 gold coins")
        break
    elif level == 100:
        starting_gold += 100
        print("You have started your mission with 100 gold coins")
        break
    elif level == 200:
        starting_gold += 200
        print("You have started your mission with 200 gold coins")
        break
    else:
        print("Please enter a valid level")
print(f"Glad to meet you dear {name} , to start your mission , please chose a weapon with your {starting_gold} gold coins")
print("The available weapons are : "
      "Spear and steel shield (50 gold coins)"
      "Katana and golden shield (100 gold coins)"
      "dragon slayer sword and diamond shield (200 gold coins)")
while True :
    weapon = str(input("Enter your wanted weapon (please pay attention to the spelling) : "))
    if weapon == "Spear and steel shield":
        starting_gold -= 50
        print(f"You are now a proud owner of a {weapon}")
        break
    elif weapon == "Katana and golden shield":
        while True :
            if starting_gold >= 100 :
                starting_gold -= 100
                print(f"You are now a proud owner of a {weapon}")
            else :
                print("You don't have enough gold coins to start your mission")
            break
    elif weapon == "dragon slayer sword and diamond shield":
        while True :
            if starting_gold >= 200 :
                starting_gold -= 200
                print(f"You are now a proud owner of a {weapon}")
            else :
                print("You don't have enough gold coins to start your mission")
            break
    else :
        print("Please enter a valid weapon")
    break
print("Oh no! You have just encountered a ferocious dragon!")
print("Even worse , he has just unleashed a torrent of fire upon you!")
print("You are taking health damage very fast")
if level == 50 :
    health_bar -= 50
    print("Oh no , you are taking health damage very fast")
    print(f"Your new health is {health_bar}")
if level == 100 :
    health_bar -= 30
    print("Oh no , you were hit a bit hard")
    print(f"Your new health is {health_bar}")
if level == 200 :
    health_bar -= 20
    print("didn't even flinch ! What a superhero you are !!")
    print(f"Your new health is {health_bar}")
print("Now it is your turn to return the favor !!!")
if level == 50 :
    dragon_health -=20
    print("Looks like the dragon didn't even get scratched")
    print(f"His new health is {dragon_health}")
if level == 100 :
    dragon_health -=40
    print("Great Hit")
    print(f"His new health is {dragon_health}")
if level == 200 :
    dragon_health -=70
    print("WoW !! Didn't even know you could inflict such damage with that arm ")
    print(f"His new health is {dragon_health}")
print("NOOOOOOO , The dragon is ready to unleash his most powerful technique : The Solar Burst ")
if level == 50 :
    health_bar -= 50
    print(health_bar)
    print("I'm sorry to say this , but you're dead")
    print(f"So what did you learn today {name} ? ")
    print(f"Well, dear {name} , it's that anything that comes easy goes easy and nothing will ever last")
if level == 100 :
    health_bar -= 70
    print(health_bar)
    print("I'm sorry to say this , but you're dead")
    print(f"So what did you learn today {name} ? ")
    print("Well , it's that sometimes in life you gotta give everything to get what you want")
if level == 200 :
    health_bar -= 50
    print(health_bar)
    print(f"So {name} , you did it , I'm verry proud of you ")
    print("Just the time you maybe took to chose the hard difficulty was the only key to success")
print(f"------------ I'm very proud of you {name} , You're the best You're killing it literally ------------")
print("------------ Thank you for your time ------------")
#thank you

