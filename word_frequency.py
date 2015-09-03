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
            freq[word] = int(1)
        else: freq[word] += 1
    freq = sorted(freq, key = freq.get, reverse = True)
    return freq[0:20]

if __name__ == '__main__':
    main("sample.txt")
