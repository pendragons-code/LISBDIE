import pyautogui
import datetime
import time
def invalidchoice():
    print("You provided an invalid choice! Exiting!")
    exit()
# Copy Paste method with No Formatting Binds
def CPNFB(reps, Deviator):
    for i in range(0, reps):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
# Copy Paste method with Formatting Binds
def CPFB(reps, Deviator):
    for i in range(0, reps):
        pyautogui.hotkey('ctrl', 'shift', 'v')
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
# Copy Paste Middle Click
def CPMC(reps, Deviator):
    for i in range(0, reps):
        pyautogui.click(button='middle')
        pyautogui.typewrite("\n")
        time.sleep(Deviator) 
    exit()
    # TypeWrite from command line
def TW(reps, msg, Deviator):
    for i in range(0, reps):
        pyautogui.typewrite(msg)
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
# TypeWrite From File
def TWFF(source, reps, Deviator):
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
def BF(reps, burst, Deviator, msg):
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.typewrite(msg)
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
# Filter
def BFFF(source, reps, burst, Deviator):
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
def BFCP(reps, burst, Deviator):
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
def BFCPF(reps, burst, Deviator):
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.hotkey('ctrl', 'v', 'shift')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
def BFCPM(reps, burst, Deviator):
    for i in range(0, reps):
        for i in range(0, burst):
            pyautogui.click(button='middle')
            pyautogui.typewrite("\n")
        time.sleep(Deviator)
    exit()
#I don't know why but when I started this on some machines it went over the stop time in a if statement. So I just made it a function.

def TimeCheck(Timebased, Timebasedmin, Timebasedsec):
    stop_time = datetime.datetime.now() + datetime.timedelta(hours=Timebased, minutes=Timebasedmin, seconds=Timebasedsec)
    print(stop_time)
    if datetime.datetime.now() >= stop_time:
        exit()
