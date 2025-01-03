# CLI Number Guessing Game
A little challenge from https://roadmap.sh/projects/number-guessing-game. 

## Brief Description 

This script implements a simple CLI number-guessing game, the kind you played when you were a kid. A short and fun project to go back to the basics.

The player's goal is to guess a randomly generated number within a range based on a selected difficulty level. The game provides feedback to guide the player toward the correct answer.

### An Example Match

```text
Welcome to this Number Guessing Game! Your mission is to simply guess the number that I am thinking of!
These are the rules:
1. You have only a certain number of chances based on the difficulty.
2. If you guess correctly, congratulations!
3. If you don’t guess correctly, the game will tell you if the number is greater or less than your guess.

Select your difficulty level by typing the number: 
0. Easy - 8 tries
1. Medium - 5 tries
2. Hard - 3 tries 
>> 1
Attempt 1/5: Enter your guess: 50
Nope! The magic number is greater. Tries left: 4
...
Congrats! You got it right!
Wanna try again? Yes or no: no
Thanks for playing! Goodbye!
```


## Setup
Clone the repo to your local machine and try it yourself!

## Features

1.Difficulty Levels:
  Easy: 8 attempts
  Medium: 5 attempts
  Hard: 3 attempts

2.Hints:
The game provides feedback indicating whether the target number is greater or less than the player's guess.

3.Replayability:
Players can replay the game after each session or exit by responding appropriately to a prompt.

4.Input Validation:
  Ensures players provide valid inputs for difficulty level and guesses.

5. Feedback Mechanism:
  Guides the player by informing whether the target number is greater or lesser than the current guess.

6.Replay Prompt:
Prompts the player to decide whether to play another round or exit.
