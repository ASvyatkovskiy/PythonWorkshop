#!/usr/bin/env python
from urllib2 import urlopen

def fetch_words():
    story = urlopen("http://sixty-north.com/c/t.txt").read()
    story_words = []
    for line in story.split('\n'):
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print item
