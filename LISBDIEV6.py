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
    burst = config["burst"]


if jsonConfirm == 2:
    metter = int(input("""
[01]: Copy paste method (no formatting binds).
[02]: Copy paste method (with formatting binds).
[03]: Copy Paste with Middle click method.
[04]: Typewrite method. (command line entry)
[05]: Typewrite from txt file.
[06]: Burst typewriting.
[07]: Burst typewriting from file.
[08]: Burst pasting. (No formatting binds)
[09]: Burst pasting with formatting binds.
[10]: Burst middle click pasting.

Pls select a method of input!: """))

    if metter > 10 or metter < 1:
        print("You need to give a valid input!")
        exit()
    if metter == 4:
        msg = input("Enter the message!: ")
    if metter == 5:
        source = input("Directory? (Ensure the file is a txt file for best results!): ")
    n = input("How many times?: ")
    count = int(input("Countdown?: "))
    d = input("Delay per message/burst?: ")
    SD = input("Standard Deviation?: ")
    delay = float(d)
    STDE = float(SD)
    reps = int(n)
if count < 1:
        print("Your countdown must not be less than 1!")
        exit()

print("""
Note that this spammer's countdown is written to only parse Integers, meaning that it does not accept decimals!
""")
if math.isnan(STDE) or math.isnan(delay) or math.isnan(count) or math.isnan(metter) or delay < 0 or delay - STDE < 0 or count < 0:
    print("Ensure that the numbers/variables you entered are in the valid ranges and are numbers!")
    exit()

if metter < 4 or metter >= 8:
    msg = input("Have you copied the item you want to spam yet? [y/n]: ")
    if msg.lower() != "y" and msg.lower() != "yes":
        print("Run this when command again after you copied the item lmao!")
        exit()
if metter > 5:
    burst = int(input("How many messages should be sent per burst?: "))
    if metter == 5:
        msg = input("Enter the message!: ")

    if metter == 7:
        source = input("Directory? (Ensure the file is a txt file for best results!): ")

if STDE == 0:
    Deviator = delay
if STDE > 0:
    Deviator = random.randint(delay - STDE, delay + STDE)
    
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("""
.____    .___  ___________________________  .__________________   ____________
|    |   |   |/   _____/\______   \______ \ |   \_   _____/\   \ /   /  _____/
|    |   |   |\_____  \  |    |  _/|    |  \|   ||    __)_  \   Y   /   __  \ 
|    |___|   |/        \ |    |   \|    `   \   ||        \  \     /\  |__\  \
|_______ \___/_______  / |______  /_______  /___/_______  /   \___/  \_____  /
        \/           \/         \/        \/            \/                 \/ 
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
    for i in range(0, reps): 
        try:
            for word in f:
                pyautogui.typewrite(word)
                pyautogui.typewrite("\n")
                time.sleep(Deviator) 
        except:
            print("The directory you stated might not exist or I could not read the file!")
            exit()
#Burst Fire
def BF():
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.typewrite(msg)
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
# Filter
def BFFF():
    f = open(source, 'r')
    for i in range(0, reps):
        for i in range(0, burst):
            try:
                for word in f:
                    pyautogui.typewrite(word)
                    pyautogui.typewrite("\n")
            except:
                print("The directory you stated might not exist or I could not read the file!")
                exit()
        time.sleep(Deviator)
def BFCP():
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
def BFCPF():
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.hotkey('ctrl', 'v', 'shift')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
def BFCPM():
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.click(button='middle')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)

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
if metter == 6:
    BF()
if metter == 7:
    BFFF()
if metter == 8:
    BFCP()
if metter == 9:
    BFCPF()
if metter == 10:
    BFCPM