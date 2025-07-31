
FILENAME = "wimbledon.csv"


def load_wimbledon_data(filename):
    # Load Wimbledon data from CSV file.
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        data = [line.strip().split(",") for line in in_file]
    return data


def count_champions(data):
    # Count how many times each player has won
    champion_to_count = {}
    for row in data:
        champion = row[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count


def get_countries(data):
    # Return a set of all countries that have won Wimbledon.
    return sorted({row[1] for row in data})


def main():
    # Display Wimbledon champion summary report.
    data = load_wimbledon_data(FILENAME)
    champions = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
