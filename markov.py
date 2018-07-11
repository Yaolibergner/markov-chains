"""Generate Markov text from text files."""

from random import choice

import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as filename:

        string_of_file = filename.read()

        return string_of_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
 
    words = text_string.split()

    words.append(None)
    

    for i in range(len(words) - 2):
        key = tuple([words[i], words[i + 1]])
        possible_word = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(possible_word)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    keys = list(chains.keys())
    search_key = ()

    while True: 
        if search_key == ():
            search_key = choice(keys)
            for word in search_key:
                words.append(word)

        rand_word = choice(chains[search_key])
        words.append(rand_word)
        
        search_key = (search_key[1], rand_word)

        if chains[search_key] == [None]:
            break

    return " ".join(words)


input_path = sys.argv[-1]
# import pdb; pdb.set_trace()

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)


