# encoding: utf-8
from sandhifier import *


def find_sandhi(first_word, second_word):    
    if len(second_word) > 0:
        initial = second_word[0]
    else:
        initial = second_word
    
    all_potential_sandhis = sandhify(first_word)
    
    formatted_possible_lemmas = []
    for potential_sandhi in all_potential_sandhis:
        sandhied, rest = potential_sandhi.split(',') 
        potential_lemma_diffs = rest.split('|')
        
        possible_lemmas = []
        for potential_diff in potential_lemma_diffs:
            initials_of_potential_lemma = potential_diff.split('~')[0].split(':')
            if initial in initials_of_potential_lemma:
                possible_lemmas.append(potential_diff)
        
        if possible_lemmas:
            formatted_possible_lemmas.append('{},{}'.format(sandhied, '|'.join(possible_lemmas)))
    
    if formatted_possible_lemmas:
        return formatted_possible_lemmas
    return None 


def apply_sandhi(current_word, next_word):
    applied = []
    possible_sandhis = find_sandhi(current_word, next_word)
    if possible_sandhis:
        for sandhi in possible_sandhis:
            sandhied_current_word, rest = sandhi.split(',')
            possible_lemmas = rest.split('|')
            for lemma_diff in possible_lemmas:
                lemma_diff = lemma_diff.split('=')[0] # remove the sandhi type information for the rest of the processing
                new_initial_diff = lemma_diff.split('/')[1]
                if new_initial_diff == '':
                    applied.append(sandhied_current_word+next_word)
                else:
                    sandhied_initial, unsandhied_initials = new_initial_diff.lstrip('-').split('+')
                    sandhied_next_word = sandhied_initial+next_word.lstrip(unsandhied_initials)
                    applied.append(sandhied_current_word+sandhied_next_word)
    else:
        applied.append(current_word+' '+next_word)
    return applied

if __name__ == "__main__":
    currents = [ 'Darma', 'Darman', 'rAma', 'rAmoh', 'rAmoH', 'rAmo', 'rAm']
    initial = 'asti'
    print('Tests:')
    for c in currents:
        print('{} + {} =>'.format(c, initial), apply_sandhi(c, initial))
