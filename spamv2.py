import pyautogui
import time
import math
pyautogui.FAILSAFE = False
msg = input("Have you copied the item yet? [y/n]")
if msg != "y" and msg != "n" or msg == "no":
    print("Copy the item and run LISBDIE V2 again!")
n = input("How many times?: ")
c = input("Countdown?: ")
d =input("Delay per message?: ")
met = input("""
[1]: Copy paste method (no formatting binds).
[2]: Copy paste method (with formatting binds).
[3]: Middle click method


Pls select a method of input: """)
metter = int(met)
count = int(c)
delay = int(d)
if math.isnan(delay) or math.isnan(count) or math.isnan(metter):
    print("You did not enter numericals for the variables I needed! Run LISBDIE V2 again!")

while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("""
_    ___ ___ ___ ___ ___ _____   _____ 
| |  |_ _/ __| _ )   \_ _| __\ \ / /_  )
| |__ | |\__ \ _ \ |) | || _| \ V / / / 
|____|___|___/___/___/___|___| \_/ /___|""")
if metter == 1:
    for i in range(0, int(n)):
        time.sleep(delay)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.01)
        pyautogui.hotkey('enter')

if metter == 2:
    for i in range(0, int(n)):
        time.sleep(delay)
        pyautogui.hotkey('ctrl', 'shift', 'v')
        time.sleep(0.01)
        pyautogui.hotkey('enter')

if metter == 3:
    for i in range(0, int(n)):
        time.sleep(delay)
        pyautogui.click(button='middle')
        time.sleep(0.01)
        pyautogui.hotkey('enter')
