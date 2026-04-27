text = "python makes logic easy when practice is consistent"

text_1 = text.split()
longest_word = ""

for word in text_1:
    if len(word) > len(longest_word):
        longest_word = word

'''
count = 0
count_1 = 0

for word in text_1:
    for char in word:
        count += 1
        if count > count_1:
            longest_word = word

'''

print(longest_word)
