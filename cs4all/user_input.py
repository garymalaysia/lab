import sys, time
import quantumrandom

print ("what is your name?")
student = input("name -> ")

if "M" and "G" in student:
    sentence = "I love the hat you got! {}. ".format(student)
    print ("\n")
    for char in sentence:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.15)
    print("\n")

elif "m" and "gary" in student:
    sentence = "You are the best teacher! {}. ".format(student)
    print ("\n")
    for char in sentence:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.15)
    print("\n")

elif "gary" in student:
    sentence = "Happy Friday! {}. ".format(student)
    print ("\n")
    for char in sentence:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.15)
    print("\n")

else:
    qs_joke = ["Hi {}! What does your computer do for lunch? ".format(student),
    "Hola {}! What did the buffalo say at drop off?".format(student), 
     "Hey {}! Why do math books always look so sad?".format(student),
     "HELLO {}! Why did the kid brings a ladder to school?".format(student),
      "Ok {}! What is the smartest insect?".format(student),
     "Alright {}! What did the spider make online?".format(student),
     "R U ready {}? Why do magicians always do so well at school?".format(student),
     "Your turn {}! Which side of the turkey has the most feathers? left side? Right side?".format(student) ]
    
    as_joke = ["Your computer has a byte ^O^",
    "Bison..... Get it?",
    "They are full of problem T-T",
    "Because the kid wanted to go to HIGH school >O<",
    "Spelling Bee",
    "A Website! hehe",
    "They can handle trick question!",
    "is the OUTSIDE! hahahaha"]
    rand=quantumrandom.randint(0,7)
    print ("\n")

    for char in qs_joke[int(rand)]:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.15)

    time.sleep(5)
    print ("\n")

    for char in as_joke[int(rand)]:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.1)

    print("\n")

