import random
from fruits import fruits

# Prompt user to choose a difficulty level by number
Difficulty= input(""" 
Welcome to word guesser
1. Very Easy -- 12 Guesses
2. Easy -- 9 Guesses
3. Medium -- 6 Guesses
4. Hard -- 3 Guesses
Choose a Difficulty: """).strip()  # Get the user's input and strip any extra spaces

levels = ['Very Easy', 'Easy', 'Medium', 'Hard']

incorrectGuesses = 0
maxIncorrectGuesses = 12  # Default max guesses for

while True:
    try:
        # Check the user's input and map it to the correct difficulty level
        if Difficulty == '1':
            print(f"\n{levels[0]} Selected")
            break
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

    except ValueError:
        print("Invalid input. Please try again.")

def wordUpdated(chosenRandom, guessedLetter, wordState):
    updatedWordState = wordState[:] # Create a copy of the word state and resues it
    for i, letter in enumerate(chosenRandom):
        if letter.lower() == guessedLetter.lower(): # Check for match (case-insensitive)
            updatedWordState[i] = letter # Replace the underscore with the letter if correct -- runs through the index to check if letter is correct
    return updatedWordState

def displayWordState(wordState):
    return " ".join(wordState) #seperates Characters

randomWord = fruits
chosenRandom = random.choice(randomWord)

hidddenWord = ["_"] * len(chosenRandom)

while incorrectGuesses < maxIncorrectGuesses and "_" in hidddenWord:
    print("current word:", displayWordState(hidddenWord))

    guessedLetter = input("Input your guessed letter: ").lower()

    if len(guessedLetter) == 1 and guessedLetter.isalpha():
        newWordState = wordUpdated(chosenRandom, guessedLetter, hidddenWord)

        if newWordState == hidddenWord:
            incorrectGuesses +=1
            print(f"inncorect {maxIncorrectGuesses - incorrectGuesses}.")

        else:
            hidddenWord = newWordState
            print("Correct!")

    else:
        print("Please enter a valid letter")

if "_" not in hidddenWord:
    print("\ncurrent word:", displayWordState(hidddenWord))
    print(f"Congratulations! You've guessed the word: {''.join(hidddenWord)}")
else:
    print(f"Sorry, you've run out of guesses. The word was: {chosenRandom}")