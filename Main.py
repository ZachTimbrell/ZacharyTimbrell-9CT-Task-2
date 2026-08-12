import time

while True:
    temp = int(input("Enter temperature: "))
    noise = "beep"
    if temp >= 100:
        time.sleep(180) 
        print(noise) # Wait for 3 minutes
