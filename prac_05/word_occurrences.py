"""

Word Occurrences
Estimate: 20 minutes
Actual: 25 minutes
"""
word_to_count = {}
text = input("Text: ")
print(text)
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
print(word_to_count)

words = list(word_to_count.keys())
words.sort()

max_length = max(len(words) for word in words)
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")







