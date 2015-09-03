import re

def main(link):
    file = open(link)
    sample = file.read()
    print(word_frequency(sample))

def word_frequency(string):
    words = re.sub(r'[^A-Za-z0-9 ]', ' ', string).lower().split()
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else: freq[word] += 1
    freq = sorted(freq.items(), key = lambda c: c[1], reverse = True)
    freq = freq[0:20]
    freq = dict(freq)
    return freq

if __name__ == '__main__':
    main("sample.txt")

#Returns a dict of top 20 used words, NOT in order,
#b/c dicts are unordered
# test fails if example is not in top 20
#Options: Figure out how to order dictionary & preserve full contents
#Figure out how to return numbers in word_frequency and list contents through main
