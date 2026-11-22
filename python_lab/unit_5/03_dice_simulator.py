import random

print("DICE SIMULATOR")

while True:
    choice = input("\nPress Enter to roll the dice or Q to quit: ")

    if choice.lower() == "q":
        print("Thank you for playing")
        break

    dice = random.randint(1, 6)

    print(f"Dice Rolled: {dice}")
