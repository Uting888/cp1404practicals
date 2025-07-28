
# Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output)
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result.
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# code that prints the total for all lines in numbers.txt.
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
print(total)
