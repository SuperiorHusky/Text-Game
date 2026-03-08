#Text based plant tf game
#Created by HyperHusky and RandomMop

print("*A piercing scratch followed by a robotic voice floods the vast white room you find yourself in.*")
print("Welcome to Botnical Research Socity of Transformative Flora. Please describe your preferred name: ")
username = input()
print(f"Thank you {username} for choosing to further our research in transformative flora.")
print("Awaiting transport. Please be patiant.")
print("*A hum drones on. You notice a set of doors to your side and a lonely receptionist desk in front of you with nobody sitting there.*")


def intro ():
    n = 0
    while n < 2 :

        choice = input("Investigate the desk / Inspect the doors : ").lower()
        if choice == "investigate the desk" :
            if n == 1:
                print("*Looking inside the drawers yields nothing but stirred dust and a sense of dissapointment.*")
            else:
                print("*Walking up to the desk you notice small rings of coffee stains scattered across the plane. This place has indeed been inhabited before.*")
                print('*Theres papers with no text on them except a neat stack of parchment titled: "Volentier Form".*')
                print("*You also notice cabients along the desk.*")
                print("Tip: Interacting with things multiple times may give more information")
            n += 1
        elif choice == "inspect the doors" :
            print("*The doors are metallic and sport large windows at head height.*")
            print("*Behind the windows you see what appears to be a subway tunnel.*")
            n += 1
        else :
            print("Out of range")   
    print("*Suddenly a large rumble comes your way. A speeding train rushes through the station and halts at the platform.*")
    print("*The doors slide open with a groan and you get a glimpse of a deserted subway car lined with seats in a pleasant reddish-orange hue.*")
    print("*The robotic voice crackles on again.*")
    print(f"Subject {username}, please enter the transportation shuttle.")
    choice = input("Enter? (Y/N) : ").lower()
    if choice == "n" :
        print("*You refuse to get into the train, and instead stand your ground.*")
        print("*The voice echos again:*")
        print("Please enter the transportation shuttle or face punishment")
        n += 1
    elif choice == "y" :
        print("*You tentativly step onto the train. As soon as you are inside the doors quickly close behind you.")


intro()