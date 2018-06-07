import random

n = 0
random.seed(100)

while n < 20:
    random_number = random.randint(1,10)
    n = n + 1
    guessed_number = int(raw_input("Guess a number (from 1 to 10): "))
    print 'The number is...', guessed_number
    if guessed_number == random_number:
        print 'That is correct'

    if guessed_number < random_number:
        print 'That number is too low'

    if guessed_number > random_number:
        print 'That number is too high'
