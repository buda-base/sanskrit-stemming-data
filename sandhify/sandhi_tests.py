from sandhi_engine import *


def formatted_applied_sandhi(to_sandhify):
    if type(to_sandhify) == tuple:
        print('{} + {} => {}'.format(to_sandhify[0], to_sandhify[1], apply_sandhi(to_sandhify[0], to_sandhify[1])))
    elif type(to_sandhify) == list:
        for pair in to_sandhify:
            print('{} + {} => {}'.format(pair[0], pair[1], apply_sandhi(pair[0], pair[1])))
    elif type(to_sandhify) == dict:
        for current, nexts in to_sandhify.items():
            for n in nexts:
                print('{} + {} => {}'.format(current, n, apply_sandhi(current, n)))
    print()

test_set_1 = [('rAmoh', 'asti'), ('rAmoH', 'asti'), ('rAmo', 'asti')]
formatted_applied_sandhi(test_set_1)

test1 = ('tat', 'eva')
formatted_applied_sandhi(test1)

test_set_2 = {'rAmaH': ['asti', 'eva', 'Seva']}
formatted_applied_sandhi(test_set_2)
