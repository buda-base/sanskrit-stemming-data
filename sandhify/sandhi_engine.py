from sandhifier import *

def find_sandhi(first, second):
    all_sandhis = apply_all_sandhis(first)
    possible = []
    if len(second) > 0:
        initial = second[0]
        for possible_sandhi in all_sandhis:
            diffs = possible_sandhi.split(',')[1].split('|')
            possible_initials_list = [a.split('~')[0] for a in diffs]
            possible_initials = ':'.join(possible_initials_list)
            if initial in possible_initials:
                possible.append(possible_sandhi)
    else:
        initial = second
        for possible_sandhi in all_sandhis:
            diffs = possible_sandhi.split(',')[1].split('|')
            possible_initials_list = [a.split('~')[0] for a in diffs]
            possible_initials = ':'.join(possible_initials_list)
            if initial in possible_initials:
                possible.append(possible_sandhi)
    
    if possible:
        return possible
    return None 


def apply_sandhi(current_word, next_word):
    applied = []
    possible_sandhi = find_sandhi(current_word, next_word)
    if possible_sandhi:
        for possible in possible_sandhi:
            sandhied = possible.split(',')[0]
            new_initial = possible.split('/')[1]
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
