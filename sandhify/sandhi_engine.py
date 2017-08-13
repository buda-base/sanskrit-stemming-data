from sandhifier import *

def find_sandhi(first, second):    
    if len(second) > 0:
        initial = second[0]
    else:
        initial = second
    
    all_sandhis = sandhify(first)
    
    possible = []
    for possible_sandhi in all_sandhis:
        sandhied, rest = possible_sandhi.split(',') 
        homonyms = rest.split('|')
        
        new_homonyms = []
        for homn in homonyms:
            possible_initials = homn.split('~')[0]
            if initial in possible_initials:
                new_homonyms.append(homn)
        
        if new_homonyms:
            possible.append('{},{}'.format(sandhied, '|'.join(new_homonyms)))
    
    if possible:
        return possible
    return None 


def apply_sandhi(current_word, next_word):
    applied = []
    possible_sandhi = find_sandhi(current_word, next_word)
    if possible_sandhi:
        for possible in possible_sandhi:
            sandhied, rest = possible.split(',')
            possible_entries = rest.split('|')
            for pos in possible_entries:
                new_initial = pos.split('/')[1]
                if new_initial == '':
                    applied.append(sandhied+next_word)
                else:
                    sandhied_initial, initial = new_initial.lstrip('-').split('+')
                    sandhied_next_word = sandhied_initial+next_word.lstrip(initial)
                    applied.append(sandhied+sandhied_next_word)
    else:
        applied.append(current_word+' '+next_word)
    return applied

if __name__ == "__main__":
    currents = ['rAma', 'rAmoh', 'rAmoH', 'rAmo', 'rAm']
    initial = 'asti'
    print('Tests:')
    for c in currents:
        print('{} + {} =>'.format(c, initial), apply_sandhi(c, initial))
