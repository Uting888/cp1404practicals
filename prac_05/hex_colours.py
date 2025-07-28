
# Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get the code
COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Beige": "#f5f5dc",
    "Coral": "#ff7f50",
    "DarkGreen": "#006400",
    "GoldFusion": "#85754e",
    "HotPink": "#ff69b4",
    "Indigo": "#4b0082",
    "Jasmine": "#f8de7e"
}

def main():
    colour_name = input("Enter colour name: ").strip().upper()
    while colour_name != "":
        if colour_name in COLOUR_CODES:
            print(f"{colour_name.title()} is {COLOUR_CODES[colour_name]}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").strip().upper()

main()