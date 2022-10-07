# LISBDIE 💪:
  **About LISBDIE:**
   A spam tool written in python using keyboard input replication and multiple methods of spamming and configuration.		

  **NAVBAR:** [Details 🪶](https://github.com/pendragons-code/LISBDIE#details-) | [Attacking Methods 🔫](https://github.com/pendragons-code/LISBDIE#attacking-methods-) | [Disclaimer 🤟](https://github.com/pendragons-code/LISBDIE#disclaimer-) | [Installation 👾](https://github.com/pendragons-code/LISBDIE#installation-) | [Bash config 🕹️](https://github.com/pendragons-code/LISBDIE#bash-configuration-%EF%B8%8F) | [Resources 🧠](https://github.com/pendragons-code/LISBDIE#needed-resources-) | [Benchmarks 🎛️](https://github.com/pendragons-code/LISBDIE#needed-resources-) | [Socials 🤷‍♂‍](https://github.com/pendragons-code/LISBDIE#brazen-and-shameless-ads-) | [DEMONSTRATION 🤷‍♂‍](https://github.com/pendragons-code/LISBDIE#DEMONSTRATION)  | [💡CONFIGURATION](https://github.com/pendragons-code/LISBDIE#Config) | [🔥NEWS](https://github.com/pendragons-code/LISBDIE#Usage) | [🔥Usage](https://github.com/pendragons-code/LISBDIE#News)		
          
# News:

  Better V6 includes changes made in v5 that were accidentally reversed and now includes better variable checking. (specifically count and reps cannot be less than 1.) It also now includes an execution confirmation system.			
  
  [MAC OS USERS](https://github.com/asweigart/pyautogui/issues/687) encountering keybind/hotkey issues, learn more here.
  
  [Wayland users](https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)#:~:text=Wayland%20Security%20Module%20is%20a,work%20across%20different%20Wayland%20compositors.) will not be able to use it!
  			
			
  v8 Will aim at including arrays and manipulation of such features. This, however, will not be available for options that include copy and pasting.
			
			
  v7 Will aim at making the interface better and easier to use (potentially with a GUI) + timed based spamming, specify how long you wanna spam or how man hours you wanna spam. (essentially including a function that checks the time from a `e.g: 1 hour from now`, and exits when the time is up)		
               
# Usage:
  clone with this command!: 
  ```
  git clone https://github.com/pendragons-code/LISBDIE
  ```
  To run: 
  ```
  python3 LISBDIEv6.py
  ```
  
  **For power users 👉 👉:** 
  
  Consider editing your aliases in your `.bashrc` and it will run the script when run the alias.  
If you have no idea how that should be done, you just need to add an `alias LISBDIE='python3 ~/LISBDIE/LISBDIEv6.py'`     
    
 **Benchmarks and requests:**  
 
 I am aware that some people are interested in the benchmarks(😉), so I decided to use a PC that was immediately available to me (I was in school and I know someone who broke his chromebook and the control and restrictions system that my school uses has not yet been installed and the teachers has not realized yet, so thanks to him.), turns out the thing kinda did worse than I thought. Anyhow the benchmarks are below!😉
 
# DEMONSTRATION 🤷‍:
![DEMO](https://raw.githubusercontent.com/pendragons-code/LISBDIE/main/LISBDIE.gif) 
 
 Video was slowed down for gif conversion so this is not an accurate representation of the speed. Also the screen recording app was taking quite some CPU🤷‍. 

# Details 🪶:
**v1:**  
  LISBDIE version 1 consists of 1 spamming method, the replication of the keystrokes and entering it after every message being sent. However, there are some issues with this. You need to manually type the objects out (in terms of code), and in my tests it seems that the clipboard did much better in spamming speed (delay 0). 🦹‍♂️ 
   
   
   
**v2:**     
   LISBDIE version 2 revolves around using other methods such as spamming from the clipboard `ctrl v` and entering it repeatedly after. 💼     
    
    
     
**v3:** 
   LISBDIE version 3 makes use of the ability to type out words from a file. However, you may ask why is a clipboard version not made for this? The reason is that you can just copy the contents of the file and it would be easier??? (and yes, version 3 inherits the features of the previous versions!) 
    
    
     
**V4:**  
   LISBDIE version 4 is made to get around common anit-spam/rate-limiting technology that exists. One such technology that exist is delay checking. This means that the limiter checks the delay between each message. If the delay is consistent, it is most likely a bot since it is constantly 5 seconds (`let's say!`). However, the new feature, standard deviation is a random number from the range of numbers you provided to counter this system. This version of the tool also inherits the features of the previous versions. 
    
**SOME FIXES (v4):**
   Changed the order of operations.
   Made it that the loop does not repeatedly check the if condition, making the program run faster.
      
      
**V5:**   
   LISBDIE version 5 includes a json parsing method to find your config for your spammer, follow the format given in the `config.json` file! Fixed a bug where deviator (when standard deviation is 0) sets delay to 0 and not the stated delay. Also added fixes for file parsing, Initially not following through with the contents of the file and reading only the top item.
   
**V6:**   
   LISBDIE version 6 includes a new burst fire system that allows you to paste items, typewrite with and without a source file. The burst fire system came to mind when I was playing [squad](https://www.offworldindustries.com/game/squad/) and I found the burst fire more easy to handle than the full auto after not playing for a long time (Don't hate on the bursties they are good, in fact I recommend them to beginners.). So for some reason, it popped into my mind that, burst fire weapons are made in order to maintain consistent volumes of fire while saving ammo and preventing an inconsistent amount to be consumed each cycle. Which when put to platforms like discord, allows you to burst fire a string, still maintaining spammed items, you are more likely to escape rate limit.		
   `It should be noted that when you set the delay with a burst, this delay is used to determine the wait time between each cycle.`
   
   
  # Config:
  Here is an example of the config file!
  ```
  {
	"count": 1,
	"delay": 0,
	"SDTE": 0,
	"source": "",
	"reps": 10,
	"message": "The quick brown fox jumps over the lazy dog!",
	"metter": 4,
	"burst": 3
}
```
  
  # Attacking Methods! 🔫:
  So someone asked how they could apply this tool. Here is a method I came up with. Many people who used tools similar to this end up not being able to use their PC since it is running the keystrokes from the program. So to get around this, we can use virtual machines, they can then run the code and sign in, to let's say a discord account. This means you are spamming from the same account from multiple virtual PCs. This is good, but not smart, using multiple accounts on different virtual machines would be a better idea. So yeah! Have fun! I tried doing this on whatsapp and my friends told me that the virtual machine method was really effective, in 5 seconds we were able to pull out 8000 messages on 5 different virtual machines running arch linux, with the xfce DE.  
  
  
   
   # Disclaimer 🤟:
   This tool is indeed something I created after being bored since my life suddenly became a multi-headed dick hydra that is about to rip my flesh and bones apart 😀. That said, I do not encourage that you create chaos of any form to instill harm within in your social circle. Also if you are curious why the code is so badly written and why it kinda looks like ramen, that's because I was at a coffeeshop near school when I made this and uploaded it here. I was not using an IDE natively on my phone, rather I was using a txt file and then converting it to a python file to make this thing. So yes, it works, but not optimized yet (😭 I know!) , when I finally have some free time, I may consider optimizing this tool. Do tell me if there are any errors and if you would like me to correct such issues right away if you can. Have a nice day! :P 🤛


# Installation 👾:
  Ubuntu/Debian (updates repos and upgrades, installs python-tk and scrot):
  ```
  sudo apt update && sudo apt upgrade -y && sudo apt install scrot python-tk
  ```
      
  Arch linux (syncs with repos, updates system and installs [scrot](https://archlinux.org/packages/community/x86_64/scrot/) + [tk](https://archlinux.org/packages/extra/x86_64/tk/))
  ```
  sudo pacman -Syuu && sudo pacman -S scrot tk
  ```
  # Bash Configuration 🕹️:
   Before we begin, we need to make sure you are using bash! This is because the .bashrc file will only affect the bash terminal.
   ```
   echo $0
   ```
   The expected output should be ```bash```. If it is something else, change the defaults to bash (what I recommend), or you will have to specify that you are using bash each time before you use an alias that bash is configured to (Despite that, it should be worth highlighting that many other shells, like zsh quite literally have the same method for adding aliases. I will not be covering anything other than bash since most distros use bash by default and if you use shells like zsh, you are probably a more advanced user, also it is very similar, can't be too hard.).     
        
          
   Go to the home folder! Most things are stored in the home folder (configuration files for DE, WMs, text editors and in this case, the config for your shell!).
    ```cd```
    
   Use your preferred text editor to add the following:
    ```
    alias LISBDIEv6="python3 **directory here**"
    ```
    
   I like to do this instead, adding it in the home (```~```) folder, but with a . in front since it becomes hidden (meaning no one else knows and it does not make it too messy.). Rename the folder to ```.LISBDIEv6py``` and it should be hidden! (Linux is what I care about, Windows users you are on your own.)
   ```
   alias BANANA="python3 ~/.LISBDIEv6.py"
   ```			
   			
   To get it to work in bin:
   copy the non py version of the file and give it execute permission and transfer it to `/usr/bin`
   ```
   chmod +x myecho.py
   ```

# Needed Resources 🧠:
  [pyautogui](https://pyautogui.readthedocs.io/en/latest/quickstart.html)  
  [python](https://www.python.org/)   
  [scrot](https://en.wikipedia.org/wiki/Scrot)   
  [tk](https://docs.python.org/3/library/tk.html)
      
  `It should also be noted I do not own any of the items above.`
  
 # Brazen and shameless ADs 🤷‍♂‍
 [Instagram](https://instagram.com/pendragonscode)    
 [Site](https://code.senghong.xyz)    
 [Patreon](https://www.patreon.com/Pendragonscode) (not a lot of content tho 😥)    
 
 
 
 # Benchmarks 🎛️:
```
Test components:
Sentence to be spammed: "The quick brown fox jumps over the lazy dog."
Number of repetitions: 500
Delay between each message: 0
```


```
Chromebooks model is still the same.

Time taken by typewrite method: 1 min 04s
Time taken by copy paste method: 58s
Time taken by txt file parsing method: 2 min


Test output (spam) was in a docx file since using whatsapp and all that can be affected by internet speeds and rate limiting. This factor and some typos cause a huge inaccuracy in out data collection and I apologize.
```
CPU usage includes the other tasks as what I am also looking for is the total usage, also I could not find the instance/task as I had to run it using the IDE and not natively 😭 (remember this is chromebook and it kinda appears in a weird manner, this shit was also lagging really hard and it makes it really hard to find it. Worse, this replicates keystrokes. So I cannot scroll up and down. Damn these tiny screens. 😭).
  Will consider optimising if running the same test on another PC gets results that shows evidence of high usage, but to be fair tho, it is a lousy chromebook so lol! Also I am unable to test this on windows as i do not have a PC that can run win 11 and windows in general is completely not worth my time. 🤙

# ACKNOWLEDGEMENTS
The game, [squad](https://www.offworldindustries.com/game/squad/) is not a game that I in any way shape or form own, I'm just a player, I have to declare this so no copyright strikes lol! But seriously this game is amazingly real (comparing to my airsoft experience). I was playing this game at a friend's house and his dad, who was at some point in the military heard the game and came out telling us that was the most realistic M16 (again, this is just a military desgination of the weapon that I do not own) gunfire sound he has heard.
