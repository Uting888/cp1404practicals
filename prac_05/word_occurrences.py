""" a program to count the occurrences of words in a string."""


text = input("Text: ")

words = text.split()
word_to_count = {}

# Count word occurrences
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

sorted_words = sorted(word_to_count.items())
max_length = max(len(word) for word in word_to_count)

for word, count in sorted_words:
    print(f"{word:{max_length}} : {count}")
