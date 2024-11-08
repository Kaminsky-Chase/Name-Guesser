import random
from fruits import fruits # this is saying import fruits.py and then importing the list "fruits" into this list to use.

# Prompt user to choose a difficulty level by number
Difficulty= input(""" 
Welcome to word guesser
1. Very Easy -- 12 Guesses
2. Easy -- 9 Guesses
3. Medium -- 6 Guesses
4. Hard -- 3 Guesses
Choose a Difficulty: """).strip()  # Get the user's input and strip any extra spaces

levels = ['Very Easy', 'Easy', 'Medium', 'Hard'] # levels provided in a list

incorrectGuesses = 0 # Default guesses
maxIncorrectGuesses = 12  # Default max guesses for very easy and then subtracted by the levels. or this can be removed and it can be initlized in the levels such as maxIncorrectGuesses == 12/9/6/3

while True:
    try: # try
        # Check the user's input and map it to the correct difficulty level
        if Difficulty == '1': # if user input is 1 then it will select very easy which is indexed at 0 and so on.
            print(f"\n{levels[0]} Selected")
            break # this ends the "While" loop
        elif Difficulty == '2':
            print(f"\n{levels[1]} Selected")
            maxIncorrectGuesses -= (incorrectGuesses + 3)  # Reduce guesses for Easy
            break
        elif Difficulty == '3':
            print(f"\n{levels[2]} Selected")
            maxIncorrectGuesses -= (incorrectGuesses + 6)  # Reduce guesses for Medium
            break
        elif Difficulty == '4':
            print(f"\n{levels[3]} Selected")
            maxIncorrectGuesses -= (incorrectGuesses + 9)  # Reduce guesses for Hard
            break
        else:
            print("Invalid difficulty. Please choose from: 1, 2, 3, 4.")
            Difficulty = input("Choose a Difficulty: ").strip()  # Prompt again for valid input

    except ValueError: #cache
        print("Invalid input. Please try again.")

def wordUpdated(chosenRandom, guessedLetter, wordState):
# chosenRandom: This parameter represents the randomly chosen word that the user is trying to guess. It's typically a string (like "apple").
# guessedLetter: This parameter represents the single letter that the user has guessed. The function uses this letter to check against each letter in chosenRandom.
# wordState: This parameter is the current state of the guessed word, represented as a list of underscores (_) and revealed letters. For example, if the user has partially guessed "apple" and correctly guessed "a" and "p", then wordState might look like ["a", "p", "_", "_", "_"].
# In essence, this line sets up the function and specifies what inputs it expects to receive.

    updatedWordState = wordState[:] # Creates a copy of the current guessed word state (wordState) to avoid changing it directly
    for i, letter in enumerate(chosenRandom): # its indexing the word in the randomly generated word for potion 0 to so on -- Loops through each letter in the word (chosenRandom) with its index (i).
        if letter.lower() == guessedLetter.lower(): # Compares each letter in the word to the guessed letter, ignoring case.
            updatedWordState[i] = letter # If there's a match, replaces the underscore (_) in updatedWordState at that index with the correct letter.
    return updatedWordState # Returns the updated version of the word with correctly guessed letters revealed.

def displayWordState(wordState):
    return " ".join(wordState) #seperates Characters

randomWord = fruits # calls fruits from fruits.py
chosenRandom = random.choice(randomWord) # randomizes the selection of fruits

hidddenWord = ["_"] * len(chosenRandom) # makes the randomized word into _'s

while incorrectGuesses < maxIncorrectGuesses and "_" in hidddenWord:
    print("current word:", displayWordState(hidddenWord))
    # while you still have guesses left this will play but if you run out then it will say you failed if not it will run until you complete
    guessedLetter = input("Input your guessed letter: ").lower()

    if len(guessedLetter) == 1 and guessedLetter.isalpha(): # Check if the guessed letter is a single alphabetical character
        newWordState = wordUpdated(chosenRandom, guessedLetter, hidddenWord) # Call the wordUpdated function to update the guessed word state with the new guessed letter

        if newWordState == hidddenWord: # Check if the guessed letter did not reveal any new letters in the word
            incorrectGuesses += 1 # Increment the count of incorrect guesses
            print(f"Incorrect guess! You have {maxIncorrectGuesses - incorrectGuesses} tries left.") # Display how many incorrect guesses are remaining

        else:
            hidddenWord = newWordState # Update the hidden word state with the new revealed letters
            print("Correct!") # Notify the player that their guess was correct


    else:
        print("Please enter a valid letter")

if "_" not in hidddenWord:
    print("\ncurrent word:", displayWordState(hidddenWord))
    print(f"Congratulations! You've guessed the word: {''.join(hidddenWord)}")
else:
    print(f"Sorry, you've run out of guesses. The word was: {chosenRandom}")