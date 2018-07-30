# -*- codind: utf-8 -*-
def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sort the words"""
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)
    print word
    return

def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)
    print word
    return

def sort_sentence(sentence):
    """takes a full sentence and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last_word(sentence):
    """print first and last word about sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the wprds then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
