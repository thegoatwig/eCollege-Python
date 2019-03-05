MF = input ("Are you a man or a woman?  ").lower()

capitalGuess = input("What is the capital of Kerry?   ")
numberOfGuesses = 1

while capitalGuess != "Tralee":
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses > 3:
        print ("You guessed incorrectly 3 times, fool!")
        break
    capitalGuess = input ("Guess Again!   ")
    
if numberOfGuesses <= 3:    
    if MF not in ["woman" , "lady" , "girl"]:
        print ("You guessed it. It took you " + str(numberOfGuesses) + " guesses. Take my upvote, good sir!")
    else:
        print("You guessed it. It took you " + str(numberOfGuesses) + " guesses. Take my upvote, good madam!")
