print("Welcome to my computer quiz!")
playing = input("Do you want to play? \n")


if playing.lower()!= "yes":
    quit()


print("Okay! Let's play :) ")
score =0

answer = input("What Does CPU stands for? ").title()
if answer == "Central Processing Unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")


answer = input("What Does CPU stands for? \n").title()
if answer == "Central Processing Unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")


answer = input("What Does CPU stands for? \n").title()
if answer == "Central Processing Unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")


answer = input("What Does CPU stands for? \n").title()
if answer == "Central Processing Unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")


answer = input("What Does CPU stands for? \n").title()
if answer == "Central Processing Unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")
    
print("You got "+ str((score/5)*100) + "%.")
