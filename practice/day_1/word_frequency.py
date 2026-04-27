words = ["apple", "banana", "apple", "orange", "banana", "apple"]

words_count = {}

for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1

print(words_count)