import pyautogui
import time
import random
import math
pyautogui.FAILSAFE = False
met = input("""
[1]: Copy paste method (no formatting binds).
[2]: Copy paste method (with formatting binds).
[3]: Middle click method.
[4]: Typewrite method. (command line entry)
[5]: Typewrite from txt file.

Pls select a method of input: """)
metter = int(met)
if metter == 1 or metter == 2 or metter == 3:
    msg = input("Have you copied the item yet? [y/n]")
    if msg != "y" and msg != "n" or msg == "no":
        print("Copy the item and run LISBDIE V2 again!")

if metter == 4:
    msg = input("Enter the message: ")
if metter == 5:
    source = input("Directory? (must be a txt file!) :")
n = input("How many times?: ")
c = input("Countdown?: ")
d = input("Delay per message?: ")
SD = input("Standard Deviation?: ")
count = int(c)
delay = int(d)
STDE = int(SD)
if math.isnan(STDE) or math.isnan(delay) or math.isnan(count) or math.isnan(metter) or delay < 0 or count < 0 or delay - STDE < 0:
    print("You did not enter numericals for the variables I needed! Run LISBDIE V3 again!")
if STDE == 0:
    Deviator = 0
while(count != 0):
    
    print(count)
    time.sleep(1)
    count -= 1

print("""
.____    .___  ___________________________  .__________________   _________  
|    |   |   |/   _____/\______   \______ \ |   \_   _____/\   \ /   /  |  | 
|    |   |   |\_____  \  |    |  _/|    |  \|   ||    __)_  \   Y   /   |  |_
|    |___|   |/        \ |    |   \|    `   \   ||        \  \     /    ^   /
|_______ \___/_______  / |______  /_______  /___/_______  /   \___/\____   | 
        \/           \/         \/        \/            \/              |__| 
""")
if metter == 1:
    for i in range(0, int(n)):
        if STDE == 0:
            Deviator = 0
        if STDE > 0:
            Deviator = random.randint(delay - STDE, delay + STDE)
        time.sleep(Deviator)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite('\n')
        print(Deviator)

if metter == 2:
    for i in range(0, int(n)):
        if STDE == 0:
            Deviator = 0
        if STDE > 0:
            Deviator = random.randint(delay - STDE, delay + STDE)
        time.sleep(Deviator)
        pyautogui.hotkey('ctrl', 'shift', 'v')
        pyautogui.typewrite('\n')
        print(Deviator)

if metter == 3:
    for i in range(0, int(n)):
        if STDE == 0:
            Deviator = 0
        if STDE > 0:
            Deviator = random.randint(delay - STDE, delay + STDE)
        time.sleep(Deviator)
        pyautogui.click(button='middle')
        pyautogui.typewrite('\n')
        print(Deviator)

if metter == 4:
    for i in range(0, int(n)):
        if STDE == 0:
            Deviator = 0
        if STDE > 0:
            Deviator = random.randint(delay - STDE, delay + STDE)
        time.sleep(Deviator)
        pyautogui.typewrite(msg)
        print(Deviator)
        pyautogui.typewrite('\n')
if metter == 5:
    for i in range(0, int(n)):
        f = open(source,'r')
        for word in f:
            try:
                if STDE == 0:
                    Deviator = 0
                if STDE > 0:
                    Deviator = random.randint(delay - STDE, delay + STDE)
                print(Deviator)
                time.sleep(Deviator)
                pyautogui.typewrite(word)
                pyautogui.typewrite("\n")
            except:
                print("The directory you provided does not exist!")
                exit()

