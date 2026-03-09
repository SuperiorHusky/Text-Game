#Text based plant tf game
#Created by HyperHusky and RandomMop

import time
import keyboard
from colorama import Fore, Back, Style
import random

actions = []
randomKey = ['z', 'x', 'c', 'v']

def choice() :
    return input(f"{actions}: ")

def into() :
    actions.extend(["left","right","forward","backward","inventory"])
    print("Test input\n")
    i = choice()
    if i == "left" :
        print("Congrats")
    elif i == "right" :
        print("Fuck yoi")
    elif i == "forward" :
        print("died to swapm goo")
    elif i == "backward" :
        print("you cant leave coward")
    elif i == "inventory" :
        print("your pockets are empty")
    else :
        print(Fore.RED + Style.BRIGHT + "try angain stupid" + Fore.WHITE + Style.NORMAL)
        into()
def pause() :
    print('Press "spacebar" to continue')
<<<<<<< HEAD
    keyboard.wait('space')

def quickTime(string, ms) :
    n = 0
    r = random.randint(0,3)
    print(string)
    print(Fore.RED + Style.BRIGHT + f"PRESS {randomKey[r]}!!!" + Fore.WHITE + Style.NORMAL)
    while not(keyboard.is_pressed(f'{randomKey[r]}')) and n < ms :
        time.sleep(0.001)
        n += 1

    if n >= ms :
        print("You failed the qte")
    else :
        print("You succeded the qte")
=======
    while not(keyboard.is_pressed('space')) :
        pass
>>>>>>> 80a50915e258cb7c6fb9be6aca268c81b1724e89

print("You find youself in some strange facility. What do?")
pause()

    
<<<<<<< HEAD
into()
quickTime("Quick!", 2000)
=======


into()
>>>>>>> 80a50915e258cb7c6fb9be6aca268c81b1724e89
