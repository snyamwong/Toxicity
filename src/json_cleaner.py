"""
Module for cleaning Reddit comments, tested on 2005-12 data.

Run this module for a demo.
"""

import json
from pprint import pprint


def clean_json(orig_file, clean_file):
    """
    Cleans the json

    Args:
        orig_file (str) - path file for original file
        clean_file (str) - path file for clean file
    """

    with open(orig_file, 'r') as data, \
            open(clean_file, 'w') as writer:

        for obj in data:
            subreddit = json.loads(obj)['subreddit']
            author = json.loads(obj)['author']
            body = json.loads(obj)['body']
            score = json.loads(obj)['score']
            controversiality = json.loads(obj)['controversiality']
            gilded = json.loads(obj)['gilded']

            reddit_comment = {}
            reddit_comment['subreddit'] = subreddit
            reddit_comment['author'] = author
            reddit_comment['body'] = body
            reddit_comment['score'] = score
            reddit_comment['controversiality'] = controversiality
            reddit_comment['gilded'] = gilded

            # ignore any deleted comments
            if body != '[deleted]':
                try:
                    json.dump(reddit_comment, writer)
                    writer.write('\n')
                # ignore this, results from unicode not normalizing in some comments
                except UnicodeEncodeError:
                    pass


def sample_json(file, sample):
    """
    Returns the first N items in file

    Args:
        file (str) - path for clean file
        sample - number of samples
    """

    with open(file, 'r') as data:
        for index, obj in enumerate(data):
            if index > sample:
                break

            pprint(obj)


if __name__ == '__main__':
    """
    A quick test on RC_2005-12
    """

    ORIG_FILE = '../dump/RC_2005-12'
    CLEAN_FILE = '../dump/RC_2005-12-clean.json'
    SAMPLE = 5

    clean_json(ORIG_FILE, CLEAN_FILE)

    sample_json(CLEAN_FILE, SAMPLE)
