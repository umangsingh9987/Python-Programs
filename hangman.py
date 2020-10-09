  
# https://www.facebook.com/harsith.gayle.1/posts/2784315391846205
# Subscribed by Code House


import time

#welcoming the user
name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play hangman!"

print "
"

#wait for 1 second
time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

#here we set the secret
word = "secret"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print char,    

        else:
          print "_",     
       
            failed += 1    

    if failed == 0:        
        print "You won"  

    # exit the script
        break              

    print("")
    guess = raw_input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
 
        turns -= 1        
        print "Wrong"
        print "You have", + turns, 'more guesses' 
        if turns == 0:           
            print "You Lose"
