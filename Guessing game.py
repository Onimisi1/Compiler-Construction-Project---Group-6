from random import randint

GameOn = True
while GameOn:
    aiguess = randint(0, 11)
    try:
        myguess = int(input('Guess a number between 0 to 11:\n'))
        if myguess < 0 or myguess > 11:
            print(f'Please choose a number between 0 to 11')
            continue
    except:
        print("Please put in a number")
        continue

    if myguess == aiguess:
        print("You are smart!")
        play_again = input("Would you like to play again ? Y/N ").lower()
        if play_again.startswith('y'):
            continue
        else:
            GameOn = False
    else:
        print(f'The correct guess is {aiguess}.Try again!')
        play_again = input("Would you like to play again ? Y/N ").lower()
        if play_again.startswith('y'):
            continue
        else:
            GameOn = False



