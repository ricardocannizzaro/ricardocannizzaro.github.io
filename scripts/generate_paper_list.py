#!/usr/bin/env python3

""" A script to generate a sorted list of papers from a .bib BibTeX file

    Author: Ricardo Cannizzaro

"""

import argparse
import bibtexparser
from operator import itemgetter

def load_bib_file(bib_file_path):
    with open(bib_file_path, 'r', encoding='utf-8') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    return bib_database.entries

def sort_by_year(bib_entries):
    return sorted(bib_entries, key=lambda x: int(x.get('year', 0)), reverse=True)

def print_paper_list(sorted_papers):
    for idx, paper in enumerate(sorted_papers, start=1):
        title = paper.get('title', 'No Title')
        year = paper.get('year', 'No Year')
        authors = paper.get('author', 'No Authors')
        conference = paper.get('booktitle', '')
        journal = paper.get('journal', '')
        url = paper.get('url', '')

        print(f"{idx}. **{title}** ({year})")
        print(f"   {authors}. {conference}|{journal}")
        if url:
            print(f"   [[Paper]({url})]")
        print()

def print_paper_list_markdown(sorted_papers):
    for idx, paper in enumerate(sorted_papers, start=1):
        title = paper.get('title', 'No Title')
        year = paper.get('year', 'No Year')
        authors = paper.get('author', 'No Authors')
        conference = paper.get('booktitle', '')
        journal = paper.get('journal', '')
        url = paper.get('url', '')

        mark_down_str: str = f"* **{title}**<br>{authors}. {conference}{journal} {year}.<br>"
        if url:
            mark_down_str = mark_down_str + f"[[Paper]({url})]"
        print(mark_down_str)
        
def print_paper_list_latex_list(sorted_papers):
    print("\\begin{itemize}")
    for idx, paper in enumerate(sorted_papers, start=1):
        title = paper.get('title', 'No Title')
        year = paper.get('year', 'No Year')
        authors = paper.get('author', 'No Authors')
        conference = paper.get('booktitle', '')
        journal = paper.get('journal', '')
        url = paper.get('url', '')

        latex_str = f"  \\item {title}\\\\{authors}. {conference}{journal} {year}."
        if url:
            latex_str += f" \\href{{{url}}}{{[Paper]}}"
        print(latex_str)
    print("\\end{itemize}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a sorted list of papers from a BibTeX file.')
    parser.add_argument('bib_file_path', type=str, help='Path to the BibTeX file')

    args = parser.parse_args()

    bib_entries = load_bib_file(args.bib_file_path)
    sorted_papers = sort_by_year(bib_entries)

    print("Sorted list of papers:\n")
    print_paper_list(sorted_papers)
    print("===============================\n")

    print("\nMarkdown formatted list of papers:\n")
    print_paper_list_markdown(sorted_papers)
    print("===============================\n")

    print("\nLaTeX formatted list of papers (itemize environment):\n")
    print_paper_list_latex_list(sorted_papers)
    print("===============================\n")

