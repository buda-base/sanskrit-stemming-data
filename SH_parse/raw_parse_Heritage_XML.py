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
    mod_str = mod_str.replace('_', '').replace('+', '').replace('/', '')
    
    return mod_str


def parse_corrected_amb_stems():
    raw_lines = open_file('../input/heritage_ambiguous_stems_corrected.csv').strip().split('\n')[1:]
    parsed = {}
    for line in raw_lines:
        parts = line.split(',')
        if parts[2] != '' and parts[3] != '':
            parsed[(parts[0], parts[1])] = (parts[2], parts[3])
    return parsed


in_path = '../input/Heritage_XML'
output = defaultdict(list)
for file in os.listdir(in_path):
    raw_xml = open_file('{}/{}'.format(in_path, file)).split('\n')
    for line in raw_xml:
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

        if form != [] and stem != []:
            output[form].append(stem)

# raw pairs
write_file('../output/heritage_raw_pairs.txt', '\n'.join([a+','+'/'.join(list(set(b))) for a, b in output.items()]))
