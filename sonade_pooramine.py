def poora_soned(words):
    if not isinstance(words, list):
        raise TypeError("Input argument must be a list")
    for word in words:
        if not isinstance(word, str):
            raise TypeError("All elements in the list must be strings")
    return [word[::-1] for word in words]

words = ['hello', 'world', 'python']
reversed_words = poora_soned(words)
print(reversed_words)