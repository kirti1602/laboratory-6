# Find words that are longer than n from a given list of words
words = ['apple', 'banana', 'cherry', 'kiwi', 'orange']
n = 5
long_words = [word for word in words if len(word) > n]
print("Words longer than", n, "characters:", long_words)
