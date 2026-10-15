import random

# create list of five words 
words = ["python","apple","flower","laptop","codealpha"]
secret_word = random.choice(words)

# variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to the Hangman game!")

# start the game

while wrong_guesses < max_wrong_guesses:
    
    #display guessed and hidden letters
    display_word = ""
    
    for letter in secret_word:
        if letter in guessed_letters:
           display_word += letter+" "  
        else:
            display_word+= "_"
            
    print("\nWord:",display_word)
    
    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        break
    
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
    
    #get a letter from user
    
    guess = input("Guess a letter!").lower().strip()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
   # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
    
# Display the result
if all(letter in guessed_letters for letter in secret_word):
    print("\nCongratulations! You won!")
    print("The word was:", secret_word)
else:
    print("\nGame over! You lost.")
    print("The word was:", secret_word)
        
