#Randomizer
import random
number = random.randint(1, 99)
guesses = 0
while guesses < 5:
    guess = int("Enter an integer from 1 to 99: ")
    guesses +=1
    print ("this is your %d guess" %guesses)

if guess < number:
    print ("guess is low")
elif guess > number:
    print ("guess is high")
elif guess == number:
    
    if guess == number:
        guesses = str(guesses)
    print ("You guess it in : ", guesses + " guesses")
    if guess != number:
        number = str(number)
    print ("The secret number was",  number)
    
    
    
    
#SaleGoal        
 initialSalesGoal = 200000
multiplier = 100

for monthlyGoal in range (1,13):
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)

    print("Your sales goal for month" + str(monthlyGoal) + "is" + str(monthlySalesGoal))

    
    #KerryQuiz
    MF = input ("Are you a man or a woman?  ").lower()

capitalGuess = input("What is the capital of Kerry?   ")
numberOfGuesses = 1

while capitalGuess != "Tralee":
    capitalGuess = input ("Guess Again!   ")
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses >= 3:
        print ("You guessed incorrectly 3 times. Game over, fool!")
        break
    
    
if numberOfGuesses < 3:    
    if MF not in ["woman" , "lady" , "girl"]:
        print ("You guessed it. It took you " + str(numberOfGuesses) + " guesses. Take my upvote, good sir!")
    else:
        print("You guessed it. It took you " + str(numberOfGuesses) + " guesses. Take my upvote, good madam!")
