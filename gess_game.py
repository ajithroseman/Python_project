import random
low = int(input("Starting low number :"))
high = int(input("Ending high number :"))

random_number = random.randrange(low,high)
chance = 10
guess_counter = 0
while guess_counter < chance:
    guess_counter = guess_counter + 1
    guess = int(input(f"{guess_counter}.""Guess is :"))
    if guess_counter>=chance and guess != random_number:
        print("You guessed it WRONG !!! Better try next time ")
        print("Correct Number is",random_number)
        break
    elif guess < random_number:
        print("Too low")
    elif guess > random_number:(
        print("Too high"))
    elif guess == random_number:
        print("You have guessed it RIGHT")
        break

