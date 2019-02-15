

import string


def unique_words(filename):

    hist = histogram(filename)
    mylist = list(hist)
    mylist =  list(dict.fromkeys(mylist))

    return mylist



def count_the_article(filename):

    count = 0
    list_2 = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    hist = histogram(filename)
    for item in list_2:
        if item in hist:
            count += 1

    return count


def sorted_words(filename):

    hist = dict()
    file = open('filename')
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = len(word)
    lst = [(value, key) for key, value in hist.items()]
    lst.sort(reverse=True)

    return lst


def character_word_count(filename):


def starts_with_vow(filename):




def histogram(filename):

    hist =dict()
    file = open('filename')
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = hist.get(word, 0) + 1

    return hist
