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
    ignored_words = ['a', 'the', 'you', 'he', 'she', 'it', 'for']
    words = re.sub(r'[^A-Za-z0-9 ]', ' ', string).lower().split()
    freq = {}
    for word in words:
        if word not in ignored_words:
            if word not in freq:
                freq[word] = 1
            else: freq[word] += 1
    for word in ignored_words:
        if word in freq:
            del freq[word]
    return freq

if __name__ == '__main__':
    main("sample.txt")
