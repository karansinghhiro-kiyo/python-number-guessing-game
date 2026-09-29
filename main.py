import random

number = random.randint(1, 100)
attempts = 0

while True:

    guess = int(input("🎯 Guess a number: "))
    attempts += 1

    if guess == number:
        print("You won!! 🎉🏆")
        print("Attempts:", attempts)
        break

    elif guess > number:
        print("Too high!! 🔼")

    else:
        print("Too low!! 🔽")