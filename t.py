def popular_words_message(messages, word):
    """
    Read in files and return a tuple with the index of the line that contains
    the input word most often and its count. Return a tuple of two zeros if
    the input word can not be found.

    >>> popular_words_message("files/Message_1.txt", "to")
    (9, 3)
    >>> popular_words_message("files/Message_2.txt", "happy")
    (8, 4)
    >>> popular_words_message("files/Message_3.txt", "DSC20")
    (0, 0)
    >>> popular_words_message("files/Message_3.txt", "secret")
    (8, 1)
    """
    with open(messages, 'r') as f:
        for line in f:
            a = line.strip('\n').split()
    return a

print(popular_words_message("lab03,files/Message_1.txt", "to"))