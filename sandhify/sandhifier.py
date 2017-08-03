from sandhi_rules import *
from collections import OrderedDict
import re


def add_entries(ordered_dict, form_n_diff, initial):
    """
    Used by all the sandhi functions to bring together all the entries sharing the same inflected form and the same diffs
    format_entries() is then used to reformat the entry in '<form>,<initials>,<diff>'

    an OrderedDict is filled with form+'%'+diff(form_n_diff) as keys and the list of possible initials as value
    ex: {"rAmo'%-o'+aH/": ['a'], 'rAma%-a+aH/': ['A', 'i', 'u', 'U', 'f', 'e', 'E', 'o', 'O'], ...}
    """
    if form_n_diff not in ordered_dict.keys():
        ordered_dict[form_n_diff] = [initial]
    elif initial not in ordered_dict[form_n_diff]:  # avoid duplicates as the tables contain many of them
        ordered_dict[form_n_diff].append(initial)


def format_entries(ordered_dict):
    """
    Restructures the output of add_entries() into normal entries
    :param ordered_dict: the output of add_entries()
    :return: ex: ["rAmo',a,-o'+aH/", 'rAma,A:i:u:U:f:e:E:o:O,-a+aH/', ...]
    """
    formatted = []
    for k, v in ordered_dict.items():
        parts = k.split('%')
        form = parts[0]
        diff = parts[1]
        initials = ':'.join(v)
        formatted.append('{},{},{}'.format(form,initials,diff))
    return formatted


def apply_vowel_sandhi(sandhied, stem, final, vowel_sandhi):
    """
    Generates all vowel sandhis for a given inflected form

    :param sandhied: the OrderedDict receiving the generated forms
    :param stem: the form without the declension
    :param final: the declension (1 char) used to determine which rule to apply
    :param vowel_sandhi: from sandhi_rules.py. {final: [(initial, sandhied), ...], ...}
    """
    for rule in vowel_sandhi[final]:
        initial = rule[0]
        new_final = rule[1]
        
        # calculating the diff for vowel sandhi
        diff = ''
        if ' ' in new_final:
            new_final, new_initial = new_final.split(' ')
            if new_initial == initial:
                diff = '-{}+{}/- +'.format(new_final, final)
            else:
                diff = '-{}+{}/- {}+{}'.format(new_final, final, new_initial, initial)
        elif final == new_final:
            diff = '/-+{}'.format(initial)
        else:
            diff = '-{}+{}/-+{}'.format(new_final, final, initial)
            
        # adding the entries
        add_entries(sandhied, stem+new_final+'%'+diff, initial)        


def apply_consonant_sandhi_1(sandhied, stem, final, consonant_sandhi_1):
    """
    Generates all sandhis from the 1st consonant sandhi table

    :param sandhied: the OrderedDict receiving the generated forms
    :param stem: the form without the declension
    :param final: the declension (1 char) used to determine which rule to apply
    :param consonant_sandhi_1: from sandhi_rules.py {final: [(initial, (new_final, new_initial)), ...], ...}
    """
    for rule in consonant_sandhi_1[final]:
        initial = rule[0]
        new_final = rule[1][0]
        new_initial = rule[1][1]
        
        # calculating diff for consonant sandhi
        diff = ''
        if final == new_final and initial == new_initial:
            diff = '/- +'
        elif final == new_final and initial != new_initial:
            diff = '/- {}+{}'.format(new_initial, initial)
        elif final != new_final and initial == new_initial:
            diff = '-{}+{}/- +'.format(new_final, final)
        else:
            diff = '-{}+{}/- {}+{}'.format(new_final, final, new_initial, initial)
        
        # adding the entries
        add_entries(sandhied, stem+new_final+'%'+diff, initial)


def apply_consonant_sandhi_2(sandhied, stem, final, consonant_sandhi_2):
    """
    Generates all sandhis from the 2nd consonant sandhi table

    :param sandhied: the OrderedDict receiving the generated forms
    :param stem: the form without the declension
    :param final: the declension (1 char) used to determine which rule to apply
    :param consonant_sandhi_2: from sandhi_rules.py {final: [(initial, new_second_final+new_final), ...], ...}
    """
    for rule in consonant_sandhi_2[final]:
        initial = rule[0]
        new_final = rule[1]
        
        # calculating diff for consonant sandhi 2
        diff = ''
        if final == new_final:
            diff = '/- +'
        elif final != new_final:
            diff = '-{}+{}/- +'.format(new_final, final)

        # adding the entries
        add_entries(sandhied, stem+new_final+'%'+diff, initial)


def apply_visarga_sandhi(sandhied, stem, final, visarga_sandhi):
    """
    Generates all the sandhis from the 1st visarga table

    :param sandhied: the OrderedDict receiving the generated forms
    :param stem: the form without the declension
    :param final: the declension (2 chars) used to determine which rule to apply
    :param visarga_sandhi: from sandhi_rules.py {final: [(initial, new_second_final+new_final), ...], ...}
    """
    for rule in visarga_sandhi[final]:
        initial = rule[0]
        new_final = rule[1]
        
        # calculating diff for visarga sandhi 1
        if final == new_final:
            diff = '/- +'
        elif ' ' in new_final:
            new_final, new_initial = new_final.split(' ')
            if new_initial == initial:
                diff = '-{}+{}/- +'.format(new_final, final)
            else:
                diff = '-{}+{}/- {}+{}'.format(new_final, final, new_initial, initial)
        elif final != new_final:
            diff = '-{}+{}/- +'.format(new_final, final)
        
        # adding the entries
        add_entries(sandhied, stem+new_final+'%'+diff, initial)


def apply_absolute_finals_sandhi(sandhied, inflected_form, absolute_finals_sandhi):
    """
    Generates all the sandhis from the 1st visarga table

    :param sandhied: the OrderedDict receiving the generated forms
    :param inflected_form: unlike other rules. clusters of consonants have to be detected, so the whole inflected form is taken
    :param absolute_finals_sandhi: from sandhi_rules.py {final: [(initial, new_second_final+new_final), ...], ...}
    """
    # find ending (can be a cluster of consonants or a single one)
    consonants = ["k", "K", "g", "G", "N", "c", "C", "j", "J", "Y", "w", "W", "q", "Q", "R", "t", "T", "d", "D", "n", "p", "P", "b", "B", "m", "y", "r", "l", "v", "S", "z", "s", "h"]
    if inflected_form[-1] in consonants:
        stem, final = re.split('(['+''.join(consonants)+']+)$', inflected_form)[:2]
        
        # clusters of consonants are reduced to the first consonant
        if len(final) > 1:
            stem = stem + final[0]
            final = final[1:]
            diff = '-+{}/'.format(final)
            add_entries(sandhied, stem+'%'+diff, '')
        else:        
            for rule in absolute_finals_sandhi[final]:
                initial = rule[0] # empty string
                new_final = rule[1]
                
                # calculating diff for absolute finals sandhi
                if final == new_final:
                    diff = '/'
                elif final != new_final:
                    diff = '-{}+{}/'.format(new_final, final)
                
                # adding the entries
                add_entries(sandhied, stem+new_final+'%'+diff, '')


def apply_cC_words_sandhi(sandhied, stem, final, cC_words_sandhi):
    """
    Generates all the sandhis from the cC words table

    :param sandhied: the OrderedDict receiving the generated forms
    :param stem: the form without the declension
    :param final: the declension (1 char) used to determine which rule to apply
    :param cC_words_sandhi: from sandhi_rules.py {final: [(initial, new_initial), ...], ...}
    """
    for rule in cC_words_sandhi[final]:
        initial = rule[0]
        new_initial = rule[1]
        
        diff = '/- {}+{}'.format(new_initial, initial)
        
        # adding the entries
        add_entries(sandhied, stem+final+'%'+diff, initial)


def apply_punar_sandhi(sandhied, punar_sandhi):
    """
    Generates all sandhis for punar
    
    :param cC_words_sandhi: from sandhi_rules.py
    """
    stem = 'puna'
    final = 'r'
    for rule in punar_sandhi[final]:
        initial = rule[0]
        new_final = rule[1]
        
        # calculating diff for visarga sandhi 1
        if final == new_final:
            diff = '/- +'
        elif final != new_final:
            diff = '-{}+{}/- +'.format(new_final, final)
        
        # adding the entries
        add_entries(sandhied, stem+new_final+'%'+diff, initial)

def apply_all_sandhis(inflected_form):
    """
    Generates all the sandhis for an inflected form.
        - 'sandhied' receives the sandhied forms from the sandhi functions
        - the entries are formatted by format_entries()
    :param inflected_form: the form to sandhify
    :return: ex. rAmA['rAmA,a:A,/', 'rAme,i,-e+A/', ...]
    """
    sandhied = OrderedDict()
    
    # split in stem and ending
    final = inflected_form[-1]
    stem = inflected_form[:-1]

    if final in vowel_sandhi:
        apply_vowel_sandhi(sandhied, stem, final, vowel_sandhi)
    
    if final in consonant_sandhi_1:
        apply_consonant_sandhi_1(sandhied, stem, final, consonant_sandhi_1)
    
    if final in consonant_sandhi_2:
        apply_consonant_sandhi_2(sandhied, stem, final, consonant_sandhi_2)
    
    if final in cC_words_sandhi:
        apply_cC_words_sandhi(sandhied, stem, final, cC_words_sandhi)
        
    # visarga sandhi applies to the last two characters
    final = inflected_form[-2:]
    stem = inflected_form[:-2]
    
    if final in visarga_sandhi_1:
        apply_visarga_sandhi(sandhied, stem, final, visarga_sandhi_1)
    
    if final in visarga_sandhi_2:
        apply_visarga_sandhi(sandhied, stem, final, visarga_sandhi_2)
    
    apply_absolute_finals_sandhi(sandhied, inflected_form, absolute_finals_sandhi)
    
    # Exceptions
    if inflected_form == 'punar':
        apply_punar_sandhi(sandhied, punar_sandhi)
    
    formatted = format_entries(sandhied)
    return formatted


def find_uninflected_stem(stem, form):
    """
    Finds all the shared caracters from left to right.
    find_uninflected_stem('rAmaH', 'rAmo') => -1+aH

    :param stem: form to reach by applying the diff
    :param form: given form
    :return: a diff: '-<number of chars to delete>+<characters to add>'
    """
    if len(stem) <= len(form):
        max = len(stem)
    else:
        max = len(form)
    i = 0
    while i <= len(stem)-1 and i <= len(form)-1 and stem[i] == form[i]:
        i += 1
    stem_ending = stem[i:]
    form_ending = form[i:]
    if stem_ending == '' and form_ending == '':
        operation = ''
    else:
        form_ending_len = len(form_ending)
        operation = '-{}+{}'.format(form_ending_len, stem_ending)
    return operation


def sandhied_with_lemmas(raw_pairs):
    """
    applies apply_all_sandhis() on every entry in raw_pairs
    creates a new diff with the lemma from which the inflected form was derived
    discarding the diff produced to find the unsandhied inflected form.

    outputformat: '<sandhied_inflected_form>,<initial>,<diffs>/<initial_diff>'
    <diffs>: '<diff_to_1st_lemma>;<diff_to_2nd_lemma>;…'
    <diff_to_nth_lemma>: '-<number_of_chars_to_delete>+<chars_to_add>'
    <initial_diff>: '-<sandhied_initial>+<initial>'

    :param raw_pairs: [(inflected_form, lemma), …] generated by raw_parse_Heritage_XML.py
    :return: ex. ['prezyate,a,-1+;-6+I/-'+', 'aprezyata,A:i:u:U:f:e:E:o:O,-1+;-6+I/', …]
    """
    total_sandhied = []
    for infl, non_infl in raw_pairs:
        sandhied = apply_all_sandhis(infl)
        stems = non_infl.split('/')
        for entry in sandhied:
            parts = entry.split(',')
            sandhied_form = parts[0]
            initial = parts[1]
            new_initials = parts[2].split('/')[1]
            operations = []
            for stem in stems:
                operations.append(find_uninflected_stem(stem, sandhied_form))
            total_sandhied.append(','.join([sandhied_form, initial, ';'.join(operations)+'/'+new_initials]))
    return total_sandhied


if __name__ == "__main__":    
    # opening the inflected forms
    with open('../output/heritage_raw_pairs.txt') as f:
        list = f.readlines()
        inflected = [a.strip().split(',') for a in list]

    total_sandhied = sandhied_with_lemmas(inflected)

    with open('../output/total_output.txt', 'w', -1, 'utf-8-sig') as g:
        output = '\n'.join(total_sandhied)
        g.write(output)
