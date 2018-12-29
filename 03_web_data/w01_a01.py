# Sample program to demonstrate editor installation


def word_count(text):
    words = text.split()
    counter = dict()
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter


text = 'The rain in Spain stays mainly in the plains'
print(word_count(text))
