#!/usr/bin/env python
""" Retrieve and print words from a URL.

Usage:

    python3 driver.py<URL>
"""

import sys
from urllib import request
from word_utils import * #fetch_words,print_items


def main(url):
    """ Print each word from a text document from a URL.

    Args:
        url:  The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # The 0th argument is the module filename
