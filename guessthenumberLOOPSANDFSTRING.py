import random

def guessnumber(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('You have guessed wrong, try something higher.')
        elif guess > random_number:
            print('You have guessed wrong, try something lower.')
        

    print(f'Congrats!!! You have guessed the {random_number} correctly.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high: #this is for; if we call the function with equal low and high, so it won't give an error.
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1 # so this means, when we let computer that it's guess was high (h, hence feedback == h), 
                             # we want to adjust the upper bound of the guess on (guess = random.randint(low, high)) so it can guess again with the new info it got from us.
                             # it is guess - 1 because if it's guess is higher then our number. It should guess between low and new number (which is guess - 1)
        elif feedback == 'l':
            low = guess + 1 # same logic

    print(f'Yay, the computer guessed the number, {guess}, correctly!')

computer_guess(100)
        