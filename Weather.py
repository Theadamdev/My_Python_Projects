#Find temperatute outside
temp = float(input("Enter the temperature in Celsius : "))
rain = float(input("Enter the percentage of rain : "))
wind = float(input("Enter the wind speed in km/h : "))
humidity = float(input("Enter the percentage of humidity : "))
if 26<=temp<=36 and rain == 5 and 8<= wind <= 14 and 35<=humidity<=45 :
    print("It's sunny outside")
elif 18<=temp<=24 and 85 <= rain <= 100 and 10<= wind <= 25 and 80<=humidity<=95 :
    print("It's rainy outside")
elif 20<=temp<=27 and 10 <= rain <= 25 and 30<= wind <= 55 and 45<=humidity<=60 :
    print("It's windy outside")
elif 22<=temp<=28 and 30 <= rain <= 50 and 10<= wind <= 20 and 60<=humidity<=75 :
    print("It's cloudy outside")
elif 32<=temp<=50 and 0 <= rain <= 10 and 5<= wind <= 15 and 20<=humidity<=35 :
    print("It's very hot outside")
elif 0 <= temp <= 10 and 40 <= rain <= 70 and 10 <= wind <= 25 and 65 <= humidity <= 80:
    print("It's very cold outside")
elif 18<=temp<=26 and 90 <= rain <= 100 and 40<= wind <= 80 and 85<=humidity<=100 :
    print("It's stormy outside")
elif -6<=temp<=2 and 85 <= rain <= 100 and 10<= wind <= 30 and 75<=humidity<=90 :
    print("It's snowy outside")
elif 8 <=temp<= 16 and 10 <= rain <= 20 and 0<= wind <= 8 and 90<=humidity<=100 :
    print("It's foggy outside")
elif 5<=temp<=15 and 70 <= rain <= 90 and 35<= wind <= 65 and 80<=humidity<=95 :
    print("It's haily outside")
elif 28<=temp<=38 and 0 <= rain <= 5 and 25<= wind <= 50 and 15<=humidity<=30 :
    print("It's dusty outside")
elif -10<=temp<=0 and 70 <= rain <= 95 and 10<= wind <= 25 and 70<=humidity<=85 :
    print("It's icy outside")
elif -5<=temp<=4 and 80 <= rain <= 100 and 5<= wind <= 15 and 75<=humidity<=90 :
    print("It's frosty outside")
elif 27<=temp<=35 and 40 <= rain <= 70 and 5<= wind <= 12 and 80<=humidity<=100 :
    print("It's humid outside")
elif 10<=temp<=18 and 15 <= rain <= 30 and 2<= wind <= 10 and 90<=humidity<=100 :
    print("It's misty outside")
elif 28<=temp<=35 and 60 <= rain <= 90 and 15<= wind <= 30 and 85<=humidity<=100 :
    print("It's tropical outside")
elif -15<=temp<=-5 and rain == 100 and 60<= wind <= 100 and 80<=humidity<=95 :
    print("There's a blizzard outside")
elif 38<=temp<=48 and 0 <= rain <= 5 and 5<= wind <= 20 and 20<=humidity<=35 :
    print("It's a heatwave outside")
elif 20<=temp<=28 and 80 <= rain <= 100 and 120<= wind <= 400 and 75<=humidity<=95 :
    print("There's a tornado outside")
elif 20<=temp<=30 and 0 <= rain <= 5 and 5<= wind <= 12 and 35<=humidity<=50 :
    print("It's clear outside")
elif 15<=temp<=22 and 20 <= rain <= 40 and 8<= wind <= 18 and 50<=humidity<=65 :
    print("It's cool outside")
elif 23<=temp<=30 and 10 <= rain <= 25 and 8<= wind <= 16 and 45<=humidity<=60 :
    print("It's warm outside")
else :

    print("There is not enough data regarding your situation ")
