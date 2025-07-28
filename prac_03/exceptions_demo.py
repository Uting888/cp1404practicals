"""
CP1404/CP5632 - Practical
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid integers!")
print("Finished.")


# Answer the following questions:
# 1. When will a ValueError occur? The user enters non-integer (e.g. 'abc', 2.5).
# 2. When will a ZeroDivisionError occur? The user enters 0 as the denominator.
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes. Use a loop to re-prompt the user until they enter a non-zero denominator.