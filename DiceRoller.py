import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))
print("Rolling the dice...")
result = roll_dice(sides)
print(f"The result is: {result}")
