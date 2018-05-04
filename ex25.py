def break_words(stuff):
    """This function will break-up words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the individual words"""
    return sorted(words)

def print_first_word(words):
    """This will return/pop the first word of sentence"""
    words = words.pop(0)
    return words

def print_last_word(words):
    """This function will pop the last word"""
    words = words.pop(-1)
    return words

def sort_sentence(sentence):
    """This function will return the sorted words from a sentence"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """This function will print the first and the last word from the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """This function will print the first and the last word from the sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
