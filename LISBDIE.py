import pyautogui
import time
pyautogui.FAILSAFE = False
msg = input("Enter the message: ")
n = input("How many times?: ")
c = input("Countdown?: ")
d = input("Delay per message?:")
count = int(c)
delay = int(d)
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("""
.-.   .-..---..--..--. .-..---.
| |__ | | \ \ |-< | \ \| || |- 
`----'`-'`---'`--'`-'-'`-'`---' """)
print("Version 1")
for i in range(0,int(n)):
    time.sleep(delay)
    pyautogui.typewrite(msg)
    pyautogui.typewrite("\n")
