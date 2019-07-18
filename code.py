import random
import time

def scene1():
    print("It's 1 am, you're laying in bed drifting off to sleep when you notice your lamp went out")
    time.sleep(5)
    print("You get up to investigate, as you know that light bulb is new")
    time.sleep(5)
    print("You go to the hallway to test out that light, process of elimanation. It does not work..")
    time.sleep(7)
    print("Out of furthered curousity, you go down the hallways to test another room.")
    time.sleep(8)
    print("You make it to the end of the hallway when you realize that the fron-tdoor at the bottom of the steps is wide open")
    print()
  
def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("What do you do know? (1 or 2) : ")
        
    return path 
      
def checkPath(chosenPath) :
    print("You need to decide what to do")
    time.sleep(2)
    print("Bolting to the door seeems viable")
    time.sleep(2)
    print("Does hiding in the bedroom closet make sense?")
    print()
    time.sleep()
     
    correctPath = random.randint(1, 2)
      
    if chosenPath == str(correctPath) :
        print("You succusfully ran out the door")
        print("You are running and make it to the police department down the street")
    else:
        print("You hesitate, you're grabbed by a set of hands coming from the bathroom to your back")
        print("You fade into the darkness and your fate is left with no question")
  
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    scene1()
choice = choosePath()
checkPath(choice)
playAgain = input ("Do you want to play again? (yes or y to continue playing) : ")





