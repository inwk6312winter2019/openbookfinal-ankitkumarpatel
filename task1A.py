

import string


def unique_words(filename):

    hist = histogram(filename)
    mylist = list(hist)
    mylist =  list(dict.fromkeys(mylist))

    return mylist



def count_the_article(0):




def sorted_words(0):





def character_word_count(0):


def starts_with_vow():




def histogram(filename):

    hist =dict()
    file = open('filename')
    for line in file:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation + string.whitespace).lower()
            hist[word] = hist.get(word, 0) + 1

    return hist
