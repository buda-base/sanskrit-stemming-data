from sandhi_engine import *


def test_sandhis(to_sandhify):
    """
    
    :param to_sandhify: can be 
                        - a string containing: word1<space>word2/sandhied_form
                        - a tuple containing: word1, word2, sandhied_form
                        - a list of tuples
                        - a dict where key=word1 and value=list_of_tuples containing: word2, sandhied_form
    """
    def check_output(one, two, expected, found):
        if found == expected:
            output.append('OK: {} + {} => {}'.format(one, two, found))
        else:
            output.append('NO! {} + {} => {} instead of "{}"'.format(one, two, found, expected))
    
    output = []
    if type(to_sandhify) == str and ' ' in to_sandhify:
        to_apply, expected = to_sandhify.split('/')
        one, two = to_apply.split(' ')
        found = apply_sandhi(one, two)
        check_output(one, two, expected, found)
        
    elif type(to_sandhify) == tuple:
        one, two, expected = to_sandhify[0], to_sandhify[1], to_sandhify[2]
        found = apply_sandhi(one, two)
        check_output(one, two, expected, found)
        
    elif type(to_sandhify) == list:
        for pair in to_sandhify:
            one, two = pair[0], pair[1]
            apply_sandhi(one, two)
            check_output(one, two, expected, found)
    elif type(to_sandhify) == dict:
        for one, nexts in to_sandhify.items():
            for two in nexts:
                found = apply_sandhi(current, n)
                check_output(one, two, expected, found)
    return '\n'.join(output)

print(test_sandhis('pustakam /pustakam'))

UBC_examples = [
    ('\t~C V~', ['tat eva/tad eva']),
    ('\n\t~V C~', ['samyak asti/samyag asti']),
    ('\n\t~V V~', ['rAmasya cAtraH/rAmasya cCatraH']), # does not work because no rule found in the tables
    ('\n\thomorganic vowels', ['mA astu/mAstu', 'gacCati iti/gacCatIti', 'guru upeti/gurUpeti']),
    ('\n\tguṇation', ['na iti/neti', 'rAmeRa uktaH/rAmeRoktaH', 'mahA fziH/maharziH']),
    ('\n\tvṛddhization', ['na eti/nEti', 'mahA ozaDiH/mahOzaDiH', 'rAmasya Ekyam/rAmasyEkyam']),
    ('\n\tsemivowels', ['iti uvAca/ityuvAca', 'devI asti/devyasti', 'devI AgacCati/devyAgacCati', 'kuru adya/kurvadya', 'bahu iti/bahviti', 'maDu admi/maDvadmi', 'guru Asanam/gurvAsanam']),
    ('\n\tguṇa vowels', ["te api/te 'pi", 'te uvAca/ta uvAca', 'gfhe uta/gfha uta']),
    ('\n\tvṛḍdhi vowels', ['SriyE arTaH/SriyA arTaH', 'uBO uvAca/uBAvuvAca']),
    ('\n\tFinal: non-palatal stops', ['anuzwuB /anuzwup', 'suhfd /suhft']), # the space stands for an empty string, triggering the final sandhi.
    ('\n\tFinal: palatal stops', ['vAc /vAk', 'virAj /virAw', 'diS /dik']),
    ('\n\tFinal: nasals', ['pustakam /pustakam', 'karman /karman']),
    ('\n\tFinal: s and r', ['tapas /tapaH', 'pitar /pitaH']),
    ('\n\tFinal: consonant clusters', ['bhavant /bhavan', 'bhavantkgtrnp /bhavan'])
    ]

for title, examples in UBC_examples:
    print(title)
    for ex in examples:
        print(test_sandhis(ex))