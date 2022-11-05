import pyautogui
import time
import random
import math
import json
import datetime
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
    Timebased = config["Timebased"]
    Timebasedmin = config["Timebasedmin"]
    Timebasedsec = config["Timebasedsec"]
    if int(reps) < 1 or int(count) < 1 or int(burst) < 1:
        print("You need to make sure that burst, reps and count be at least 1! Exiting If you decimals for whatever reason, LISBDIE will be !")
        exit()

if jsonConfirm == 2:
    metter = int(input("""
[01]: Copy paste method (no formatting binds).
[02]: Copy paste method (with formatting binds).
[03]: Copy Paste with Middle click method.
[04]: Typewrite method. (command line entry)
[05]: Typewrite from txt file.
[07]: Burst typewriting.
[07]: Burst typewriting from file.
[08]: Burst pasting. (No formatting binds)
[09]: Burst pasting with formatting binds.
[10]: Burst middle click pasting.
===========================================================================================================
[11]: Time based spamming by copy and paste (no formatting binds).
[12]: Time based spamming by copy and paste (with formatting binds).
[13]: Time based spamming by copy and paste (middle click method).
[14]: Time based typewrite spamming.
[15]: Time based typewriting from a file.
[17]: Time based Burst typewriting.
[17]: Time based Burst typewriting from file.
[18]: Time based Burst pasting with no formatting binds.
[19]: Time based Burst pasting with formatting binds.
[20]: Time based Burst pasting with middle click method.
Note that script would exit as long as the time limit is up, even mid burst
Also if the spam has completed the code will exit!

Pls select a method of input!: """))

    if metter > 10:
        Timebased = float(input("What is the duration you would like the spammer to run for in hours?: "))
        Timebasedmin = float(input("What is the duration you would like the spammer to run for in minutes?: "))
        Timebasedsec = float(input("What is the duration you would like the spammer to run for in seconds?: "))
    if metter == 4 or metter == 14:
        msg = input("Enter the message!: ")
    if metter == 5 or metter == 15:
        source = input("Directory? (Ensure the file is in .txt for best results!): ")
    reps = int(input("How many times?: "))
    if reps < 1:
        print("Reps cannot be less than 1!")
        reps = input("How many times?: ")
    count = int(input("Countdown?: "))
    if count < 1:
        print("Countdown should not be less than 1!")
        count = int(input("Countdown?: "))
    delay = float(input("Delay per message/Burst?: "))
    STDE = float(input("Standard deviation?: "))

    if metter > 5 and metter < 11 or metter > 15 and metter < 21:
        burst = int(input("How many reps per burst?: "))
        if metter == 7 or metter == 17:
            msg = input("Enter the message!: ")
print("Not that this spammer's countdown is written to only accept integers, meaning no decimals.")
if math.isnan(STDE) or math.isnan(delay) or math.isnan(count) or math.isnan(metter) or delay < 0 or delay - STDE < 0 or delay + STDE < 0 or count < 0:
    print("Ensure that the numbers that you have entered are in the valid ranges and are numbers!")
    exit()

if metter < 4 or metter >= 8 and metter < 14 and metter  >= 18:
    msg = input("Have you copied the item you want to spam yet? [y/n]: ")
    if msg.lower() != "y" and msg.lower != "yes":
        print("Run this when command again after you copied the item lmao!")
        exit()
if STDE == 0:
    Deviator = delay
if STDE > 0:
    Deviator = random.randint(delay - STDE, delay + STDE)
readycheck = input("Ready to execute? [y/n]: ")
if readycheck != "y" and readycheck != "yes":
    print("EXITING!")
    exit()

while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("""
.____    .___  ___________________________  .__________________   _____________ 
|    |   |   |/   _____/\______   \______ \ |   \_   _____/\   \ /   /\______  \ 
|    |   |   |\_____  \  |    |  _/|    |  \|   ||    __)_  \   Y   /     /    /
|    |___|   |/        \ |    |   \|    `   \   ||        \  \     /     /    / 
|_______ \___/_______  / |______  /_______  /___/_______  /   \___/     /____/  
        \/           \/         \/        \/            \/                      
    """)
# Copy Paste method with No Formatting Binds
def CPNFB():
    for i in range(0, reps):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
# Copy Paste method with Formatting Binds
def CPFB():
    for i in range(0, reps):
        pyautogui.hotkey('ctrl', 'shift', 'v')
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
# Copy Paste Middle Click
def CPMC():
    for i in range(0, reps):
        pyautogui.click(button='middle')
        pyautogui.typewrite("\n")
        time.sleep(Deviator) 
    exit()
    # TypeWrite from command line
def TW():
    for i in range(0, reps):
        pyautogui.typewrite(msg)
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
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
    exit()
def BFCP():
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
def BFCPF():
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.hotkey('ctrl', 'v', 'shift')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
def BFCPM():
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.click(button='middle')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
#I don't know why but when I started this on some machines it went over the stop time in a if statement. So I just made it a function.

def TimeCheck():
    stop_time = datetime.datetime.now() + datetime.timedelta(hours=Timebased, minutes=Timebasedmin, seconds=Timebasedsec)
    if datetime.datetime.now() >= stop_time:
        exit()
match metter:
    case 1:
        CPNFB()
    case 2:
        CPFB()
    case 3:
        CPMC()
    case 4:
        TW()
    case 5:
        TWFF()
    case 7:
        BF()
    case 7:
        BFFF()
    case 8:
        BFCP()
    case 9:
        BFCPF()
    case 10:
        BFCPM()
    case 11:
        TimeCheck()
        CPNFB()
    case 12:
        TimeCheck()
        CPFB()
    case 13:
        TimeCheck()
        CPMC()
    case 14:
        print(datetime.datetime.now)
        print(stop_time)
        TimeCheck()
        TW()
    case 15:
        TimeCheck()
        TWFF()
    case 17:
        TimeCheck()
        BF()
    case 17:
        TimeCheck()
        BFFF()
    case 18:
        TimeCheck()
        BFCP()
    case 19:
        TimeCheck()
        BFCPF()
    case 20:
        TimeCheck()
        BFCPM()
    case _:
        print("Invalid choice: exiting")
        exit()
