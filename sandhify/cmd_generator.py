# encoding: utf-8
import os
import sys
import re
from click.decorators import command
sys.path.append(os.path.abspath(os.path.join('..', 'resources')))
from find_applicable_sandhis import FindApplicableSandhis


class CmdGenerator:
    """

    """
    def __init__(self, language):
        self.find = FindApplicableSandhis(language)

    def find_sandhis_for(self, word1, word2):
        if len(word2) > 0:
            initial_char = word2[0]
        else:
            initial_char = word2

        all_potential_sandhis = self.find.all_possible_sandhis(word1)
        
        formatted_possible_lemmas = []
        for potential_sandhi in all_potential_sandhis:
            sandhied, rest = potential_sandhi.split(',')
            potential_lemma_diffs = rest.split('|')

            possible_lemmas = []
            for potential_diff in potential_lemma_diffs:
                initials_of_potential_lemma = potential_diff.split('$')[0].split(':')
                if initial_char in initials_of_potential_lemma:
                    to_del_formatted = self.formatToDelete(potential_diff)
                    possible_lemmas.append(to_del_formatted)

            if possible_lemmas:
                formatted_possible_lemmas.append('{},{}'.format(sandhied, '|'.join(possible_lemmas)))

        if formatted_possible_lemmas:
            return self.join_complementary_entries(formatted_possible_lemmas)
        return None
    
    @staticmethod
    def adjust_new_initial_in_consonant1_sandhi(cmd):
        print(cmd)
        if '/=' not in cmd and '-+=' not in cmd and '- +=' not in cmd:
            initial, remainder = cmd.split('$')
            new_initial = cmd.split('/-')[1].split('+')[0].strip()
            if initial != new_initial:
                return '{}${}'.format(new_initial, remainder)
        return cmd
    
    @staticmethod
    def formatToDelete(command):
        if '$/' in command:
            return command
        else:
            first_part, remainder = command.split('$')
            diff, last_part = remainder.split('/')
            to_del, to_add = diff.lstrip('-').split('+')
            to_del = str(len(to_del))
            
            return '{}$-{}+{}/{}'.format(first_part, to_del, to_add, last_part) 
    
    def join_complementary_entries(self, entries):
        joined = {}
        for entry in entries:
            form, cmd = entry.split(',')
            cmd = self.adjust_new_initial_in_consonant1_sandhi(cmd)
            if form in joined.keys():
                joined[form].append(cmd)
            else:
                joined[form] = [cmd]
        
        output = []
        for form, cmds in joined.items():
            output.append('{},{}'.format(form, '|'.join(cmds)))
        
        return '\n'.join(sorted(output))
        

if __name__ == "__main__":
    lang = 'sanskrit'
    engine = CmdGenerator(lang)
    
    word1 = 'rAmaH'
    word2 = 'wikAm'
    cmd = engine.find_sandhis_for(word1, word2)
    if cmd:
        print(cmd)