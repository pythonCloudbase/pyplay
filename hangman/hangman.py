import random
import time
 
HANGMANPICS = ["""

  +---+
  |   |
      |
      |
      |
      |
===========""","""
  +---+
  |   |
  o   |
      |
      |
      |
===========""","""
  +---+
  |   |
  o   |
  |   |
      |
      |
===========""","""
  +---+
  |   |
  o   |
 /|   |
      |
      |
===========""","""
  +---+
  |   |
  o   |
 /|\  |
      |
      |
===========""","""
  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
===========""","""
  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
==========="""
]

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS,missedLetters,correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:',end='')
    for letter in missedLetters:
        print(letter,end='')
    print()

    blanks = '_'*len(secretWord)

    for i in range( len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i]+ secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter,end='')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('You have already chosen that letter once, short term memory, huh?')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Guess one of the letters in the alphabet, you dimwit.')
        else :
            return guess

def playAgain():
    print('Wanna go again? (who else you want to get hanged today?)')
    return input().lower().startwith(y)

print('H A N g M A N')
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range (len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes! The secret word is ' + secretWord +'. You have won.')
                time.sleep(3)
                print('Hope you are happy. Whoo the beeping hoo.')
                time.sleep(2)
                print('Another criminal goes scottfree')
                time.sleep(1)
                print('So thank you.')
                gameIsDone = True
            else:
                missedLetters = missedLetters + guess

                if len(missedLetters) == len(HANGMANPICS) - 1:
                    displayBoard(HANGMANPICS, missedLetters,correctLetters,secretWord)
                    print("Would you look at that. You are out of chances buddy.")
                    time.sleep(2)
                    print("You planned another innocents funeral.")
                    time.sleep(1)
                    print("Good job.")
                    gameIsDone = True

                if gameIsDone:
                    if playAgain():
                        missedLetters=""
                        correctLetters=""
                        gameIsDone = False
                        secretWord = getRandomWord(words)
                    else:
                        break