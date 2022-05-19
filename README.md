# LISBDIE 💪:
  A spam tool made in python using different methods for spamming.  
  To run: `python3 LISBDIEv3.py`  
 
  
  For power users 👉 👉:  
  Consider editing your aliases in your `.bashrc` and it will run the script when run the alias.  
If you have no idea how that should be done, you just need to add an `alias LISBDIE='python3 LISBDIEv3.py'`     
    
 
 I am aware that some people are interested in the benchmarks(😉), so I decided to use a PC that was immediately available to me (I was in school and I know someone who broke his chromebook and the control and restrictions system that my school uses has not yet been installed and the teachers has not realized yet, so thanks to him.), turns out the thing kinda did worse than I thought. Anyhow the benchmarks are below!😉

# Details 🪶:
  LISBDIE version 1 consists of 1 spamming method, the replication of the keystrokes and entering it after every message being sent. However, there are some issues with this. You need to manually type the objects out (in terms of code), and in my tests it seems that the clipboard did much better in spamming speed (delay 0). 🦹‍♂️
    
   LISBDIE version 2 revolves around using other methods such as spamming from the clipboard `ctrl v` and entering it repeatedly after. 💼    
      
   LISBDIE version 3 makes use of the ability to type out words from a file. However, you may ask why is a clipboard version not made for this?     
   The reason is that you can just copy the contents of the file and it would be easier??? (and yes, version 3 inherits the features of the previous versions!)
   
   Update: as of 5th may 2022,I found time at 00:27 to add v1's features into v2. Hooray! 🤟    
   
   Branches: The linux branch will soon include an automated script to install all the needed dependencies. 🤟   
      
   Next feature: I will add a feature where it will spam the contents of a txt file with configurations as well. 🏹
  
  
  # Attacking Methods! 🔫
  So someone asked how they could apply this tool. Here is a method I came up with. Many people who used tools similar to this end up not being able to use their PC since it is running the keystrokes from the program. So to get around this, we can use virtual machines, they can then run the code and sign in, to let's say a discord account. This means you are spamming from the same account from multiple virtual PCs. This is good, but not smart, using multiple accounts on different virtual machines would be a better idea. So yeah! Have fun! I tried doing this on whatsapp and my friends told me that the virtual machine method was really effective, in 5 seconds we were able to pull out 8000 messages on 5 different virtual machines running arch linux, with the xfce DE.  
  
  
   
   # Disclaimer 🤟:
   This tool is indeed something I created after being bored since my life suddenly became a multi-headed dick hydra that is about to rip my flesh and bones apart 😀. That said, I do not encourage that you create chaos of any form to instill harm within in your social circle. Also if you are curious why the code is so badly written and why it kinda looks like ramen, that's because I was at a coffeeshop near school when I made this and uploaded it here. I was not using an IDE natively on my phone, rather I was using a txt file and then converting it to a python file to make this thing. So yes, it works, but not optimized yet (😭 I know!) , when I finally have some free time, I may consider optimizing this tool. Do tell me if there are any errors and if you would like me to correct such issues right away if you can. Have a nice day! :P 🤛


# Installation 👾:
  Ubuntu/Debian (updates repos and upgrades at the same time):
  ```
  sudo apt update && sudo apt upgrade -y && sudo apt install scrot
  ```
      
  Arch linux (syncs with repos, updates system and installs [scrot](https://archlinux.org/packages/community/x86_64/scrot/))
  ```
  sudo pacman -Syuu && sudo pacman -S scrot
  ```



# Needed Resources 🧠:
  [pyautogui](https://pyautogui.readthedocs.io/en/latest/quickstart.html)  
  [python](https://www.python.org/)   
  [scrot](https://en.wikipedia.org/wiki/Scrot)    
      
  `It should also be noted I do not own any of the items above.`
  
 # Brazen and shameless ADs 🤷‍♂‍
 [Instagram](https://instagram.com/pendragonscode)    
 [Site](https://code.senghong.xyz)    
 [Patreon](https://www.patreon.com/Pendragonscode) (not a lot of content tho 😥)    
 
 
 
 # Benchmarks 🎛️:
```
Test components:
Sentence to be spammed: "The quick brown fox jumps over the lazy dog."
Number of repetitions: 5000
Delay between each message: 0
```
CPU usage includes the other tasks as what I am also looking for is the total usage, also I could not find the instance/task as I had to run it using the IDE and not natively 😭 (remember this is chromebook and it kinda appears in a weird manner, this shit was also lagging really hard and it makes it really hard to find it. Worse, this replicates keystrokes. So I cannot scroll up and down. Damn these tiny screens. 😭).



```
keystrokes replication:
Time to complete 5000 sets: 43 seconds
Average CPU and RAM usage: 76% and 400MiB
Peak CPU: 91%
Peak RAM: 692 MiB

Pasting method (no formatting, ctrl v method as middle click is used for something else on chrome OS):
Time to complete: 37 seconds
Average CPU and RAM usage: 86% and 538 MiB
Peak CPU: 100%
Peak RAM: 736 MiB

Spam by file (content replication by typing):
Time to complete 5000 sets: 52 seconds
Average CPU and RAM usage: 100% and 900MiB
Peak CPU: 100%
Peak RAM: 1.2GiB 
```

  Will consider optimising if running the same test on another PC gets results that shows evidence of high usage, but to be fair tho, it is a lousy chromebook so lol! Also I am unable to test this on windows as i do not have a PC that can run win 11 and windows in general is completely not worth my time. 🤙
