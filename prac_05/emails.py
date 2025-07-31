""" a program that stores users' emails (unique keys) and names (values) in a dictionary. """

def extract_name_from_email(email):
    # Extracts and formats name from the email username part.
    username = email.split('@')[0]
    name_parts = username.split('.')
    name = " ".join(part.title() for part in name_parts)
    return name

def main():
    #Store emails and names in a dictionary, prompt for confirmation, and print the result.
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name_guess = extract_name_from_email(email)
        confirmation = input(f"Is your name {name_guess}? (Y/n) ").lower()
        if confirmation != "y" and confirmation != "":
            name_guess = input("Name: ")
        email_to_name[email] = name_guess
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

main()
