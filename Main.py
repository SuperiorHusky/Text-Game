#Text based plant tf game
#Created by HyperHusky and RandomMop

import time
import keyboard
from colorama import Fore, Back, Style
import random
import os

actions = []
randomKey = ['z', 'x', 'c', 'v']
gameTime = 0
invest2 = 0



def choice() :
    return input(Fore.CYAN + f"{actions}: " + Fore.WHITE)

def intro1() :
    global gameTime
    global invest2
    
    if gameTime >= 2 :
        pass
    else:
        i = choice()
        if i.lower() == actions[0] or i == "1" :
            print("\nLooking back through your mind you don't recall signing up for anything like this. In fact, you can hardly even recall what you were doing before you woke up or really anything about yourself. But before this situation can fill you with dread, the robot secretary cuts you off with her soothing, yet metallic voice.")
            gameTime += 1
            actions.remove(['Try to remind yourself of what happened before all of this', '1'])
            intro1()
        elif i == "2" :
            if invest2 == 0 :
                print("\nThe room you've awoken in is plain and clean. Nothing seems out of the ordinary")
                invest2 += 1
            else:
                print("\nActually, on further inspection, you see some signs of dilapidation near the corners of the ceiling. Black mold maybe.")
                actions.remove(['Inspect the room. Where exactly are you?', '2'])
            gameTime += 1
            intro1()
        elif i == "3" :
            print("\nYou walk toward the secretary. She greets you with a warm smile. Well at least as warm as something unorganic can be.")
            gameTime += 2
        elif i == "0" :
            print("\nYou don't have anything in your inventory")
            intro1()
        else :
            print(Fore.RED + Style.BRIGHT + "\nInput out of range" + Fore.WHITE + Style.NORMAL)
            intro1()

def questioning() :
    global gameTime
    if gameTime >= 5 :
        pass
    else: 
        i = choice()
        if i == "1" :
            print('"Well you got here like everyone else does silly! The launch pad over on the south side of the facility of course! As for the specifics on how you got on that ship I can\'t really say."')
            print('"Is there something else you want to ask about?"')
            c = input(Fore.CYAN + "['Yes please', 'No thanks']" + Fore.WHITE)
            if c.lower() == "yes please" :
                actions.remove("How did I get here?")
                actions.remove("1")
                gameTime += 1
                questioning()
            elif c.lower() == "no thanks":
                pass
            else:
                print(Fore.RED + "Input out of range" + Fore.WHITE)
                actions.remove("How did I get here?")
                actions.remove("1")
                gameTime += 1
                questioning()
        if i == "2" :
            print('"Oh well ummm, you see your fleshy body can\'t exactly tell when somethings wet, it can only detect temperature, so I\'m sure it\'s just an issue with my cooling line"')
            print("That response felt like a deflection. You can clearly tell that it's wet. Dripping almost.")
            print('"You still have time before the train arrives so is there anything else you\'d like to ask?"')
            c = input(Fore.CYAN + "['Yes please', 'No thanks']" + Fore.WHITE)
            if c.lower() == "yes please" :
                actions.remove("Why is my ID wet?")
                actions.remove("2")
                gameTime += 1
                questioning()
            elif c.lower() == "no thanks":
                pass
            else:
                print(Fore.RED + "Input out of range" + Fore.WHITE)
                actions.remove("Why is my ID wet?")
                actions.remove("2")
                gameTime += 1
                questioning()
        if i == "3" :
            print('"The habitats here are separated into biospheres so all the flora can effectively flourish. For example: the Fields Biosphere where a lot of the less threatening or easy to maintain flora are kept."')
            print('"Did that answer your question? If not there\'s still time before the train arrives, so ask away!"')
            c = input(Fore.CYAN + "['Yes please', 'No thanks']" + Fore.WHITE)
            if c.lower() == "yes please" :
                actions.remove("What do you mean biospheres?")
                actions.remove("3")
                gameTime += 1
                questioning()
            elif c.lower() == "no thanks":
                pass
            else:
                print(Fore.RED + "Input out of range" + Fore.WHITE)
                actions.remove("What do you mean biospheres?")
                actions.remove("3")
                gameTime += 1
                questioning()
        if i == "4" :
            print('"Oh I\'m D4-191Y of the Servi-bot line of consumer grade robots! Thanks for asking! None of the other volunteers ever bothered to ask for my name…."')
            dl = ["Oh that's a little sad, I think you're pretty cute for an android", "1", "D4-191Y….. That's a weird name for android, what's your manufacturer?", "2"]
            while True :            
                d = input(Fore.CYAN + f"{dl}" + Fore.WHITE)
                if d == "1" :
                    print('"Y..You Really think so?"')
                    print("The robotic secretary's face display begins to glow a bright red in response to this apparently rare compliment. You can sense you have begun to fluster this humble Servi-bot.")

                    el = ["Don't take it personally, I say things like this to all my robot companions", "1", "Of course! The kind of robot you'd expect to see on bolts and buttons monthly even…", "2"]
                    while True :  
                        e = input(Fore.CYAN + f"{el}" + Fore.WHITE)
                        if e == "1" :
                            print('"Ah I see….."')
                            print("Her fervor and enthusiasm at the conversation has fell significantly.")
                            print('"Well if you need me for anything else or have any other questions then I\'ll be right here"')
                            c = input(Fore.CYAN + "['Yes please', 'No thanks']" + Fore.WHITE)
                            if c.lower() == "yes please" :
                                actions.remove("Who are you?")
                                actions.remove("4")
                                gameTime += 1
                                questioning()
                            elif c.lower() == "no thanks":
                                gameTime += 1
                                break
                            else:
                                print(Fore.RED + "Input out of range" + Fore.WHITE)
                                actions.remove("Who are you?")
                                actions.remove("4")
                                gameTime += 1
                                questioning()
                        elif e == "2" :
                            print('"Oh my, I don\'t know if I\'d go that far but it\'s nice to know that my regular self maintenance has made me appealing"')
                            print('If it wasn\'t obvious how flustered she was, it\'s certainly more pronounced now. She\'s visibly getting even redder and letting off tiny bits of steam here and there. Seems like comparing her to such pretty robots is putting her in quite the state.')
                            print('"Anyway, if there\'s anything else I can assist you with I\'d be happy to help cutie~"')
                            c = input(Fore.CYAN + "['Yes please', 'No thanks']" + Fore.WHITE)
                            if c.lower() == "yes please" :
                                actions.remove("Who are you?")
                                actions.remove("4")
                                gameTime += 1
                                questioning()
                            elif c.lower() == "no thanks":
                                gameTime += 1
                                break
                            else:
                                print(Fore.RED + "Input out of range" + Fore.WHITE)
                                actions.remove("Who are you?")
                                actions.remove("4")
                                gameTime += 1
                                questioning()

                elif d == "2" :
                    print('"It\'s a…. kind of a nickname of sorts that my mistresses gave me. I don\'t actually recall what my manufacturer is, but I do remember the assembly line somewhat. Although my black-box feature only allows me to see a certain distance back before I was properly booted up."')
                    print("Seems like a weird case of owners sanding off the labels, but the fact she can't recall any factory settings at all seems a bit odd. Considering the circumstances, you don't know if you'll be getting any more answers about this from her despite your curiosity.")
                    print('"Now are there any other less personal matters you need help with?"')
                    c = input(Fore.CYAN + "['Yes please', 'No thanks']" + Fore.WHITE)
                    if c.lower() == "yes please" :
                        actions.remove("Who are you?")
                        actions.remove("4")
                        gameTime += 1
                        questioning()
                    elif c.lower() == "no thanks":
                        gameTime += 1
                        break
                    else:
                        print(Fore.RED + "Input out of range" + Fore.WHITE)
                        actions.remove("Who are you?")
                        actions.remove("4")
                        gameTime += 1
                        questioning()
                else:
                    print(Fore.RED + "Input out of range" + Fore.WHITE)
        if i == "5" :
            print('"You can\'t remember anything? It\'s most likely a major case of cryo-induced memory loss."')
            print(Fore.CYAN + "Cryo-induced memory loss? That's not a thing." + Fore.WHITE)
            print('"Of course it is! Many people have been subject to cryo-induced memory loss, especially after extended durations."')
            print('You know that cryogenics are extremely reliable and hardly have any side effects. But you decide to let the subject drop.')
            print('"If you have any more questions I\'ll gladly answer them!"')
            c = input(Fore.CYAN + "['Yes please', 'No thanks']" + Fore.WHITE)
            if c.lower() == "yes please" :
                actions.remove("Why can't I remember anything?")
                actions.remove("5")
                gameTime += 1
                questioning()
            elif c.lower() == "no thanks":
                gameTime += 1
                pass
            else:
                print(Fore.RED + "Input out of range" + Fore.WHITE)
                actions.remove("Why can't I remember anything?")
                actions.remove("5")
                gameTime += 1
                questioning()

def pause() :
    print('\nPress "spacebar" to continue\n')
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
        return False
    else :
        return True

def clear() :
    os.system('cls')

clear()

print("You awake in an unfamiliar looking room. A vast white containment that appears about as sterile as a doctors office. As you begin to take in the harsh lighting, a piercing scratch followed by a robotic voice floods the room. Somehow, you managed to miss the robotic bunny girl looking secretary standing behind a large reception desk. In a dulcet but robotic tone it says:")
pause()
print('\n"Welcome to Botanical Research Society of Transformative Flora! We are very happy you chose to become one of our very willing and happy volunteers for the citizen scientist position!"')
pause()
print("\nVolunteer? Citizen scientist position? Almost everything here feels unfamiliar. It might be a good idea to INVESTIGATE your surroundings to get your bearings or try and remember how you got here. You can also forgo all of that and make conversation with that rather welcoming secretary.\n")


actions.extend(["Try to remind yourself of what happened before all of this", "1", "Inspect the room. Where exactly are you?", "2", "Talk with the secretary", "3", "Inventory", "0"])


intro1()

print('\n"Could you please come here sweetheart? Take as much time as you need to get yourself adjusted, but there\'s some important paperwork you need to fill out before I can let you go."')
print('\n"Would you please take the time to fill out this form for me sweetheart?"')
username = input(Fore.CYAN + "At the top of the form you sign your name: " + Fore.WHITE)
print(f'\n{username}! What a wonderful name you have there. lemme get your ID printed out for you real quick. If you\'d just smile for me really fast-"')

pause()
cameraQTE = quickTime("", 400)
if cameraQTE == True :
    print("\nSurprisingly you actually manage to crack a pretty good smile before- *FLASH* *CLICK*. Seems like your impeccable reaction time payed off, your ID hopefully won't look terrible now.")
else:
    print("\nYour brain doesn't even have time to process her words before- *FLASH* *CLICK*. Just like at the DMV you've been caught with your pants down by the flash of a camera bulb.")

pause()

print("The steel secretary hums and whirs and eventually, an ID slides out of her thin mouth. When you pick it up it's bizarrely…. wet? It feels as if this secretary spit it out of an actual human mouth. Again you don't have any time to dwell on this before she cuts you off.")
print('"Make sure not to loose that deary! That ID is how you\'re going to get access all the facilities and biospheres here at this facility! Now do you have any questions for me before your transport gets here?"')
actions.clear()
actions.extend(["How did I get here?", "1", "Why is my ID wet?", "2", "What do you mean biospheres?", "3", "Who are you?", "4", "Why can't I remember anything?", "5", "Exit"])
gameTime = 2
questioning()

print('The room suddenly shakes and the rushing sound of wind pushes past you. Behind a set of doors beyond the secretary, streaks of polished metal fly past small windows. Whatever is out there comes to a stop, and the doors slide open reveling a subway car inside.')
print('"It looks like your train is here dearie! Please step inside, and bask in the glory of the Botanical Research Society of Transformative Flora!"')

actions.clear()
actions.extend(["Walk into the train car", "1", "Stay put,", "2"])
train = choice()

while True :
    if train == "2" :
        print('"Ahem, I said that your train is here. That means you need to get inside."')
        break
    elif train == "1" :
        break
    else: 
        print(Fore.RED + "Input out of range" + Fore.WHITE)

actions.clear()
actions.extend(["Enter", "1", "Refuse", "2"])
train = choice()

while True :
    if train == "2" :
        print('"I know it may seem a bit intimidating, but there\'s nothing to worry about! Travel by train is a very old yet safe form of transportation."')
        break
    elif train == "1" :
        break
    else: 
        print(Fore.RED + "Input out of range" + Fore.WHITE)

actions.clear()
actions.extend(["Go in", "1", "Back away", "2"])
train = choice()

while True :
    if train == "2" :
        print('"Ok dearie, I\'ve been patient with you, but this is your last chance to go inside yourself before I force you to."')
        break
    elif train == "1" :
        break
    else: 
        print(Fore.RED + "Input out of range" + Fore.WHITE)

actions.clear()
actions.extend(["Comply", "1", "Hold position", "2"])
train = choice()
bad = False

while True :
    if train == "2" :
        print('"Oh well, I did warn you…"')
        print("A series of clicks and whirs emanate from the chromatic sleeves of the secretary as she raises an arm upwards. Something that wasn't there before protrudes from her arm. Then, quicker than you can blink, a pulse is fired from the device, and renders you completely unconscious. When you awake, you notice a buzzing in your head that wasn't present before, and somehow you've made it onto the train.")
        bad = True
        break
    elif train == "1" :
        break
    else: 
        print(Fore.RED + "Input out of range" + Fore.WHITE)

if bad == False:
    print("You cross the threshold of the doors onto the train. It's unfamiliar and primitive. Built large enough to move 50 or so people at once. The thought of no privacy between strangers is one that revolts you. Luckily for now however, you are the only passenger of this weird vessel. The doors behind you slide to their closed positions, and with a slight jolt, the train starts to move.")
else:
    pass