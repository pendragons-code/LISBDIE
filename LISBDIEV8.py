import pyautogui
import json
import math
import json
import datetime
import time
import SpamFunctions
import random
pyautogui.FAILSAFE = False

# This part gets user response if he wanna get the stuff from the json file or manually put in stuff.
jsonConfirm = int(input("""
[1]: Import configuration file from json!
[2]: Manually set config with command-line interface!

Please select an input method!: """))
if jsonConfirm != 1 and jsonConfirm != 2:
    SpamFunctions.invalidchoice()
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

if jsonConfirm == 2:
    #asking user which options to fly with
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
===========================================================================================================
[11]: Time based spamming by copy and paste (no formatting binds).
[12]: Time based spamming by copy and paste (with formatting binds).
[13]: Time based spamming by copy and paste (middle click method).
[14]: Time based typewrite spamming.
[15]: Time based typewriting from a file.
[16]: Time based Burst typewriting.
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
        if metter == 6 or metter == 16:
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
# filter
match metter:
    case 1:
        SpamFunctions.CPNFB(reps, Deviator)
    case 2:
        SpamFunctions.CPFB(reps, Deviator)
    case 3:
        SpamFunctions.CPMC(reps, Deviator)
    case 4:
        SpamFunctions.TW(reps, msg, Deviator)
    case 5:
        SpamFunctions.TWFF(source, reps, Deviator)
    case 6:
       SpamFunctions. BF(reps, burst, Deviator, msg)
    case 7:
        SpamFunctions.BFFF(source, reps, burst, Deviator)
    case 8:
        SpamFunctions.BFCP(reps, burst, Deviator)
    case 9:
        SpamFunctions.BFCPF(reps, burst, Deviator)
    case 10:
        SpamFunctions.BFCPM(reps, burst, Deviator)
    case 11:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.CPNFB(reps, Deviator)
    case 12:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.CPFB(reps, Deviator)
    case 13:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.CPMC(reps, Deviator)
    case 14:
        print(datetime.datetime.now)
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.TW(reps, msg, Deviator)
    case 15:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.TWFF(source, reps, Deviator)
    case 16:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.BF(reps, burst, Deviator, msg)
    case 17:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.BFFF(source, reps, burst, Deviator)
    case 18:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.BFCP(reps, burst, Deviator)
    case 19:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.BFCPF(reps, burst, Deviator)
    case 20:
        SpamFunctions.TimeCheck(Timebased, Timebasedmin, Timebasedsec)
        SpamFunctions.BFCPM(reps, burst, Deviator)
    case _:
        print("Invalid choice: exiting")
        exit()
