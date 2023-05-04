import string

def word_frequency(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.translate(str.maketrans("", "", string.punctuation))
            line = line.lower()
            words = line.split()
            for word in words:
                if word.isalpha():
                    word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

filename = "word_freque.txt"
word_freq = word_frequency(filename)
print(word_freq)