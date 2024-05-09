import random

def guessing_game():
    # Generate a random number between 1 and 100
    number = random.randint(1,100)
    player_name = input("Hola, What's your name?")
    num_guesses = 0

    print(player_name + ', I am thinking of a number between 1 and 100. Can you guess it?')

    while num_guesses < 10:
        guess = int(input())
        num_guesses += 1
        if guess < number:
            print('Your guess is too low')
        elif guess > number:
            print('Your guess is too high')
        else:
            break

    if guess == number:
        print('Congrats, ' + player_name + '! You guessed the number in ' + 
              str(num_guesses) + ' tries.')
    else: 
        print("You lost " + player_name + "! The number I guessed was " + str(number))

guessing_game()

