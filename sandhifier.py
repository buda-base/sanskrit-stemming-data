from sandhi_rules import *
from collections import OrderedDict

def apply_vowel_sandhi(stem, final, vowel_sandhi):
    applied = OrderedDict()
    for rule in vowel_sandhi[final]:
        # {final: [(initial, sandhied), ...], ...}
        initial = rule[0]
        new_final = rule[1]
        
        # calculating the diff for vowel sandhi
        diff = ''
        if final == new_final:
            diff = '/'
        else:
            diff = '-{}+{}/'.format(new_final, final)
            
        # adding the entries
        if stem+new_final+'%'+diff not in applied.keys():
            applied[stem+new_final+'%'+diff] = [initial]
        elif initial not in applied[stem+new_final+'%'+diff]: # avoid duplicates as the tables contain many of them
            applied[stem+new_final+'%'+diff].append(initial)
        
    # formatting the entries
    formatted = []
    for k, v in applied.items():
        parts = k.split('%')
        form = parts[0]
        diff = parts[1]
        initials = ':'.join(v)
        formatted.append('{},{},{}'.format(form,initials,diff))
    return formatted


def apply_consonant_sandhi_1(stem, final, consonant_sandhi_1):
    applied = OrderedDict()
    for rule in consonant_sandhi_1[final]:
        # {final: [(initial, (new_final, new_initial)), ...], ...}
        initial = rule[0]
        new_final = rule[1][0]
        new_initial = rule[1][1]
        
        # calculating diff for consonant sandhi
        diff = ''
        if final == new_final and initial == new_initial:
            diff = '/'
        elif final == new_final and initial != new_initial:
            diff = '/-{}+{}'.format(new_initial, initial)
        elif final != new_final and initial == new_initial:
            diff = '-{}+{}/'.format(new_final, final)
        else:
            diff = '-{}+{}/-{}+{}'.format(new_final, final, new_initial, initial)
        
        # adding the entries
        if stem+new_final+'%'+diff not in applied.keys():
            applied[stem+new_final+'%'+diff] = [initial]
        elif initial not in applied[stem+new_final+'%'+diff]: # avoid duplicates as the tables contain many of them
            applied[stem+new_final+'%'+diff].append(initial)
        
    # formatting the entries
    formatted = []
    for k, v in applied.items():
        parts = k.split('%')
        form = parts[0]
        diff = parts[1]
        initials = ':'.join(v)
        formatted.append('{},{},{}'.format(form,initials,diff))
    return formatted


def apply_consonant_sandhi_2(stem, final, consonant_sandhi_2):
    applied = OrderedDict()
    for rule in consonant_sandhi_2[final]:
        # {final: [(initial, new_second_final+new_final), ...], ...}
        initial = rule[0]
        new_final = rule[1]
        
        # calculating diff for consonant sandhi 2
        diff = ''
        if final == new_final:
            diff = '/'
        elif final != new_final:
            diff = '-{}+{}/'.format(new_final, final)

        # adding the entries
        if stem+new_final+'%'+diff not in applied.keys():
            applied[stem+new_final+'%'+diff] = [initial]
        elif initial not in applied[stem+new_final+'%'+diff]: # avoid duplicates as the tables contain many of them
            applied[stem+new_final+'%'+diff].append(initial)
        
    # formatting the entries
    formatted = []
    for k, v in applied.items():
        parts = k.split('%')
        form = parts[0]
        diff = parts[1]
        initials = ':'.join(v)
        formatted.append('{},{},{}'.format(form,initials,diff))        
    return formatted


def apply_visarga_sandhi(stem, final, visarga_sandhi):
    applied = OrderedDict()
    for rule in visarga_sandhi[final]:
        # {final: [(initial, new_second_final+new_final), ...], ...}
        initial = rule[0]
        new_final = rule[1]
        
        # calculating diff for visarga sandhi 1
        if final == new_final:
            diff = '/'
        elif final != new_final:
            diff = '-{}+{}/'.format(new_final, final)
        
        # adding the entries
        if stem+new_final+'%'+diff not in applied.keys():
            applied[stem+new_final+'%'+diff] = [initial]
        elif initial not in applied[stem+new_final+'%'+diff]: # avoid duplicates as the tables contain many of them
            applied[stem+new_final+'%'+diff].append(initial)
        
    # formatting the entries
    formatted = []
    for k, v in applied.items():
        parts = k.split('%')
        form = parts[0]
        diff = parts[1]
        initials = ':'.join(v)
        formatted.append('{},{},{}'.format(form,initials,diff))        
    return formatted


def apply_all_sandhis(inflected_form):    
    sandhied = []
    
    # split in stem and ending
    final = inflected_form[-1]
    stem = inflected_form[:-1]

    if final in vowel_sandhi:
        new_sandhied = apply_vowel_sandhi(stem, final, vowel_sandhi)
        sandhied.extend(new_sandhied)
    
    if final in consonant_sandhi_1:
        new_sandhied = apply_consonant_sandhi_1(stem, final, consonant_sandhi_1)
        sandhied.extend(new_sandhied)
    
    if final in consonant_sandhi_2:
        new_sandhied = apply_consonant_sandhi_2(stem, final, consonant_sandhi_2)
        sandhied.extend(new_sandhied)
        
    # visarga sandhi applies to the last two characters
    final = inflected_form[-2:]
    stem = inflected_form[:-2]
    
    if final in visarga_sandhi_1:
        new_sandhied = apply_visarga_sandhi(stem, final, visarga_sandhi_1)
        sandhied.extend(new_sandhied)
    
    if final in visarga_sandhi_2:
        new_sandhied = apply_visarga_sandhi(stem, final, visarga_sandhi_2)
        sandhied.extend(new_sandhied)
    return sandhied
    

if __name__ == "__main__":    
    # opening the inflected forms
    with open('output/heritage_forms_total.txt') as f:
        list = f.readlines()
        inflected = [a.split()[0] for a in list]    

    total_sandhied = []
    for infl in inflected:
        sandhied = apply_all_sandhis(infl)
        total_sandhied.extend(sandhied)
    
    with open('output/total_output.txt', 'w', -1, 'utf-8-sig') as g:
        output = '\n'.join(total_sandhied)
        g.write(output)
