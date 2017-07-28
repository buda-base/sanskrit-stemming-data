def generate_sandhi_rules(initials, sandhi):
    rules = []
    for final, sandhied_forms in sandhi:
        rule = (final, [])
        for num, form in enumerate(sandhied_forms):
            rule[1].append((initials[num], form))
        rules.append(rule)
    return rules

def generate_sandhis(initials, sandhi_rules, name, comment):
    vowel = generate_sandhi_rules(initials, sandhi_rules)
    print(comment)
    print(name)
    for final, rules in vowel:
        print('\t\t"{}": ['.format(final))
        formatted_rules = []
        for rule in rules:        
            formatted_rules.append('\t\t\t\t("{}", "{}")'.format(rule[0], rule[1]))
        print(',\n'.join(formatted_rules)+'],')
    print('\t\t\t}')

def generate_consonant_sandhi_1(initials, sandhi_rules, name, comment):
    cons_sandhi1 = generate_sandhi_rules(initials, sandhi_rules)
    print(comment)
    print(name)
    groups = []
    for final, rules in cons_sandhi1:
        formatted_rules = []
        for rule in rules:
            sandhi = rule[1]
            if '(' in sandhi:
                parts = rule[1].split('(')
                new_final = parts[0] 
                new_initial = parts[1][:-1]
                formatted_rules.append('\t\t\t("{}", ("{}", "{}"), "")'.format(rule[0], new_final, new_initial))
            else:
                new_final = sandhi
                new_initial = rule[0]
                formatted_rules.append('\t\t\t("{}", ("{}", "{}"))'.format(rule[0], new_final, new_initial))
        groups.append('\t\t"{}": [\n'.format(final)+',\n'.join(formatted_rules)+'\n\t\t]')
    print(',\n'.join(groups))
    print('}')

vowel_sandhi_initials = ["a", "A", "A", "i", "i", "u", "U", "f", "e", "E", "o", "O"]
vowel_sandhi = [("a", ["A", "A", "A", "e", "e", "o", "o", "ar", "E", "E", "O", "O"]),
                ("A", ["A", "A", "A", "e", "e", "o", "o", "ar", "E", "E", "O", "O"]),
                ("i", ["ya", "yA", "yA", "I", "I", "yu", "yU", "yf", "ye", "yE", "yo", "yO"]),
                ("I", ["ya", "yA", "yA", "I", "I", "yu", "yU", "yf", "ye", "yE", "yo", "yO"]),
                ("u", ["va", "vA", "vA", "vi", "vi", "U", "U", "vf", "ve", "vE", "vo", "vO"]),
                ("U", ["va", "vA", "vA", "vi", "vi", "U", "U", "vf", "ve", "vE", "vo", "vO"]),
                ("f", ["ra", "rA", "rA", "ri", "ri", "ru", "rU", "F", "re", "rE", "ro", "rO"]),
                ("e", ["e '", "a A", "a A", "a i", "a i", "a u", "a U", "a f", "a e", "a E", "a o", "a O"]),
                ("E", ["A a", "A A", "A A", "A i", "A i", "A u", "A U", "A f", "A e", "A E", "A o", "A O"]),
                ("o", ["o '", "avA", "a A", "avi", "avi", "avu", "avU", "avf", "ave", "avE", "avo", "avO"]),
                ("O", ["Ava", "AvA", "AvA", "Avi", "Avi", "Avu", "AvU", "Avf", "Ave", "AvE", "Avo", "AvO"])
                ]

consonant_sandhi_1_initials = ["a", "A", "i", "i", "u", "U", "f", "e", "E", "o", "O", "y", "r", "l", "v", "S", "S", "z", "s", "h"]
consonant_sandhi_1 = [("k", ["g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "k", "k", "g(G)"]),
                      ("w", ["q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q", "w", "w", "w", "w", "q(Q)"]),
                      ("t", ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "l", "d", "c(C)", "c(C)", "t", "t", "d(D)"]),
                      ("p", ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "p", "p", "p", "p", "b(B)"]),
                      ("N", ["NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "NN", "N", "N", "N", "N", "N", "N", "N", "N", "N"]),
                      ("n", ["nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "nn", "n", "n", "Ml", "n", "Y(S)", "Y(C)", "n", "n", "n"]),
                      ("m", ["m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "m", "M", "M", "M", "M", "M", "M", "M", "M", "M"])
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

visarga_sandhi_1_initials = ["a", "A", "i", "i", "u", "U", "f", "e", "E", "o", "O", "y", "r", "l", "v", "S", "z", "s", "h"]
visarga_sandhi_1 = [("aH", ["o'", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "o", "o", "o", "o", "aH", "aH", "aH", "o"]),
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
                    ("AH", ["AH", "AH", "A", "Ar", "A", "Ar", "AS", "AS", "A", "Ar", "A", "Ar", "AZ", "AZ", "A", "Ar", "A", "Ar", "As", "As", "A", "Ar", "A", "Ar", "AH", "AH", "A", "Ar", "A", "Ar", "A", "Ar", "A", "Ar"]),
                    ("iH", ["iH", "iH", "ir", "ir", "ir", "ir", "iS", "iS", "ir", "ir", "ir", "ir", "iz", "iz", "ir", "ir", "ir", "ir", "is", "is", "ir", "ir", "ir", "ir", "iH", "iH", "ir", "ir", "ir", "ir", "ir", "ir", "ir", "ir"]),
                    ("IH", ["IH", "IH", "Ir", "Ir", "Ir", "Ir", "IS", "IS", "Ir", "Ir", "Ir", "Ir", "Iz", "Iz", "Ir", "Ir", "Ir", "Ir", "Is", "Is", "Ir", "Ir", "Ir", "Ir", "IH", "IH", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir", "Ir"]),
                    ("uH", ["uH", "uH", "ur", "ur", "ur", "ur", "uS", "uS", "ur", "ur", "ur", "ur", "uz", "uz", "ur", "ur", "ur", "ur", "us", "us", "ur", "ur", "ur", "ur", "uH", "uH", "ur", "ur", "ur", "ur", "ur", "ur", "ur", "ur"]),
                    ("UH", ["UH", "UH", "Ur", "Ur", "Ur", "Ur", "US", "US", "Ur", "Ur", "Ur", "Ur", "Uz", "Uz", "Ur", "Ur", "Ur", "Ur", "Us", "Us", "Ur", "Ur", "Ur", "Ur", "UH", "UH", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur", "Ur"]),
                    ("eH", ["eH", "eH", "er", "er", "er", "er", "eS", "eS", "er", "er", "er", "er", "ez", "ez", "er", "er", "er", "er", "es", "es", "er", "er", "er", "er", "eH", "eH", "er", "er", "er", "er", "er", "er", "er", "er"]),
                    ("oH", ["oH", "oH", "or", "or", "or", "or", "oS", "oS", "or", "or", "or", "or", "oz", "oz", "or", "or", "or", "or", "os", "os", "or", "or", "or", "or", "oH", "oH", "or", "or", "or", "or", "or", "or", "or", "or"]),
                    ("EH", ["EH", "EH", "Er", "Er", "Er", "Er", "ES", "ES", "Er", "Er", "Er", "Er", "Ez", "Ez", "Er", "Er", "Er", "Er", "Es", "Es", "Er", "Er", "Er", "Er", "EH", "EH", "Er", "Er", "Er", "Er", "Er", "Er", "Er", "Er"]),
                    ("OH", ["OH", "OH", "Or", "Or", "Or", "Or", "OS", "OS", "Or", "Or", "Or", "Or", "Oz", "Oz", "Or", "Or", "Or", "Or", "Os", "Os", "Or", "Or", "Or", "Or", "OH", "OH", "Or", "Or", "Or", "Or", "Or", "Or", "Or", "Or"])
                    ]

vowel_sandhi_msg = '# {final: [(initial, sandhied), ...], ...}\n# for i I u U, the application of these rules only when the form is not a dual has no incidence in the need to generate all sandhied forms here'
vowel_sandhi_name = 'vowel_sandhi = {'
# generate_sandhis(vowel_sandhi_initials, vowel_sandhi, vowel_sandhi_name, vowel_sandhi_msg)

cons_sandhi1_msg = '# {final: [(initial, (new_final, new_initial)), ...], ...}'
cons_sandhi1_name = 'consonant_sandhi_1 = {'
# generate_consonant_sandhi_1(consonant_sandhi_1_initials, consonant_sandhi_1, cons_sandhi1_name, cons_sandhi1_msg)

cons_sandhi2_msg = '# {final: [(initial, newFinal), ...], ...}\n# the initial consonant is unchanged'
cons_sandhi2_name = 'consonant_sandhi_2 = {'
# generate_sandhis(consonant_sandhi_2_initials, consonant_sandhi_2, cons_sandhi2_name, cons_sandhi2_msg)

visarga_sandhi1_msg = '# {final: [(initial, new_second_final+new_final), ...], ...}\n# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged'
visarga_sandhi1_name = 'visarga_sandhi_1 = {'
# generate_sandhis(visarga_sandhi_1_initials, visarga_sandhi_1, visarga_sandhi1_name, visarga_sandhi1_msg)

visarga_sandhi2_msg = '# {final: [(initial, new_second_final+new_final), ...], ...}\n# "new_second_final+new_final" replace the last two caracters of the previous word while the initial is unchanged'
visarga_sandhi2_name = 'visarga_sandhi_2 = {'
# generate_sandhis(visarga_sandhi_2_initials, visarga_sandhi_2, visarga_sandhi2_name, visarga_sandhi2_msg)
