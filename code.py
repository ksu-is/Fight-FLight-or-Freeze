import random
import time
#Choice 1
def scene1():
    print("It's 1 am, you're laying in bed drifting off to sleep when you notice your lamp went out")
    time.sleep(5)
    print()
    print("You get up to investigate, as you know that light bulb is new")
    time.sleep(5)
    print()
    print("You go to the hallway to test out that light, process of elimanation. It does not work..")
    time.sleep(7)
    print()
    print("Out of furthered curousity, you go down the hallway to test another room.")
    time.sleep(8)
    print()
    print("You make it to the end of the hallway when you realize that the front-door at the bottom of the steps is wide open")
    print()
  
def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("What do you do know? (1 or 2) : ")
        
    return path 
      
def checkPath(chosenPath) :
    time.sleep(2)
    print()
    print("The moment is now")
    time.sleep(2)
    print()
    print("You decided with your choice")
    time.sleep(2)
    print()
    print("Is it the right one?")
    print()
    
     
    correctPath = (1)
      
    if chosenPath == str(correctPath) :
        time.sleep(2)
        print("You succusfully ran out the door")
        time.sleep(2)
        print()
        print("You are running and make it to the police department down the street")
        print()
    else:
        time.sleep(2)
        print()
        print("You hesitate, you're grabbed by a set of hands coming from the bathroom to your back")
        time.sleep(2)
        print()
        print("You fade into the darkness and your fate is left with no question")

def scene2():
    time.sleep(2)
    print()
    print("1.You make a bolt to the stairs or 2.You hide in the closet in your bedroom")

def scene3():
    time.sleep(2)
    print()
    print("An hour later, police are called to the scene of the crime..your house")
    time.sleep(5)
    print()
    print("Upon investigating,the police find nobody in the house and no scenes of a struggle.")
    time.sleep(5)
    print()
    print("However, the fusebox was discovered to had been turned off")
    time.sleep(5)
    print()
    print("As the police captain, do you send patrol around the surrounding neighborhood for the rest of the week to deter this coninuing or assume normal assignments? (1.Change and act on hard or 2.Do not change)")
    time.sleep(5)
    print()


#2nd choice
def choosePath2():
    path = ""
    while path != "1" and path != "2":
        path = input(" (1 or 2) : ")
        
    return path 
      
def checkPath2(chosenPath2) :
    time.sleep(2)
    print()
    print("Over-reacting will frighten the community")
    time.sleep(2)
    print()
    print("Not doing enough seems like you're a week captain")
    time.sleep(2)
    print()
    print("However, you have to stick to your decision as a captain")
    print()
    
     
    correctPath2 = (1)
      
    if chosenPath2 == str(correctPath2) :
        time.sleep(2)
        print("You over-react and assign to much of your force to the are, three nights later, same crime happens on the other side of town")
        time.sleep(2)
        print()
        print("The criminal(s) know how you act...")
    else:
        time.sleep(2)
        print()
        print("You act cauaslly, and not over-assign your team")
        time.sleep(2)
        print()
        print("The person strikes again, but this time down the street")
        time.sleep(2)
        print()
        print("Same MO, you got a serial killer on your hands")

def scene4 ():
    print("The main question comes to play, how is this fixed?")
    time.sleep(2)
    print()
    print("The continuation of Fight-Flight-Or Freeze will come as a new comit to this app")
    time.sleep(2)
    print()
    print("Coming July 31st....")

  
playAgain = "yes"
while playAgain == "yes":
    scene1()
    scene2()
    choice = choosePath()
    checkPath(choice)
    scene3()
    choice2 = choosePath2()
    checkPath2(choice2)
    playAgain = input ("Do you want to play again? (yes to continue playing) : ")

