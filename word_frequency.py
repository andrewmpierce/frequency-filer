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
    return freq[0:20]

if __name__ == '__main__':
    main("sample.txt")

#Problem: Program is return a LIST of tuples,
#not a dictionary with values, tests are looking for dictionary
# Test is looking for number output
