import sys, time, os
import random
import emoji

pick = [0,1,2,3,4,5,6,7]
rand=random.choice(pick)


def clear():
    os.system('clear')

while len(pick):

    clear()
    student = input("name -> ")

    if "M" and "G" in student:
        sentence = "I love the hat you got! {}. ".format(student)
        print ("\n")
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n")

    elif "m" and "gary" in student:
        sentence = "You are the best teacher! {}. ".format(student)
        print ("\n")
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n")

    elif "gary" in student:
        sentence = "Happy Friday! {}. ".format(student)
        print ("\n")
        for char in sentence:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.11)
        print("\n")

    else:
        qs_joke = ["Hi {}! What did one snowman say to another snowman?? ".format(student),
        "Hola {}! What goes \"Oh Oh Oh\" ?".format(student), 
         "Hey {}! What do you call an elf wearing ear muffs?".format(student),
         "HELLO {}! When Santa is on the beach what do the elves call him?".format(student),
          "Ok {}!  What do you call Santa when he stops moving?".format(student),
         "Alright {}! What does an elf study in school?".format(student),
         "R U ready {}? What kind of ball doesn’t bounce?".format(student),
         "Your turn {}! What do you get if you mix a vampire with a snowman?".format(student) ]
        
        as_joke = ["You're Cool! ",
        " Santa walking backward <--",
        "You can call them anything because they can't hear you",
        " Sandy Claus",
        "Santa Pause",
        "The elfabet",
        "A snowball.",
        "Frostbite hahahaha"]
        print ("\n")

        for char in qs_joke[int(rand)]:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.1)

        input("")
        print("\n")


        for char in as_joke[int(rand)]:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.1)

        print("\n")
        input("Press Enter to continue ....")
        

    #print(rand)
    pick.remove(rand)
    if not len(pick):
        break
    else:
        rand=random.choice(pick)


#What did one snowman say to another snowman?
# You're Cool!

#What goes "Oh Oh Oh" ?
# Santa walking backward

#What do you can an elf wearing ear muffs?
#You can call them anything because they can't hear you

#When Santa is on the beach what do the elves call him?
# Sandy Claus 
