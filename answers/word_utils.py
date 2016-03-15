#!/usr/bin/env python3

from urllib import request

def fetch_words(url="http://sixty-north.com/c/t.txt"):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of string containing the words from the document.
    """
    story = request.urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    return story_words


def print_items(items):
    """ Print items one per line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)
