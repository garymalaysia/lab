import sys, time
import quantumrandom
import emoji

#create a list of play options
t = ["rock", "paper", "scissors"]

student = input("Student name: ")

#assign a random play to the computer
rand=quantumrandom.randint(0,2)
computer = t[int(rand)]

kids = 0 # Number of win for kids
machine = 0 # number of win for machine

#set player to False
player = False

game = ["Rock, Paper, Scissors? "]

while kids != 2 and machine != 2 :
    print ("\n")
#set player to True
    for char in game[0]:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.05)

    player = input("-> ")
    if player == computer:
        if player == "rock":
            print(emoji.emojize('{} plays :raised_fist:'.format(student)))
            print(emoji.emojize('Machine plays :raised_fist:'))
        elif player == "paper":
            print(emoji.emojize('{} plays :raised_hand:'.format(student)))
            print(emoji.emojize('Machine plays :raised_hand:'))
        else:
            print(emoji.emojize('{} plays :victory_hand:'.format(student)))
            print(emoji.emojize('Machine plays :victory_hand:'))
        print("Tie!")

        
    elif player == "rock":
        if computer == "paper":
            print(emoji.emojize('{} plays :raised_fist:'.format(student)))
            print(emoji.emojize('Machine plays :raised_hand:'))
            print("You lose!", computer, "covers", player)
            machine +=1

        else:
            print(emoji.emojize('{} plays :raised_fist:'.format(student)))
            print(emoji.emojize('Machine plays  :victory_hand:'))
            print("You win!", player, "smashes", computer)
            kids +=1
            
    elif player == "paper":
        if computer == "scissors":
            print(emoji.emojize('{} plays  :raised_hand:'.format(student)))
            print(emoji.emojize('Machine plays  :victory_hand:'))
            print("You lose!", computer, "cut", player)
            machine +=1
            
        else:
            print(emoji.emojize('{} plays  :raised_hand:'.format(student)))
            print(emoji.emojize('Machine plays  :raised_fist:'))
            print("You win!", player, "covers", computer)
            kids +=1

    elif player == "scissors":
        if computer == "rock":
            print(emoji.emojize('{} plays  :victory_hand:'.format(student)))
            print(emoji.emojize('Machine plays  :raised_fist:'))
            print("You lose...", computer, "smashes", player)
            machine +=1
            
        else:
            print(emoji.emojize('{} plays  :victory_hand:'.format(student)))
            print(emoji.emojize('Machine plays   :raised_hand:'))
            print("You win!", player, "cut", computer)
            kids +=1
            
    else:
        print("That's not a valid play. Check your spelling!")
    
    rand=quantumrandom.randint(0,2)
    computer = t[int(rand)]
    print ("{} count: ".format(student), kids)
    print ("Machine count: ", machine)

    if kids >= 2:

        print ("\n")
        print ("*********************************")
        print ("*          {} Win!!!!!!         *".format(student))
        print ("*********************************")
        print ("\n")
    elif machine >= 2:
        print ("\n")
        print ("*********************************")
        print ("*          Machine Win!!!!!     *")
        print ("*********************************")
        print ("\n")
    else:
        None

