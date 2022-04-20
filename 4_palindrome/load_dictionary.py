"""
This script reads the words from a text file and takes they in list
"""

import sys


def load(file):
    """Check file and takes words in lower register"""
    try:
        with open(file) as in_file:
            loader_txt = in_file.read().strip().split('\n')
            loader_txt = [x.lower() for x in loader_txt]
            return loader_txt
    except IOError as e:
        print(f'{e} \nError with open {file}. Close program')
        sys.exit(1)
