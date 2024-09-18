from wonderwords import RandomWord
import random

SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_WRONG_GUESSES = 7
SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \\( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

def get_letter_from_user(snowman_dict, wrong_guesses_list):
    while True:
        user_input_string = input("\nPlease guess a letter: ").lower()
        print()

        if not user_input_string.isalpha(): 
            print(f"\"{user_input_string}\" is invalid input. A guess must be a letter.")
        elif len(user_input_string) > 1:
            print(f"\"{user_input_string}\" is invalid input. A guess must be a single letter.")
        elif user_input_string in snowman_dict is False or user_input_string in wrong_guesses_list:
            print(f"You have already guessed the letter {user_input_string}. Please guess another letter.")
        else:
            break
    
    return user_input_string

def build_word_dict(word):
    word_dict = {}

    for letter in word:
        if letter not in word_dict:
            word_dict[letter] = False

    return word_dict

def snowman():
    r = RandomWord()
    snowman_word = r.word(word_min_length = SNOWMAN_MIN_WORD_LENGTH, word_max_length = SNOWMAN_MAX_WORD_LENGTH)
    snowman_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []
    wrong_guesses_num = 0

    print(f"Welcome to Snowman, a game where you guess letters of a word. Once you reach {SNOWMAN_WRONG_GUESSES} wrong guesses, you lose!")

    while wrong_guesses_num < SNOWMAN_WRONG_GUESSES and not get_word_progress(snowman_word, snowman_dict):
        user_input = get_letter_from_user(snowman_dict, wrong_guesses_list)

        if user_input in snowman_dict:
            if not snowman_dict[user_input]:
                snowman_dict[user_input] = True
                print(f"Great job, the letter {user_input} is in the word!")
            else:
                print(f"You have already guessed the letter {user_input}. Please enter another letter.")
        else:
            wrong_guesses_list.append(user_input)
            wrong_guesses_num += 1
            print(f"The letter {user_input} is not in the word.")

        print_snowman(wrong_guesses_num)
        print_word_progress_string(snowman_word, snowman_dict)

        if wrong_guesses_num == (SNOWMAN_WRONG_GUESSES - 1):
            print(f"\nYou have incorrectly guessed {wrong_guesses_list} with 1 wrong guess left.")
        elif wrong_guesses_num > 0:
            print(f"\nYou have incorrectly guessed {wrong_guesses_list} with {SNOWMAN_WRONG_GUESSES - wrong_guesses_num} wrong guesses left.")

    if get_word_progress(snowman_word, snowman_dict):
        if wrong_guesses_num == 1:
            print(f"\nCongratulations, you won with {wrong_guesses_num} wrong guess! :) You correctly guessed the word {snowman_word}.\n")
        else:
            print(f"\nCongratulations, you won with {wrong_guesses_num} wrong guesses! :) You correctly guessed the word {snowman_word}.\n")
    else:
        print(f"Unfortunately, you have lost. :( The word was {snowman_word}.\n")
    
def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])

def print_word_progress_string(word, word_dict):
    guesses_string = ""
    letter_num = 0

    for letter in word:
        if letter_num > 0:
            guesses_string += " "
        if not word_dict[letter]:
            guesses_string += "_"
        else:
            guesses_string += letter
        
        letter_num += 1
    
    print(guesses_string)

def get_word_progress(word, word_dict):
    for letter in word:
        if not word_dict[letter]:
            return False

    return True