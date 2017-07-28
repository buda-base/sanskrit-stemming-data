from sandhi_rules import *
with open('output/heritage_forms_total.txt') as f:
    list = f.readlines()

inflected = [a.split()[0] for a in list]

for infl in inflected[:10]:
    print()
    final = infl[-1]
    if final in vowel_sandhi:
        for rule in vowel_sandhi[final]:
            print(infl[:-1]+rule[1]+' '+rule[0])

