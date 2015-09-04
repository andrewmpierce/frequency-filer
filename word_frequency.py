import re

def main(link):
    file = open(link)
    sample = file.read()
    return loop(word_frequency(sample))


def loop(dictionary):
    counter = 0
    sorted_list = sorted(dictionary.items(), key = lambda c: c[1], reverse = True)
    for x in range(20):
        print(sorted_list[counter][0] + ' ' + str(sorted_list[counter][1]))
        counter += 1


def word_frequency(string):
    words = re.sub(r'[^A-Za-z0-9\s]', '', string).lower().split()
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else: freq[word] += 1
    return freq

if __name__ == '__main__':
    main("sample.txt")
