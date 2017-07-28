def generate_sandhi_rules(initials, sandhi):
    rules = []
    for final, sandhied_forms in sandhi:
        rule = (final, [])
        for num, form in enumerate(sandhied_forms):
            rule[1].append((initials[num], form))
        rules.append(rule)
    return rules

def generate_vowel_sandhi(initials, sandhi_rules):
    vowel = generate_sandhi_rules(initials, sandhi_rules)
    print('# {final: [(initial, sandhied), ...], ...}')
    print('vowel_sandhi = {')
    for final, rules in vowel:
        print('\t\t"{}": ['.format(final))
        formatted_rules = []
        for rule in rules:        
            formatted_rules.append('\t\t\t\t("{}", "{}")'.format(rule[0], rule[1]))
        print(',\n'.join(formatted_rules)+'],')
    print('\t\t\t}')

def generate_consonant_sandhi_1(initials, sandhi_rules):
    cons_sandhi1 = generate_sandhi_rules(initials, sandhi_rules)
    print('# {final: [(initial, (new_final, new_initial), context), ...], ...')
    print('consonant_sandhi_1 = {')
    groups = []
    for final, rules in cons_sandhi1:
        formatted_rules = []
        for rule in rules:
            sandhi = rule[1]
            if '(' in sandhi:
                parts = rule[1].split('(')
                new_final = parts[0] 
                new_initial = parts[1][:-1]
                if '/' in new_initial:
                    new_initial = new_initial.split('/')
                    for i in new_initial:
                        formatted_rules.append('\t\t\t("{}", ("{}", "{}"), "")'.format(rule[0], new_final, i))
                else:
                    formatted_rules.append('\t\t\t("{}", ("{}", "{}"), "")'.format(rule[0], new_final, new_initial))
            else:
                new_final = sandhi
                new_initial = rule[0]
                formatted_rules.append('\t\t\t("{}", ("{}", "{}"), "")'.format(rule[0], new_final, new_initial))
        groups.append('\t\t"{}": [\n'.format(final)+',\n'.join(formatted_rules)+'\n\t\t]')
    print(',\n'.join(groups))
    print('}')

def generate_consonant_sandhi_2(initials, sandhi_rules):
    
    pass

vowel_sandhi_initials = ["a", "A", "i", "i", "u", "U", "f", "e", "E", "o", "O"]
vowel_sandhi = [("a", ["A", "A", "e", "e", "o", "o", "ar", "E", "E", "O", "O"]),
                ("A", ["A", "A", "e", "e", "o", "o", "ar", "E", "E", "O", "O"]),
                ("i", ["ya", "yA", "I", "I", "yu", "yU", "yf", "ye", "yE", "yo", "yO"]),
                ("I", ["ya", "yA", "I", "I", "yu", "yU", "yf", "ye", "yE", "yo", "yO"]),
                ("u", ["va", "vA", "vi", "vi", "U", "U", "vf", "ve", "vE", "vo", "vO"]),
                ("U", ["va", "vA", "vi", "vi", "U", "U", "vf", "ve", "vE", "vo", "vO"]),
                ("f", ["ra", "rA", "ri", "ri", "ru", "rU", "F", "re", "rE", "ro", "rO"]),
                ("e", ["e '", "a A", "a i", "a i", "a u", "a U", "a f", "a e", "a E", "a o", "a O"]),
                ("E", ["A a", "A A", "A i", "A i", "A u", "A U", "A f", "A e", "A E", "A o", "A O"]),
                ("o", ["o '", "avA", "avi", "avi", "avu", "avU", "avf", "ave", "avE", "avo", "avO"]), # alternative rule for "avA" (=>"a A") needs to be manually added
                ("O", ["Ava", "AvA", "Avi", "Avi", "Avu", "AvU", "Avf", "Ave", "AvE", "Avo", "AvO"])
                ]

consonant_sandhi_1_initials = ["a", "A", "i", "i", "u", "U", "f", "e", "E", "o", "O", "y", "r", "l", "v", "S", "z", "s", "h"]
consonant_sandhi_1 = [("k", ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "k", "k", "g(G)"]),
                      ("w", ["q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "w", "w", "w", "q(Q)"]),
                      ("t", ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "l", "d", "c(C)", "t", "t", "d(D)"]),
                      ("p", ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "p", "p", "p", "b(B)"]),
                      ("N", ["NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "N", "N", "N", "N", "N", "N", "N", "N"]),
                      ("n", ["nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "n", "n", "Ml", "n", "Y(S/C)", "n", "n", "n"]),
                      ("m", ["m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "M", "M", "M", "M", "M", "M", "M", "M"])
                      ]

consonant_sandhi_2_initials = ["k/K", "g/G", "c/C", "j/J", "w/W", "q/Q", "t/T", "d/D", "p/P", "b/B", "n/m"]
consonant_sandhi_2 = [("k", ["", "g", "", "g", "", "g", "", "g", "", "g", "N"]),
                      ("w", ["", "q", "", "q", "", "q", "", "q", "", "q", "R"]),
                      ("t", ["", "d", "c", "j", "w", "q", "", "d", "", "d", "n"]),
                      ("p", ["", "b", "", "b", "", "b", "", "b", "", "b", "m"]),
                      ("R", ["", "", "", "", "", "", "", "", "", "", ""]),
                      ("n", ["", "", "MS", "Y", "Mz", "R", "Ms", "", "", "", ""]),
                      ("m", ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"])
                      ]

visarga_sandhi_1_initials = ["vowels", "y", "r", "l", "v", "S", "z", "s", "h"]
visarga_sandhi_1 = [("aH", ["a/o'", "o", "o", "o", "o", "", "", "", "o"]),
                    ("AH", ["A", "A", "A", "A", "A", "", "", "", "A"]),
                    ("(V)H", ["r", "r", "", "r", "r", "", "", "", "r"])
                    ]

visarga_sandhi_2_initials = ["k/K", "g/G", "c/C", "j/J", "w/W", "q/Q", "t/T", "d/D", "p/P", "b/B", "n/m"]
visarga_sandhi_2 = [("aH", ["", "o", "aS", "o", "az", "o", "as", "o", "", "o", "o"]),
                    ("AH", ["", "A", "AS", "A", "AZ", "A", "As", "A", "", "A", "A"]),
                    ("(V)H", ["", "r", "S", "r", "z", "r", "s", "r", "", "r", "r"])
                    ]

# generate_vowel_sandhi(vowel_sandhi_initials, vowel_sandhi)
# generate_consonant_sandhi_1(consonant_sandhi_1_initials, consonant_sandhi_1)

