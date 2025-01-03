import random 

# Welcome and difficulty messages
welcomeMsg = """ Welcome to this Number Guessing Game! Your mission is to simply guess the number that I am thinking of!
These are the rules:
1. You have only a certain number of chances based on the difficulty.
2. If you guess correctly, congratulations!
3. If you don’t guess correctly, the game will tell you if the number is greater or less than your guess.
"""

selectDifficultyMsg = """Select your difficulty level by typing the number: 
0. Easy - 10 tries
1. Medium - 5 tries
2. Hard - 3 tries 
"""

# List of difficulties
listOfDifficulties = [8, 5, 3]

# Game function
def runGuessingGame(): 
    print(welcomeMsg)
    
    # Input validation for difficulty selection
    while True:
        selectedDifficulty = input(selectDifficultyMsg).strip()

        if selectedDifficulty.isdigit() and int(selectedDifficulty) in [0, 1, 2]:
            selectedDifficulty = int(selectedDifficulty)
            break
        else:
            print("Invalid input! Please enter a number (0, 1, or 2).")

    totalTries = listOfDifficulties[selectedDifficulty]
    numberOfTriesLeft = totalTries

    selectedNumber = random.randint(1, 100)  # Generates a random number between 1-100

    # Guess - inputs and validations
    for attempt in range(1, totalTries + 1):
        while True:
            guess = input(f"Attempt {attempt}/{totalTries}: Enter your guess: ").strip()

            if guess.isdigit():
                guess = int(guess)
                break
            else:
                print("Invalid input! Please enter a valid number.")     

        if guess < selectedNumber: 
            print(f"Nope! The magic number is greater. Tries left: {numberOfTriesLeft - 1}")
        elif guess > selectedNumber:
            print(f"Nope! The magic number is lesser. Tries left: {numberOfTriesLeft - 1}")
        else: 
            print("Congrats! You got it right!")
            break
            
        numberOfTriesLeft -= 1

    else: 
        print(f"Oh! You didn't guess :( The correct number was {selectedNumber}. Good luck next time!")        

# Main game loop
while True:
    runGuessingGame()
    tryAgain = input("Wanna try again? Yes or no: ").strip().lower()
    if tryAgain != "yes":
        print("Thanks for playing! Goodbye!")
        break
