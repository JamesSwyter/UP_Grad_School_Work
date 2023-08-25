import re
import pandas as pd


def analyzeWords(words):
    """
    Function analyzing text data from a Panda.Series
    :param words: a Panda.Series of words
    :return: A dictionary with metrics about the words
    """

    # initiate char_count_list
    char_count_list = [len(i) for i in words]

    # initiate size counts dictionary
    max_char = max(char_count_list)
    size_counts = {}
    for i in range(1, max_char+1):
        size_counts[i] = 0

    # Initiate oo list, list of >= 6 letter words, and letter counts dictionary
    oo_list = []
    oo_index = []
    six_letter_list = []
    six_letter_index = []
    letter_counts_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
                          'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
                          'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # Go through each word, fill out the lists and dictionary above
    for i in words:

        if len(i) > 5:
            six_letter_list.append(i.lower())
            six_letter_index.append(words[words == i].index[0])

        letter_key = i[0].lower()
        letter_counts_dict[letter_key] += 1

        size_counts[len(i)] += 1

        match_object = re.search('oo', i)

        if match_object:
            oo_list.append(i)
            oo_index.append(words[words == i].index[0])

    words_6plus_count = len(six_letter_list)
    oo_count = len(oo_list)

    # List of oo words and 6+ letter words are returned as a series
    six_letter_series = pd.Series(six_letter_list, six_letter_index)
    oo_series = pd.Series(oo_list, oo_index)

    # Create dictionary with all metrics to be returned
    metric_dict = {'letter_counts': letter_counts_dict, 'max_char': max_char, 'size_counts': size_counts,
                   'oo_count': oo_count, 'oo_words': oo_series, 'words_6plus': six_letter_series,
                   'words_6plus_count': words_6plus_count}

    return metric_dict
