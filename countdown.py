#This is not fully completed , we still need to add a place where the user only enters the time in hours , minutes and seconds not only seconds 
import time
timer = int(input("Enter how many seconds you want to time : "))

for i in reversed(range(0, timer)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("TIME'S UP" )
