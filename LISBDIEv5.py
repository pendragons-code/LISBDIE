import pyautogui
import time
import random
import math
import json
pyautogui.FAILSAFE = False
jsoner = input("""
[1]: Import configuration file from json!
[2]: Manually set config with command-line interface!
        

Please select an input method!: """)
jsonConfirm = int(jsoner)

if jsonConfirm != 1 and jsonConfirm != 2:
    print("INVALID CHOICE PROVIDED, EXITING!")
    exit()

if jsonConfirm == 1:
    file = open("config.json")
    config = json.load(file)
    metter = config["metter"]
    source = config["source"]
    reps = config["reps"]
    STDE = config["SDTE"]
    delay = config["delay"]
    count = config["count"]
    msg = config["message"]


if jsonConfirm == 2:
    met = input("""
[1]: Copy paste method (no formatting binds).
[2]: Copy paste method (with formatting binds).
[3]: Copy Paste with Middle click method.
[4]: Typewrite method. (command line entry)
[5]: Typewrite from txt file.

Pls select a method of input!: """)
    metter = int(met)
    if metter == 4:
        msg = input("Enter the message!: ")
    if metter == 5:
        source = input("Directory? (Ensure the file is a txt file for best results!): ")
    n = input("How many times?: ")
    c = input("Countdown?: ")
    d = input("Delay per message?: ")
    SD = input("Standard Deviation?: ")
    count = int(c)
    delay = float(d)
    STDE = float(SD)
    reps = int(n)
if count < 1:
        print("Your countdown must not be less than 1!")
        exit()

print("""Note that this spammer is written to only parse Integers, meaning that it does not accept decimals!""")
if math.isnan(STDE) or math.isnan(delay) or math.isnan(count) or math.isnan(metter) or delay < 0 or delay - STDE < 0 or count < 0 or metter > 5 or metter < 1:
    print("Countdown only parse by ints!")
    exit()

if metter < 4:
    msg = input("Have you copied the item you want to spam yet? [y/n]: ")
    if msg.lower() != "y" and msg.lower() != "yes":
        print("Run this when command again after you copied the item lmao!")
        exit()

if STDE == 0:
    Deviator = delay
if STDE > 0:
    Deviator = random.randint(delay - STDE, delay + STDE)
    
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("""
.____    .___  ___________________________  .__________________   ____.________
|    |   |   |/   _____/\______   \______ \ |   \_   _____/\   \ /   /|   ____/
|    |   |   |\_____  \  |    |  _/|    |  \|   ||    __)_  \   Y   / |____  \ 
|    |___|   |/        \ |    |   \|    `   \   ||        \  \     /  /       \ 
|_______ \___/_______  / |______  /_______  /___/_______  /   \___/  /______  /
        \/           \/         \/        \/            \/                  \/ 
    """)
# Copy Paste method with No Formatting Binds
def CPNFB():
    for i in range(0, reps):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
# Copy Paste method with Formatting Binds
def CPFB():
    for i in range(0, reps):
        pyautogui.hotkey('ctrl', 'shift', 'v')
        pyautogui.typewrite("\n")
        time.sleep(Deviator) 
# Copy Paste Middle Click
def CPMC():
    for i in range(0, reps):
        pyautogui.click(button='middle')
        pyautogui.typewrite("\n")
        time.sleep(Deviator) 
    # TypeWrite from command line
def TW():
    for i in range(0, reps):
        pyautogui.typewrite(msg)
        pyautogui.typewrite("\n")
        time.sleep(Deviator) 
# TypeWrite From File
def TWFF():
    f = open(source, 'r')
    for word in f:
        try:
            for i in range(0, reps):
                pyautogui.typewrite(word)
                pyautogui.typewrite("\n")
                time.sleep(Deviator) 
        except:
            print("The directory you stated might not exist or I could not read the file!")
            exit()

# Filter
if metter == 1:
    CPNFB()
if metter == 2:
    CPFB()
if metter == 3:
    CPMC()
if metter == 4:
    TW()
if metter == 5:
    TWFF()
