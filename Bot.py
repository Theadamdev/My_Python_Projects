#I'm pround of myself
print('Hi , my name is Bot and i know nothing about you')
name : str = input('What is your name ? ')
print(f'Welcome , {name} !')
mood : str = input("How are you doing ? \n "
      "1.good \n "
      "2.sad \n "
      "3.doing very bad \n "
      "4.content \n "
      "Enter your choice : ")
if mood == 'good' :
    print('Ok Bye')
elif mood == 'sad' :
    print('Indeed, with hardship comes ease')
elif mood == 'doing very bad' :
    print('Alhamduliallah')
else :
    print('All praise be to allah')
gender : str = input("What gender are you ? \n "
      "1.male \n "
      "2.female \n "
      "Enter your choice :")
if gender == 'male' :
    print(f'{name} is a male')
else :
    print(f'{name} is a female')
favourite_color : str = input("What is your favourite color ? \n "
      "1.Blue \n "
      "2.Pink \n "
      "3.Red \n "
      "4.Yellow \n "
      "Enter your choice : ")
print("That's enough questions for today")

print(f'You name is {name} , you are {mood} , you are a {gender} and your favourite color is {favourite_color}')
