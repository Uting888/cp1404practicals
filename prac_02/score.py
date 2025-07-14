"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    random_score = random.uniform(0, 100)
    print(f"Random score is {random_score:.2f}")
    print(determine_score_status(random_score))


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()