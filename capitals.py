#Find the capitals of the 20 most known countries in the world
country = str(input("What country do you wanna know the capital of ? : ")).capitalize()
capitals = {"USA": "Washington D.C" ,
            "China": "Beijing" ,
            "England": "London" ,
            "France": "Paris" ,
            "Germany": "Berlin" ,
            "Italy": "Rome" ,
            "Spain": "Madrid" ,
            "Japan": "Tokyo" ,
            "Morocco": "Rabat" ,
            "India": "New Delhi" ,
            "Canada": "Ottawa" ,
            "Brazil": "Brasilia" ,
            "Russia": "Moscow" ,
            "Australia": "Canberra" ,
            "Mexico": "Mexico City" ,
            "South korea": "Seoul" ,
            "Saudi arabia": "Riyadh" ,
            "South africa": "Well,Pretoria (administrative),Cape Town(legislative) and Bloemfontein(judicial)" ,
            "Egypt": "Cairo" ,
            "Turkey": "Ankara" ,
            "Argentina": "Buenos Aires" ,
            }
if country in capitals:
    print(f"The capital of {country} is {capitals.get(country)}")
else :

    print("Sorry , but we don't have your country")
