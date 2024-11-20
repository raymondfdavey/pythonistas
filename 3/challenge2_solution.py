import random # A library that contains random number functions and methods


def generate_answer():
    """Returns a random number in the range 1 to 99 inclusive"""
    x = random.randrange(98) + 1  # from 1 to 99
    return x

def check_previous(guess, my_list):
    """Takes a list of user guesses and the current user guess and return
    True is the user guess is already in that list, False otherwise.
    """
    x = 0
    while x < len(my_list):
        if my_list[x] == guess:
            return True
        else:
            x += 1
    return False

def analyse_guess(guess, answer):
    """Takes the user guess as parameters and return s-1
    if it is too low, -2 is if it is too high
    and 0 if it is correct.
    """
    if guess == answer:
        return 0
    elif guess > answer:
        return -2
    else:
        return -1


# Starting point for the program...
def main():
    answer = generate_answer()
    attempts = 0
    all_attempts = []  # List of all guesses made
    game_over = False
    guess = 0

    while game_over is False:
        guess = int(input('Enter your guess: '))
        if guess == -1:
            print('Thanks for playing!')
            game_over = True
            quit(0)  # Ends the program

        if check_previous(guess, all_attempts) is False:
            all_attempts.append(guess)
            x = analyse_guess(guess, answer)
            if x == 0:
                print('Well done - you win!!')
                game_over = True
            elif x == -2:
                print('Too high!!')
                attempts += 1
            elif x == -1:
                print('Too low!!')
                attempts += 1

        else:
            print('tried that already!!!')

        if attempts == 10:
            print('Out of turns!')
            print('The correct answer was: ', answer)
            print('Better luck next time!')
            game_over = True

if __name__ == "__main__":
    main()
