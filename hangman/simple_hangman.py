import random
import math

word_dict =       ['bulbasaur',
                   'ivysaur',
                   'venusaur',
                   'squirtle',
                   'wartortle',
                   'blastoise',
                   'charmander',
                   'charmeleon',
                   'charizard',]

guess_word = word_dict [math.floor(random.random() * len(word_dict))]
gameOn = True

guess_array = list(len(guess_word) * '*')

max_attempts = 5

guess_count = 0

print("")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Pokemon Original starters game !")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("")

while(gameOn):
    print("".join(guess_array))
    print("chances left: " , max_attempts - guess_count)
    current_guess = input("Enter your guess : ")
    if (current_guess in guess_word):
        print("Good guess!")

        for i in range(0, len(guess_word)):
            if(guess_word[i]  == current_guess):
                guess_array[i] =  current_guess

        #guess_array[guess_word.index(current_guess)] = current_guess
        if (list(guess_word) == guess_array) :
            print("You have won!")
            print("The answer is ", guess_word)
            gameOn = False
    else :
        print(" That character is not in the answer.")
        guess_count += 1
        if (guess_count == max_attempts):
            print("You loose.")
            gameON = False

    print("\n")


    




