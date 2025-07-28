import random

NUMBER_OF_NUMBERS = 6
MIN = 1
MAX = 45

number_of_picks = int(input("How many quick picks? "))

for _ in range(number_of_picks):
    quick_pick = []
    # Generate 6 unique random numbers
    while len(quick_pick) < NUMBER_OF_NUMBERS:
        number = random.randint(MIN, MAX)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()

    # Print numbers aligned in 2-character wide fields
    print(" ".join(f"{num:2}" for num in quick_pick))
