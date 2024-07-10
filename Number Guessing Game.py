print("Guess a number between 1 and 10")

import random

number = random.randint(1, 10)

while True:
  
  guess = int(input("Guess your number; "))
  
  if guess == number:
    print("You're correct! Congratulations! :D")
    break
  elif guess < number:
    print("Too low! :(")
  elif guess > number:
    print("Too high! :(")