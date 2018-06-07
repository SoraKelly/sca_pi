import random
import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)
led_pin = 11
buzz_pin = 32
GPIO.setup (buzz_pin,GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(2)

random.seed(100)
n = random.randint(1,10)
while True:
    guess = int(raw_input('Guess a number between 1 and 10:'))
    guess = int(guess)
    if guess < n:
        print 'guess is too low'
        Buzz.start(50)
        time.sleep(1)
        Buzz.stop()
    elif guess > n:
            print 'guess is too high'
            Buzz.start(50)
            time.sleep(1)
            Buzz.stop()

    else:
            print 'you guessed it'
            GPIO.output(led_pin, True)
            time.sleep(2)
            GPIO.output(led_pin, False)
            GPIO.cleanup(1)
            break
