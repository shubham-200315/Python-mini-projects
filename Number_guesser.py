import random
while True:
    try:
       top_of_range = int(input("Type a number: "))
    except:
       pass
    else:
      break
    
random_number = random.randint(0,top_of_range)
guesses =0
while True:

    guesses+=1
    try:
      user_guess = int(input("Make a guess: "))
    except:
        pass
    else:
        if user_guess == random_number:
            print("You Got Correct")
            break
        else:
            if user_guess > random_number:
                print("You are above number")
            else:
                 print("You are below number")
            

print("Huraah! and you took " + str(guesses) + " guesses")
