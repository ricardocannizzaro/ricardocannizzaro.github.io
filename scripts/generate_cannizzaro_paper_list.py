#!/usr/bin/env python3

""" A script to generate a sorted list of papers from a .bib BibTeX file

    Author: Ricardo Cannizzaro

"""

from generate_paper_list import parse_from_args

def main():
    args = {'bib_file_path': '../files/cannizzaro_citations.bib'}
    parse_from_args(args)