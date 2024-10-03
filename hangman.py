import random
from hangmanwords import WordList
from hangmanart import stages, logo

Lives = 6

print(logo)

ChosenWord = random.choice(WordList)

Placeholder = ""

WordL = len(ChosenWord)

for position in range(WordL):
    Placeholder += "_"

print("The word is: ",Placeholder)

GameOver = False

CorrectL = []

while not GameOver:
    Guess = input("\nGuess a letter: ").lower()

    if Guess in CorrectL:
        print(f"You've alredy guessed {Guess}")

    Display = ""

    for Letter in ChosenWord:
        if Letter == Guess:
            Display += Letter
            CorrectL.append(Guess)
        elif Letter in CorrectL:
            Display += Letter
        else:
            Display += "_"

    print("Word to guess: " + Display)

    if Guess not in ChosenWord:
        Lives -= 1
        print(f"You guessed {Guess}, that's not in the word. You lose a life.")
        if Lives == 0:
            GameOver = True
            print(f"You let the man get hanged. The word was {ChosenWord}.")

    if "_" not in Display:
        GameOver = True
        print("You saved the man from being hanged. Congratulations!!")

    print(stages[Lives])

exit = input("Press ENTER to exit the game")