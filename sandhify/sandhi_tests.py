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
        if len(found) > 1:
            if expected in found:
                output.append("ok. {} + {} => {}            (most probably a special case. see UBC's tables)".format(one, two, ' OR '.join(found)))
            else:
                output.append('NO! {} + {} => {}. Expected:"{}"'.format(one, two, ' OR '.join(found), expected))
        elif len(found) == 1:
            if expected in found:
                output.append('ok. {} + {} => {}'.format(one, two, ' OR '.join(found)))
            else:
                output.append('NO! {} + {} => {}. Expected:"{}"'.format(one, two, ' OR '.join(found), expected))
    
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

UBC_examples = [
    ('\t~C V~', ['tat eva/tad eva']),
    ('\n\t~V C~', ['samyak asti/samyag asti']),
    ('\n\t~V V~', ['rAmasya cAtraH/rAmasya cCAtraH']), # does not work because no rule found in the tables
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
    ('\n\tFinal: consonant clusters', ['bhavant /bhavan', 'bhavantkgtrnp /bhavan']),
    ('\n\tfinal dentals', ['Bavat janma/Bavaj janma', 'etat Danam/etad Danam', 'Bavat deham/Bavad deham', 'tat Saram/tac Caram']),
    ('\n\tfinal m', ['pustakam paWati/pustakaM paWati', 'vanam gacCAmi/vanaM gacCAmi']),
    ('\n\tfinal n', ['mahAn qamaraH/mahAR qamaraH', 'etAn cCAtraH/etAMS cCAtraH', 'gacCan ca/gacCaMS ca', 'tAn tAn/tAMs tAn', 'asmin wIkA/asmiMz wIkA']),  # etAn gacCati changed to cCatraH (n+g = n g, following table)
    ('\n\tbefore l', ['tat lokaH/tal lokaH', 'tAn lokAn/tAM lokAn']),
    ('\n\tbefore h', ['vAk hi/vAg Gi', 'tat hi/tad Di']),
    ('\n\t-aḥ sandhi', ['rAmaH gacCati/rAmo gacCati', "rAmaH asti/rAmo 'sti", 'rAmaH karoti/rAmaH karoti', 'rAmaH calati/rAmaS calati', 'rAmaH wIkAm/rAmaz wIkAm', 'rAmaH tu/rAmas tu', 'rAmaH patati/rAmaH patati', 'rAmaH uvAca/rAma uvAca']),
    ('\n\t-āḥ sandhi', ['devAH vadanti/devA vadanti', 'devAH eva/devA eva', 'devAH kurvanti/devAH kurvanti', 'devAH patanti/devAH patanti', 'devAH ca/devAS ca', 'devAH wIkA/devAz wIkA', 'devAH tu/devAs tu']),
    ('\n\t-iḥ -īḥ -uḥ -ūḥ -eḥ -oḥ -aiḥ -auḥ', ['muniH vadati/munir vadati', 'tEH uktam/tEr uktam', 'BUH Buvas/BUr Buvas', 'muniH karoti/muniH karoti', 'agniH ca/agniS ca', 'muneH wIkAm/munez wIkAm', 'tEH tu/tEs tu', 'guruH patati/guruH patati']),
    ('\n\tException: punar', ['punar punar/punaH punar', 'punar milAmaH/punar milAmaH', 'punar ramati/punaH ramati', 'punar uvAca/punar uvAca'])
    ]

output = []
for title, examples in UBC_examples:
    output.append(title)
    for ex in examples:
        output.append(test_sandhis(ex))

with open('test_log.txt', 'w', -1, 'utf-8-sig') as g:
    output = '\n'.join(output)
    g.write(output)