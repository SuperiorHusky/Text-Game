#Text based plant tf game
#Created by HyperHusky and RandomMop

import time
import keyboard

actions = []

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
        print("try angain stupid")
        into()
def pause() :
    print('Press "spacebar" to continue')
    while not(keyboard.is_pressed('space')) :
        pass
    time.sleep(0.5)

print("You find youself in some strange facility. What do?")
pause()

    


into()