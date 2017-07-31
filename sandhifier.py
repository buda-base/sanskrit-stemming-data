from sandhi_rules import *


def apply_vowel_sandhi(stem, final, vowel_sandhi):
    applied = []
    for rule in vowel_sandhi[final]:
        # {final: [(initial, sandhied), ...], ...}
        initial = rule[0]
        sandhi = rule[1]
        
        # calculating the diff for vowel sandhi
        diff = ''
        if final == sandhi:
            diff = '=/='
        else:
            diff = '-{}+{}/='.format(final, sandhi)
            
        # formatting the entry
        form = '{}{},{},{}'.format(stem, sandhi, initial, diff)
        if form not in sandhied: # avoiding duplicates since the tables contain many of them
            applied.append(form)
    return applied


def apply_consonant_sandhi_1(stem, final, consonant_sandhi_1):
    applied = []
    for rule in consonant_sandhi_1[final]:
        # {final: [(initial, (new_final, new_initial)), ...], ...}
        initial = rule[0]
        new_final = rule[1][0]
        new_initial = rule[1][1]
        
        # calculating diff for consonant sandhi
        diff = ''
        if final == new_final and initial == new_initial:
            diff = '=/='
        elif final == new_final and initial != new_initial:
            diff = '=/-{}+{}'.format(initial, new_initial)
        elif final != new_final and initial == new_initial:
            diff = '-{}+{}/='.format(final, new_final)
        else:
            diff = '-{}+{}/-{}+{}'.format(final, new_final, initial, new_initial)
        
        # formatting the entry
        form = '{}{},{},{}'.format(stem, new_final, initial, diff)
        if form not in sandhied: # same as above
            applied.append(form)
    return applied


def apply_consonant_sandhi_2(stem, final, consonant_sandhi_2):
    applied = []
    for rule in consonant_sandhi_2[final]:
        # {final: [(initial, new_second_final+new_final), ...], ...}
        initial = rule[0]
        new_final = rule[1]
        
        # calculating diff for consonant sandhi 2
        diff = ''
        if final == new_final:
            diff = '=/='
        elif final != new_final:
            diff = '-{}+{}/='.format(final, new_final)
        
        # formatting the entry
        form = '{}{},{},{}'.format(stem, new_final, initial, diff)
        if form not in sandhied: # same as above
            applied.append(form)
    return applied


def apply_all_sandhis(infl):    
    # split in stem and ending
    final = infl[-1]
    stem = infl[:-1]

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
    final = infl[-2:]
    stem = infl[:-2]
    
    
    return sandhied
    

# opening the inflected forms
with open('output/heritage_forms_total.txt') as f:
    list = f.readlines()
    inflected = [a.split()[0] for a in list]    

for infl in inflected[:10]:
    sandhied = []
    apply_all_sandhis(infl)
    print('\n'.join(sandhied))