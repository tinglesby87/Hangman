import os
import random
import sys


#Let user know how many letters word contains



#Let user know if guess appears on computer's word
#Display partially guessed word and underscores for letters that have not been guessed
#More than one guess, display error input is invalid try again
#Let user choose difficulty level at beginning of program (Easy: 4-6, M: 6-10, H: 10+ characters)
#Add loop so when game mode ends, user asked if they want to play again and game begins again



list = [
    "Wizards",
    "Kings",
    "Celtics",
    "Pistons",
    "Suns",
    "Lakers",
    "Blazers",
    "Pelicans",
    "Magic",
    "Sixers"
    "Knicks",
    "Nets",
    "Warriors",
    "Spurs",
    "Jazz",
    "Rockets",
    "Grizzlies",
    "Mavericks",
    "Clippers",
    "Bulls",
    "Hawks",
    "Heat",
]

def clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')

bad_guesses= []
good_guesses=[]
guess = input("Guess a letter:").lower()
secret_word = random.randchoice("team", list)


def draw(bad_guesses, good_guesses, secret_word):
    for letter in guess:
        if letter in good_guesses:
            print(letter, end="")
        else:
            print('_', end='')

def play(done):
    clear()
    secret_word = random.randchoice("team", list)
    #bad_guesses = {}
    #good_guesses ={}

    while True:
    difficulty_box = input("Please enter a difficulty_level = 1= Easy, 2 = Medium, 3 = Hard ")
    try:
        difficulty_box = str(difficulty_box)
        break
    except ValueError:
        print("Gimme a number")

def math_quiz(min_num, max_num):
    for _ in range(answer_box):
        x= random.randint(min_num, max_num)
        y= random.randint(min_num, max_num)
        product = x*y
        input_box= int(input("{} * {} = ".format(x, y)))
        if  input_box == product :
            print("That is correct")
        else:
            print("Oops! That's incorrect")

if difficulty_box == 1:
    secret_word(1,5)

elif difficulty_box == 2:
    secret_word(2,10)

else:
    secret_word(5,25)




def get_guess(bad_guesses, good_guesses):
    guess = input("Guess a letter:").lower()
    while True:      #added while loop, loop will run on its own, don't need continues
       if len(guess) != 1:
           print("You can only guess a single letter")
       elif guess in bad_guesses or guess in good_guesses:
           print("You've already guessed that letter!")
       elif not guess.isalpha():
           print("You can only guess letters!")
       else:
           return guess
    while True:
        start =input("Press enter_return to start, or enter q to quit")
        if start.lower() == "q":
            while len(bad_guesses) < 7 and len(good_guesses) != len(secret_word):
                if letter in good_guesses:
                    print(letter, end = '_')
                else:
                    print('_', end= '')
            print('Strikes: {}/7'.format(len(bad_guesses)))
            print("")
            if len(guess) != 1:
                print("You can only guess a single team")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
    while True:
        draw(bad_guesses, good_guesses, secret_word)
        good_guesses.append(guess)
        found = True
        for letter in secret_word:
            if letter not in good_guesses:
                found = False
            if found:
                print("You win!")
                print("The secret word was ",{}.format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses)==7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost")
                print("The secret word was ",{}).format(secret_word)
                done = True


        if done:
            play_again = input("Play again? Y/n").lower()
            if play_again != "n":
                return play #(done=False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to quit").lower()
    if start == 'q':
        print("Bye")
        sys.exit()
    else:
        return True

print("Welcome to Letter Guess")

done = False

while True:
    clear()
    welcome()
    play(done)


while True:
    start = input("Press enter/return to start, or Q to quit")
    if start.lower() == 'q':










