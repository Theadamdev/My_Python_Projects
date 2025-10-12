import time
timer = int(input("Enter how many seconds you want to time : "))

for i in reversed(range(0, timer)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP" )