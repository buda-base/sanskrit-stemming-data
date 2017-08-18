# encoding: utf-8
from _collections import OrderedDict
def generate_sandhi_rules(initials, sandhi):
    """
    Unpacks the sandhi table into individual rules

    :param initials: The first row containing the initial char of the next word
    :param sandhi: The remaining rows, the first column contains the ending char of the current word
    :return: [('a', [('a', 'A'), ('A', 'A'), ...]), ('A', [('a', 'A'), ('A', 'A'), ...]), ...]
    """
    rules = []
    for final, sandhied_forms in sandhi:
        rule = (final, [])
        for num, form in enumerate(sandhied_forms):
            rule[1].append((initials[num], form))
        rules.append(rule)
    return rules


def generate_sandhis(initials, sandhi_rules, name, comment):
    """
    Formats the output of generate_sandhi_rules() so it can simply be pasted in sandhi_rules.py,
    which is then used by sandhifier.py

    :param initials: for generate_sandhi_rules()
    :param sandhi_rules:  for generate_sandhi_rules()
    :param name: name of the variable (in sandhi_rules.py) for a given sandhi table
    :param comment: put before the variable
    """
    output = []
    all_rules = generate_sandhi_rules(initials, sandhi_rules)
    
    # transfer to an OrderdDict to have in the same line all the sandhis with the same final (ex: table has two lines for final i)
    rules_flattened = OrderedDict()
    for final, rules in all_rules:
        if final not in rules_flattened.keys():
            rules_flattened[final] = []
        rules_flattened[final].extend(rules)
        
    output.append(comment)
    output.append(name)
    for final, rules in rules_flattened.items():
        output.append('\t\t"{}": ['.format(final))
        formatted_rules = []
        for rule in rules:        
            formatted_rules.append('\t\t\t\t("{}", "{}")'.format(rule[0], rule[1]))
        output.append(',\n'.join(formatted_rules)+'],')
    output.append('\t\t\t}')
    return '\n'.join(output)


def generate_consonant_sandhi_1(initials, sandhi_rules, name, comment):
    """
    Does the same thing as generate_sandhis(), further unpacking sandhis like "c(C)"
    """
    output = []
    cons_sandhi1 = generate_sandhi_rules(initials, sandhi_rules)
    output.append(comment)
    output.append(name)
    groups = []
    for final, rules in cons_sandhi1:
        formatted_rules = []
        for rule in rules:
            sandhi = rule[1]
            if '(' in sandhi:
                parts = rule[1].split('(')
                new_final = parts[0] 
                new_initial = parts[1][:-1]
                formatted_rules.append('\t\t\t("{}", ("{}", "{}"))'.format(rule[0], new_final, new_initial)) # the space in the diff is preserved
            else:
                new_final = sandhi
                new_initial = rule[0]
                formatted_rules.append('\t\t\t("{}", ("{}", "{}"))'.format(rule[0], new_final, new_initial))
        groups.append('\t\t"{}": [\n'.format(final)+',\n'.join(formatted_rules)+'\n\t\t]')
    output.append(',\n'.join(groups))
    output.append('}')
    return '\n'.join(output)

# These tables have been manually formatted from the .csv files of the same content.

vowel_sandhi_initials = ["a", "A", "A", "i", "i", "u", "U", "f", "e", "E", "o", "O"]
vowel_sandhi = [("a", ["A", "A", "A", "e", "e", "o", "o", "ar", "E", "E", "O", "O"]),
                ("A", ["A", "A", "A", "e", "e", "o", "o", "ar", "E", "E", "O", "O"]),
                ("i", ["ya", "yA", "yA", "I", "I", "yu", "yU", "yf", "ye", "yE", "yo", "yO"]),
                ("i", ["i a", "i A", "i A", "i i", "i i", "i u", "i U", "i f", "i e", "i E", "i o", "i O"]),
                ("I", ["ya", "yA", "yA", "I", "I", "yu", "yU", "yf", "ye", "yE", "yo", "yO"]),
                ("I", ["I a", "I A", "I A", "I i", "I i", "I u", "I U", "I f", "I e", "I E", "I o", "I O"]),
                ("u", ["va", "vA", "vA", "vi", "vi", "U", "U", "vf", "ve", "vE", "vo", "vO"]),
                ("u", ["u a", "u A", "u A", "u i", "u i", "u u", "u U", "u f", "u e", "u E", "u o", "u O"]),
                ("U", ["va", "vA", "vA", "vi", "vi", "U", "U", "vf", "ve", "vE", "vo", "vO"]),
                ("U", ["U a", "U A", "U A", "U i", "U i", "U u", "U U", "U f", "U e", "U E", "U o", "U O"]),
                ("f", ["ra", "rA", "rA", "ri", "ri", "ru", "rU", "F", "re", "rE", "ro", "rO"]),
                ("e", ["e '", "a A", "a A", "a i", "a i", "a u", "a U", "a f", "a e", "a E", "a o", "a O"]),
                ("e", ["e a", "e A", "e A", "e i", "e i", "e u", "e U", "e f", "e e", "e E", "e o", "e O"]),
                ("E", ["A a", "A A", "A A", "A i", "A i", "A u", "A U", "A f", "A e", "A E", "A o", "A O"]),
                ("o", ["o '", "avA", "a A", "avi", "avi", "avu", "avU", "avf", "ave", "avE", "avo", "avO"]),
                ("O", ["Ava", "AvA", "AvA", "Avi", "Avi", "Avu", "AvU", "Avf", "Ave", "AvE", "Avo", "AvO"])
                ]

consonant_sandhi_1_initials = ['y', 'r', 'l', 'v', 'S', 'S', 'z', 's', 'h']
consonant_sandhi_1 = [('k', ['g', 'g', 'g', 'g', 'g', 'g', 'k', 'k', 'g(G)']),
                      ('w', ['q', 'q', 'q', 'q', 'w', 'w', 'w', 'w', 'q(Q)']),
                      ('t', ['d', 'd', 'l', 'd', 'c(C)', 'c(C)', 't', 't', 'd(D)']),
                      ('p', ['b', 'b', 'b', 'b', 'p', 'p', 'p', 'p', 'b(B)']),
                      ('N', ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']),
                      ('n', ['n', 'n', 'M', 'n', 'Y(S)', 'Y(C)', 'n', 'n', 'n']),
                      ('m', ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'])
                      ]

consonant_sandhi_2_initials = ["k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "t", "T", "d", "D", "p", "P", "b", "B", "n", "m"]
consonant_sandhi_2 = [("k", ["k", "k", "g", "g", "k", "k", "g", "g", "k", "k", "g", "g", "k", "k", "g", "g", "k", "k", "g", "g", "N", "N"]),
                      ("w", ["w", "w", "q", "q", "w", "w", "q", "q", "w", "w", "q", "q", "w", "w", "q", "q", "w", "w", "q", "q", "R", "R"]),
                      ("t", ["t", "t", "d", "d", "c", "c", "j", "j", "w", "w", "q", "q", "t", "t", "d", "d", "t", "t", "d", "d", "n", "n"]),
                      ("p", ["p", "p", "b", "b", "p", "p", "b", "b", "p", "p", "b", "b", "p", "p", "b", "b", "p", "p", "b", "b", "m", "m"]),
                      ("R", ["R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R", "R"]),
                      ("n", ["n", "n", "n", "n", "MS", "MS", "Y", "Y", "Mz", "Mz", "R", "R", "Ms", "Ms", "n", "n", "n", "n", "n", "n", "n", "n"]),
                      ("m", ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"])
                      ]

consonant_sandhi_1_vowels_initials = ['a', 'A', 'i', 'I', 'u', 'U', 'f', 'e', 'E', 'o', 'O']
consonant_sandhi_1_vowels = [('ak', ['ag', 'ag', 'ag', 'ag', 'ag', 'ag', 'ag', 'ag', 'ag', 'ag', 'ag']),
                             ('Ak', ['Ag', 'Ag', 'Ag', 'Ag', 'Ag', 'Ag', 'Ag', 'Ag', 'Ag', 'Ag', 'Ag']),
                             ('ik', ['ig', 'ig', 'ig', 'ig', 'ig', 'ig', 'ig', 'ig', 'ig', 'ig', 'ig']),
                             ('Ik', ['Ig', 'Ig', 'Ig', 'Ig', 'Ig', 'Ig', 'Ig', 'Ig', 'Ig', 'Ig', 'Ig']),
                             ('uk', ['ug', 'ug', 'ug', 'ug', 'ug', 'ug', 'ug', 'ug', 'ug', 'ug', 'ug']),
                             ('Uk', ['Ug', 'Ug', 'Ug', 'Ug', 'Ug', 'Ug', 'Ug', 'Ug', 'Ug', 'Ug', 'Ug']),
                             ('ek', ['eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg', 'eg']),
                             ('ok', ['og', 'og', 'og', 'og', 'og', 'og', 'og', 'og', 'og', 'og', 'og']),
                             ('Ek', ['Eg', 'Eg', 'Eg', 'Eg', 'Eg', 'Eg', 'Eg', 'Eg', 'Eg', 'Eg', 'Eg']),
                             ('Ok', ['Og', 'Og', 'Og', 'Og', 'Og', 'Og', 'Og', 'Og', 'Og', 'Og', 'Og']),
                             ('aw', ['aq', 'aq', 'aq', 'aq', 'aq', 'aq', 'aq', 'aq', 'aq', 'aq', 'aq']),
                             ('Aw', ['Aq', 'Aq', 'Aq', 'Aq', 'Aq', 'Aq', 'Aq', 'Aq', 'Aq', 'Aq', 'Aq']),
                             ('iw', ['iq', 'iq', 'iq', 'iq', 'iq', 'iq', 'iq', 'iq', 'iq', 'iq', 'iq']),
                             ('Iw', ['Iq', 'Iq', 'Iq', 'Iq', 'Iq', 'Iq', 'Iq', 'Iq', 'Iq', 'Iq', 'Iq']),
                             ('uw', ['uq', 'uq', 'uq', 'uq', 'uq', 'uq', 'uq', 'uq', 'uq', 'uq', 'uq']),
                             ('Uw', ['Uq', 'Uq', 'Uq', 'Uq', 'Uq', 'Uq', 'Uq', 'Uq', 'Uq', 'Uq', 'Uq']),
                             ('ew', ['eq', 'eq', 'eq', 'eq', 'eq', 'eq', 'eq', 'eq', 'eq', 'eq', 'eq']),
                             ('ow', ['oq', 'oq', 'oq', 'oq', 'oq', 'oq', 'oq', 'oq', 'oq', 'oq', 'oq']),
                             ('Ew', ['Eq', 'Eq', 'Eq', 'Eq', 'Eq', 'Eq', 'Eq', 'Eq', 'Eq', 'Eq', 'Eq']),
                             ('Ow', ['Oq', 'Oq', 'Oq', 'Oq', 'Oq', 'Oq', 'Oq', 'Oq', 'Oq', 'Oq', 'Oq']),
                             ('at', ['ad', 'ad', 'ad', 'ad', 'ad', 'ad', 'ad', 'ad', 'ad', 'ad', 'ad']),
                             ('At', ['Ad', 'Ad', 'Ad', 'Ad', 'Ad', 'Ad', 'Ad', 'Ad', 'Ad', 'Ad', 'Ad']),
                             ('it', ['id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id', 'id']),
                             ('It', ['Id', 'Id', 'Id', 'Id', 'Id', 'Id', 'Id', 'Id', 'Id', 'Id', 'Id']),
                             ('ut', ['ud', 'ud', 'ud', 'ud', 'ud', 'ud', 'ud', 'ud', 'ud', 'ud', 'ud']),
                             ('Ut', ['Ud', 'Ud', 'Ud', 'Ud', 'Ud', 'Ud', 'Ud', 'Ud', 'Ud', 'Ud', 'Ud']),
                             ('et', ['ed', 'ed', 'ed', 'ed', 'ed', 'ed', 'ed', 'ed', 'ed', 'ed', 'ed']),
                             ('ot', ['od', 'od', 'od', 'od', 'od', 'od', 'od', 'od', 'od', 'od', 'od']),
                             ('Et', ['Ed', 'Ed', 'Ed', 'Ed', 'Ed', 'Ed', 'Ed', 'Ed', 'Ed', 'Ed', 'Ed']),
                             ('Ot', ['Od', 'Od', 'Od', 'Od', 'Od', 'Od', 'Od', 'Od', 'Od', 'Od', 'Od']),
                             ('ap', ['ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']),
                             ('Ap', ['Ab', 'Ab', 'Ab', 'Ab', 'Ab', 'Ab', 'Ab', 'Ab', 'Ab', 'Ab', 'Ab']),
                             ('ip', ['ib', 'ib', 'ib', 'ib', 'ib', 'ib', 'ib', 'ib', 'ib', 'ib', 'ib']),
                             ('Ip', ['Ib', 'Ib', 'Ib', 'Ib', 'Ib', 'Ib', 'Ib', 'Ib', 'Ib', 'Ib', 'Ib']),
                             ('up', ['ub', 'ub', 'ub', 'ub', 'ub', 'ub', 'ub', 'ub', 'ub', 'ub', 'ub']),
                             ('Up', ['Ub', 'Ub', 'Ub', 'Ub', 'Ub', 'Ub', 'Ub', 'Ub', 'Ub', 'Ub', 'Ub']),
                             ('ep', ['eb', 'eb', 'eb', 'eb', 'eb', 'eb', 'eb', 'eb', 'eb', 'eb', 'eb']),
                             ('op', ['ob', 'ob', 'ob', 'ob', 'ob', 'ob', 'ob', 'ob', 'ob', 'ob', 'ob']),
                             ('Ep', ['Eb', 'Eb', 'Eb', 'Eb', 'Eb', 'Eb', 'Eb', 'Eb', 'Eb', 'Eb', 'Eb']),
                             ('Op', ['Ob', 'Ob', 'Ob', 'Ob', 'Ob', 'Ob', 'Ob', 'Ob', 'Ob', 'Ob', 'Ob']),
                             ('aN', ['aNN', 'aNN', 'aNN', 'aNN', 'aNN', 'aNN', 'aNN', 'aNN', 'aNN', 'aNN', 'aNN']),
                             ('AN', ['AN', 'AN', 'AN', 'AN', 'AN', 'AN', 'AN', 'AN', 'AN', 'AN', 'AN']),
                             ('iN', ['iNN', 'iNN', 'iNN', 'iNN', 'iNN', 'iNN', 'iNN', 'iNN', 'iNN', 'iNN', 'iNN']),
                             ('IN', ['IN', 'IN', 'IN', 'IN', 'IN', 'IN', 'IN', 'IN', 'IN', 'IN', 'IN']),
                             ('uN', ['uNN', 'uNN', 'uNN', 'uNN', 'uNN', 'uNN', 'uNN', 'uNN', 'uNN', 'uNN', 'uNN']),
                             ('UN', ['UN', 'UN', 'UN', 'UN', 'UN', 'UN', 'UN', 'UN', 'UN', 'UN', 'UN']),
                             ('eN', ['eNN', 'eNN', 'eNN', 'eNN', 'eNN', 'eNN', 'eNN', 'eNN', 'eNN', 'eNN', 'eNN']),
                             ('oN', ['oNN', 'oNN', 'oNN', 'oNN', 'oNN', 'oNN', 'oNN', 'oNN', 'oNN', 'oNN', 'oNN']),
                             ('EN', ['EN', 'EN', 'EN', 'EN', 'EN', 'EN', 'EN', 'EN', 'EN', 'EN', 'EN']),
                             ('ON', ['ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON', 'ON']),
                             ('an', ['ann', 'ann', 'ann', 'ann', 'ann', 'ann', 'ann', 'ann', 'ann', 'ann', 'ann']),
                             ('An', ['An', 'An', 'An', 'An', 'An', 'An', 'An', 'An', 'An', 'An', 'An']),
                             ('in', ['inn', 'inn', 'inn', 'inn', 'inn', 'inn', 'inn', 'inn', 'inn', 'inn', 'inn']),
                             ('In', ['In', 'In', 'In', 'In', 'In', 'In', 'In', 'In', 'In', 'In', 'In']),
                             ('un', ['unn', 'unn', 'unn', 'unn', 'unn', 'unn', 'unn', 'unn', 'unn', 'unn', 'unn']),
                             ('Un', ['Un', 'Un', 'Un', 'Un', 'Un', 'Un', 'Un', 'Un', 'Un', 'Un', 'Un']),
                             ('en', ['enn', 'enn', 'enn', 'enn', 'enn', 'enn', 'enn', 'enn', 'enn', 'enn', 'enn']),
                             ('on', ['onn', 'onn', 'onn', 'onn', 'onn', 'onn', 'onn', 'onn', 'onn', 'onn', 'onn']),
                             ('En', ['En', 'En', 'En', 'En', 'En', 'En', 'En', 'En', 'En', 'En', 'En']),
                             ('On', ['On', 'On', 'On', 'On', 'On', 'On', 'On', 'On', 'On', 'On', 'On']),
                             ('am', ['am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'am']),
                             ('Am', ['Am', 'Am', 'Am', 'Am', 'Am', 'Am', 'Am', 'Am', 'Am', 'Am', 'Am']),
                             ('im', ['im', 'im', 'im', 'im', 'im', 'im', 'im', 'im', 'im', 'im', 'im']),
                             ('Im', ['Im', 'Im', 'Im', 'Im', 'Im', 'Im', 'Im', 'Im', 'Im', 'Im', 'Im']),
                             ('um', ['um', 'um', 'um', 'um', 'um', 'um', 'um', 'um', 'um', 'um', 'um']),
                             ('Um', ['Um', 'Um', 'Um', 'Um', 'Um', 'Um', 'Um', 'Um', 'Um', 'Um', 'Um']),
                             ('em', ['em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em', 'em']),
                             ('om', ['om', 'om', 'om', 'om', 'om', 'om', 'om', 'om', 'om', 'om', 'om']),
                             ('Em', ['Em', 'Em', 'Em', 'Em', 'Em', 'Em', 'Em', 'Em', 'Em', 'Em', 'Em']),
                             ('Om', ['Om', 'Om', 'Om', 'Om', 'Om', 'Om', 'Om', 'Om', 'Om', 'Om', 'Om'])
                             ]

visarga_sandhi_1_initials = ["a", "A", "i", "i", "u", "U", "f", "e", "E", "o", "O", "y", "r", "l", "v", "S", "z", "s", "h"]
visarga_sandhi_1 = [("aH", ["o '", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "o", "o", "o", "o", "aH", "aH", "aH", "o"]),
                    ("AH", ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "AH", "AH", "AH", "A"]),
                    ("iH", ["ir", "ir", "ir", "ir", "ir", "ir", "ir", "ir", "ir", "ir", "ir", "ir", "I", "ir", "ir", "H", "iH", "iH", "ir"]),
                    ("IH", ["Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "I", "Ir", "Ir", "H", "IH", "IH", "Ir"]),
                    ("uH", ["ur", "ur", "ur", "ur", "ur", "ur", "ur", "ur", "ur", "ur", "ur", "ur", "U", "ur", "ur", "H", "uH", "uH", "ur"]),
                    ("UH", ["Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "U", "Ur", "Ur", "H", "UH", "UH", "Ur"]),
                    ("eH", ["er", "er", "er", "er", "er", "er", "er", "er", "er", "er", "er", "er", "e", "er", "er", "H", "eH", "eH", "er"]),
                    ("oH", ["or", "or", "or", "or", "or", "or", "or", "or", "or", "or", "or", "or", "o", "or", "or", "H", "oH", "oH", "or"]),
                    ("EH", ["Er", "Er", "Er", "Er", "Er", "Er", "Er", "Er", "Er", "Er", "Er", "Er", "E", "Er", "Er", "H", "EH", "EH", "Er"]),
                    ("OH", ["Or", "Or", "Or", "Or", "Or", "Or", "Or", "Or", "Or", "Or", "Or", "Or", "O", "Or", "Or", "H", "OH", "OH", "Or"])
                    ]

visarga_sandhi_2_initials = ["k", "K", "g", "g", "G", "G", "c", "C", "j", "j", "J", "J", "w", "W", "q", "q", "Q", "Q", "t", "T", "d", "d", "D", "D", "p", "P", "b", "b", "B", "B", "n", "n", "m", "m"]
visarga_sandhi_2 = [("aH", ["aH", "aH", "o", "ar", "o", "ar", "aS", "aS", "o", "ar", "o", "ar", "az", "az", "o", "ar", "o", "ar", "as", "as", "o", "ar", "o", "ar", "aH", "aH", "o", "ar", "o", "ar", "o", "ar", "o", "ar"]),
                    ("AH", ["AH", "AH", "A", "Ar", "A", "Ar", "AS", "AS", "A", "Ar", "A", "Ar", "Az", "Az", "A", "Ar", "A", "Ar", "As", "As", "A", "Ar", "A", "Ar", "AH", "AH", "A", "Ar", "A", "Ar", "A", "Ar", "A", "Ar"]),
                    ("iH", ["iH", "iH", "ir", "ir", "ir", "ir", "iS", "iS", "ir", "ir", "ir", "ir", "iz", "iz", "ir", "ir", "ir", "ir", "is", "is", "ir", "ir", "ir", "ir", "iH", "iH", "ir", "ir", "ir", "ir", "ir", "ir", "ir", "ir"]),
                    ("IH", ["IH", "IH", "Ir", "Ir", "Ir", "Ir", "IS", "IS", "Ir", "Ir", "Ir", "Ir", "Iz", "Iz", "Ir", "Ir", "Ir", "Ir", "Is", "Is", "Ir", "Ir", "Ir", "Ir", "IH", "IH", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir"]),
                    ("uH", ["uH", "uH", "ur", "ur", "ur", "ur", "uS", "uS", "ur", "ur", "ur", "ur", "uz", "uz", "ur", "ur", "ur", "ur", "us", "us", "ur", "ur", "ur", "ur", "uH", "uH", "ur", "ur", "ur", "ur", "ur", "ur", "ur", "ur"]),
                    ("UH", ["UH", "UH", "Ur", "Ur", "Ur", "Ur", "US", "US", "Ur", "Ur", "Ur", "Ur", "Uz", "Uz", "Ur", "Ur", "Ur", "Ur", "Us", "Us", "Ur", "Ur", "Ur", "Ur", "UH", "UH", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur"]),
                    ("eH", ["eH", "eH", "er", "er", "er", "er", "eS", "eS", "er", "er", "er", "er", "ez", "ez", "er", "er", "er", "er", "es", "es", "er", "er", "er", "er", "eH", "eH", "er", "er", "er", "er", "er", "er", "er", "er"]),
                    ("oH", ["oH", "oH", "or", "or", "or", "or", "oS", "oS", "or", "or", "or", "or", "oz", "oz", "or", "or", "or", "or", "os", "os", "or", "or", "or", "or", "oH", "oH", "or", "or", "or", "or", "or", "or", "or", "or"]),
                    ("EH", ["EH", "EH", "Er", "Er", "Er", "Er", "ES", "ES", "Er", "Er", "Er", "Er", "Ez", "Ez", "Er", "Er", "Er", "Er", "Es", "Es", "Er", "Er", "Er", "Er", "EH", "EH", "Er", "Er", "Er", "Er", "Er", "Er", "Er", "Er"]),
                    ("OH", ["OH", "OH", "Or", "Or", "Or", "Or", "OS", "OS", "Or", "Or", "Or", "Or", "Oz", "Oz", "Or", "Or", "Or", "Or", "Os", "Os", "Or", "Or", "Or", "Or", "OH", "OH", "Or", "Or", "Or", "Or", "Or", "Or", "Or", "Or"])
                    ]

absolute_finals_sandhi_initials = ['']
absolute_finals_sandhi = [("k", ["k"]),
                          ("K", ["k"]),
                          ("g", ["k"]),
                          ("G", ["k"]),
                          ("w", ["w"]),
                          ("W", ["w"]),
                          ("q", ["w"]),
                          ("Q", ["w"]),
                          ("t", ["t"]),
                          ("T", ["t"]),
                          ("d", ["t"]),
                          ("D", ["t"]),
                          ("p", ["p"]),
                          ("P", ["p"]),
                          ("b", ["p"]),
                          ("B", ["p"]),
                          ("c", ["k"]),
                          ("C", ["k"]),
                          ("j", ["w"]),
                          ("J", ["w"]),
                          ("S", ["k"]),
                          ("N", ["N"]),
                          ("Y", ["Y"]),
                          ("R", ["R"]),
                          ("n", ["n"]),
                          ("m", ["m"]),
                          ("s", ["H"]),
                          ("r", ["H"])
                          # deal with the consonant clusters in sandhifier
                          ]

cC_words_sandhi_initials = ["c", "C"]
cC_words_sandhi = [("a", ["cC", "cC"]),
                   ("A", ["c", "C"]),
                   ("i", ["cC", "cC"]),
                   ("I", ["c", "C"]),
                   ("u", ["cC", "cC"]),
                   ("U", ["c", "C"]),
                   ("f", ["cC", "cC"]),
                   ("e", ["cC", "cC"]),
                   ("E", ["c", "C"]),
                   ("o", ["cC", "cC"]),
                   ("O", ["c", "C"])
                   ]

punar_sandhi_initials = ['k', 'K', 'g', 'G', 'c', 'C', 'j', 'J', 'w', 'W', 'q', 'Q', 't', 'T', 'd', 'D', 'p', 'P', 'b', 'B', 'N', 'Y', 'R', 'n', 'm', 'y', 'r', 'l', 'v', 'S', 'z', 's', 'h', 'a', 'A', 'A', 'i', 'i', 'u', 'U', 'f', 'e', 'E', 'o', 'O']
punar_sandhi = [('r', ['H', 'H', 'r', 'r', 'H', 'H', 'r', 'r', 'H', 'H', 'r', 'r', 'H', 'H', 'r', 'r', 'H', 'H', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'])
                ]

total_output = ['# this file is the output of generate_rules_from_tables.py\n# the tables are "unpacked" and transcoded to SLP1 in input/sandhi-charts/*.csv\n']

vowel_sandhi_msg = '# {final: [(initial, sandhied), ...], ...}\n# for i I u U, the application of these rules only when the form is not a dual has no incidence in the need to generate all sandhied forms here'
vowel_sandhi_name = 'vowel_sandhi = {'
total_output.append(generate_sandhis(vowel_sandhi_initials, vowel_sandhi, vowel_sandhi_name, vowel_sandhi_msg))

cons_sandhi1_msg = '# {final: [(initial, (new_final, new_initial)), ...], ...}'
cons_sandhi1_name = 'consonant_sandhi_1 = {'
total_output.append(generate_consonant_sandhi_1(consonant_sandhi_1_initials, consonant_sandhi_1, cons_sandhi1_name, cons_sandhi1_msg))

cons_sandhi2_msg = '# {final: [(initial, newFinal), ...], ...}\n# the initial consonant is unchanged'
cons_sandhi2_name = 'consonant_sandhi_2 = {'
total_output.append(generate_sandhis(consonant_sandhi_2_initials, consonant_sandhi_2, cons_sandhi2_name, cons_sandhi2_msg))

consonant_sandhi_1_vowels_msg = '# {finals: [(initial, new_second_final+new_final), ...], ...}\n# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged'
consonant_sandhi_1_vowels_name = 'consonant_sandhi_1_vowels = {'
total_output.append(generate_sandhis(consonant_sandhi_1_vowels_initials, consonant_sandhi_1_vowels, consonant_sandhi_1_vowels_name, consonant_sandhi_1_vowels_msg))

visarga_sandhi1_msg = '# {finals: [(initial, new_second_final+new_final), ...], ...}\n# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged'
visarga_sandhi1_name = 'visarga_sandhi_1 = {'
total_output.append(generate_sandhis(visarga_sandhi_1_initials, visarga_sandhi_1, visarga_sandhi1_name, visarga_sandhi1_msg))

visarga_sandhi2_msg = '# {finals: [(initial, new_second_final+new_final), ...], ...}\n# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged'
visarga_sandhi2_name = 'visarga_sandhi_2 = {'
total_output.append(generate_sandhis(visarga_sandhi_2_initials, visarga_sandhi_2, visarga_sandhi2_name, visarga_sandhi2_msg))

absolute_finals_sandhi_msg = '# {final: [(empty_string, new_final), ...], ...}'
absolute_finals_sandhi_name = 'absolute_finals_sandhi = {'
total_output.append(generate_sandhis(absolute_finals_sandhi_initials, absolute_finals_sandhi, absolute_finals_sandhi_name, absolute_finals_sandhi_msg))

cC_words_sandhi_msg = '# {final: [(initial, newFinal), ...], ...}\n# the final consonant is unchanged'
cC_words_sandhi_name = 'cC_words_sandhi = {'
total_output.append(generate_sandhis(cC_words_sandhi_initials, cC_words_sandhi, cC_words_sandhi_name, cC_words_sandhi_msg))

punar_sandhi_msg = '# {final: [(initial, newFinal), ...], ...}\n# the initial consonant is unchanged'
punar_sandhi_name = 'punar_sandhi = {'
total_output.append(generate_sandhis(punar_sandhi_initials, punar_sandhi, punar_sandhi_name, punar_sandhi_msg))

with open('sandhi_rules.py', 'w', -1, 'utf-8-sig') as g:
    output = '\n'.join(total_output)
    g.write(output)