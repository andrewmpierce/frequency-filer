import re

def file(link):
    file = open(link)
    sample = file.read()
    return sample

def word_frequency(string):
    words = re.sub(r'[^A-Za-z0-9 ]', ' ', string).lower().split()
    print(words)
    worddict = {}
    for word in words:
        if word not in worddict:
            worddict[word] = int(1)
        else: worddict[word] += 1
    return print(worddict)





word_frequency(file("sample.txt"))
