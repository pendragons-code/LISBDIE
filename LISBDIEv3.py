import pyautogui
import time
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
d =input("Delay per message?: ")
count = int(c)
delay = int(d)
if math.isnan(delay) or math.isnan(count) or math.isnan(metter) or delay < 0 or count < 0:
    print("You did not enter numericals for the variables I needed! Run LISBDIE V3 again!")

while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("""
.____    .___  ___________________________  .__________________   ____________  
|    |   |   |/   _____/\______   \______ \ |   \_   _____/\   \ /   /\_____  \ 
|    |   |   |\_____  \  |    |  _/|    |  \|   ||    __)_  \   Y   /   _(__  < 
|    |___|   |/        \ |    |   \|    `   \   ||        \  \     /   /       |
|_______ \___/_______  / |______  /_______  /___/_______  /   \___/   /______  /
        \/           \/         \/        \/            \/                   \/
""")
if metter == 1:
    for i in range(0, int(n)):
        time.sleep(delay)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite('\n')

if metter == 2:
    for i in range(0, int(n)):
        time.sleep(delay)
        pyautogui.hotkey('ctrl', 'shift', 'v')
        pyautogui.typewrite('\n')

if metter == 3:
    for i in range(0, int(n)):
        time.sleep(delay)
        pyautogui.click(button='middle')
        pyautogui.typewrite('\n')

if metter == 4:
    for i in range(0, int(n)):
        time.sleep(delay)
        pyautogui.typewrite(msg)
        pyautogui.typewrite('\n')
if metter == 5:
    for i in range(0, int(n)):
        try:
            f = open(source,'r')
            for word in f:
                time.sleep(delay)
                pyautogui.typewrite(word)
                pyautogui.typewrite("\n")
        except:
            print("The directory you stated might not exist!")
