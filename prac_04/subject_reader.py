"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            # Convert student count to int
            parts[2] = int(parts[2])
            subject_data.append(parts)
    return subject_data


def display_subject_details(data):
    for subject_code, lecturer, student_count in data:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()
