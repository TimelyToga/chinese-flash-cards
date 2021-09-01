"""
This is a script for combining all flashcards in `sets/` into a single 
flashcard data file: `all.tsv`
"""

import csv
import os

SETS_DIR = 'sets'
OUTPUT_DIR = 'final'

def get_terms(fn):
    with open(fn) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        return [row for row in rd]

def merge_definitions(def_list):
    """Merge definitions if they are exactly equivalent or contained within each other

    Args:
        def_list (List[str]): potentially distinct definitions for same term

    Returns:
        List[str]: List of unique definitions for term
    """
    for a_idx, a in enumerate(def_list):
        for b_idx, b in enumerate(def_list):
            a_low = a.lower()
            b_low = b.lower()
            if a_idx == b_idx:
                # Don't compare the same index
                continue
            if a_low == b_low: 
                def_list.remove(b)
                continue
            if a_low in b_low:
                def_list.remove(a)
            if b_low in a_low: 
                def_list.remove(b)

    return def_list

def dedup_terms(term_lst):
    term_map = {}
    dupes = 0
    for flashcard in term_lst:
        # print(flashcard)
        # Input validation
        if len(flashcard) != 2:
            raise Exception(f'Terms should only have 2 fields: {term}')

        term = flashcard[0]
        definition = flashcard[1]

        if term in term_map:
            lst = term_map[term]
            lst.append(definition)
            term_map[term] = lst
        else: 
            # print(f'Added new term: {flashcard}')
            term_map[term] = [definition]


    # Merge duped definitions
    for k,v in term_map.items(): 
        if len(v) != 1:
            dupes += len(v)
            term_map[k] = merge_definitions(v)

    # Render definition lists to str
    final_list = []
    for k, def_lst in term_map.items():
        def_lst_str = "; ".join(def_lst)
        final_list.append((k, def_lst_str))

    return term_map, dupes

def combine(sets_dir, output_dir):
    raw_terms = []
    for set in os.listdir(sets_dir):
        rel_set_path = os.path.join(sets_dir, set)
        print(f'Parsing set: {rel_set_path}')

        raw_terms.extend(get_terms(rel_set_path))

    print(f'Master list of {len(raw_terms)} terms')

    term_map, dupe_count = dedup_terms(raw_terms)
    print(f'{len(term_map.keys())} unique terms')
    print(f'{len(term_map.keys()) + dupe_count} total definitions')

    


if __name__ == '__main__': 
    combine(SETS_DIR, OUTPUT_DIR)