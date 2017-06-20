#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
from collections import defaultdict

def write_file(file_path, content):
    with open(file_path, mode='w') as f:
        f.write(content)


def open_file(file_path):
    try:
        with open(file_path, mode='r') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, mode='r', encoding='utf-16-le') as f:
            return f.read()

def remove_SLP1_modifiers(string):
    mod_str = string
    # removes #NUM  from the string
    mod_str = re.sub(r'\#([0-9]{1}|[0-9]{2})', r'', mod_str)
    # remove other modifiers
    mod_str = mod_str.replace('_', '').replace('+', '')
    
    return mod_str


in_path = './Heritage_XML'
prefixed = 0
suffixed = 0
infixed = 0
indeclined = 0
total = 0
forms = []
output = defaultdict(list)
amb_stems = []
for file in os.listdir(in_path):
    raw_xml = open_file('{}/{}'.format(in_path, file)).split('\n')
    for line in raw_xml:
        total += 1
        # find the form and the stem
        form = re.findall(r'form="([^\"]+)"', line)
        stem = re.findall(r'stem="([^\"]+)"', line)
        # put in a string and remove modifiers
        if len(form) == 1:
            form = form[0]
            form = remove_SLP1_modifiers(form)
        if len(stem) == 1:
            stem = stem[0]
            stem = remove_SLP1_modifiers(stem)        

        operation = '' 
        if stem:
            if stem != form and stem in form:
                if form.startswith(stem):
                    suffix = form.replace(stem, '')
                    operation = '>'+str(len(suffix))
                    suffixed += 1
                elif form.endswith(stem):
                    prefix = form.replace(stem, '')
                    operation = '<'+str(len(prefix))
                    prefixed += 1
                else:
                    parts = form.split(stem)
                    if len(parts) == 2:
                        pre, suf = form.split(stem)
                    else:
                        amb_stems.append(line)
                    operation = '<'+str(len(pre))+'>'+str(len(suf))
                    infixed += 1
            elif stem == form:
                operation = '='
            else:
                operation = '}'+stem
        elif form:
            operation = '{'
            indeclined += 1
        
        if form:
            forms.append(form)
        
        operation = remove_SLP1_modifiers(operation)
        if form:
            output[form].append(operation)


# delete duplicates in the operations
for key, value in output.items():
    output[key] = list(set(value))

# write Heritage forms
output_list = ['{} {}'.format(key, ';'.join(value)) for key, value in output.items()]
write_file('output/heritage_forms_total.txt', '\n'.join(sorted(output_list)))

# write ambiguous stems (to be checked in the dictionary)
write_file('output/heritage_ambiguous_stems.txt', '\n'.join(amb_stems))

# list ambiguous forms
amb_forms_count = 0
amb_forms = []
for o in output_list:
    if ';' in o:
        amb_forms_count += 1
        amb_forms.append(o)
write_file('output/heritage_ambiguous_forms.txt', '\n'.join(amb_forms))

log = ''
log += 'Prefixed: ' + str(prefixed) + '\n'
log += 'Prefixed+Suffixed: ' + str(infixed) + '\n'
log += 'Suffixed: ' + str(suffixed) + '\n'
log += 'Indeclined: ' + str(indeclined) + '\n'
log += 'Total lines: ' + str(total) + '\n'
log += 'Total Unique forms: ' + str(len(set(forms))) + '\n'
log += 'Total ambiguous stems: ' + str(len(amb_stems)) + '\n'
log += 'Total ambiguous forms: ' + str(amb_forms_count)  + '\n'

print(log)
write_file('log.txt', log)