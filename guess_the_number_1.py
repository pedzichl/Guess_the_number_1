from random import randint

def input_type():
    """
    get number from user
    :rtype: int
    :return: given number converted to int
    """
    while True:
        guess = input("Guess the number from 1 to 100: ")
        try:
            guess = int(guess)
            if guess >= 1 and guess <= 100:
                break
            else:
                print("Your guess should be a number from 1 to 100!")
        except ValueError:
            print("It is not a number!")
    return guess

def user_value():
    """ main function of the game. """
    winning_num = randint(1, 100)
    guess = input_type()
    while guess != winning_num:
        if guess > winning_num:
            print("Too big!")
        else:
            print("Too small!")
        guess = input_type()
    print("You win!")



if __name__ == '__main__':
    user_value()



