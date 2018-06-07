import random

random.seed(100)
n = random.randint(1,10)
while True:
    guess = int(raw_input('Guess a number between 1 and 10:'))
    if guess < n:
        print 'guess is too low'
    else:
        if guess > n:
            print 'guess is too high'
        else:
            print 'you guessed it'
            break
