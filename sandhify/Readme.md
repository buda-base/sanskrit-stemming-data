## 1 `input/sandhi-charts` (manually done)

##### Input
 - the 5 sandhi charts found on [UBC Sanskrit](https://ubcsanskrit.ca/lesson3/sandhicharts.html)'s website
 
##### Action
 - The charts are transcoded in [SLP1](https://en.wikipedia.org/wiki/SLP1)
 - The tables are "unpacked" (for ex. [here](../input/sandhi-charts/UBC_sandhi_charts_vowels.csv))
 - The exceptions and special rules are integrated in the unpacked tables

##### Output
 - `input/sandhi-charts/UBC_sandhi_charts.ods`
 - The corresponding `.csv` files in `input/sandhi-charts/`

## 2 Implement the tables in Python (manually done)

##### Input
 - `input/sandhi-charts/*.csv`

##### Action
 - Format them as in [this file](./generate_rules_from_tables.py#69)
 - Run `generate_rules_from_tables.py`

##### Output
 - The tables in `generate_rules_from_tables.py`
 - `sandhi_rules.py` to be used by `sandhifier.py`

## 3 `sandhifier.py`

##### Input
 - `output/heritage_raw_pairs.txt` from `raw_parse_Heritage_XML.py`
 - `sandhi_rules.py`

##### Action
 - generates all the sandhied forms for every inflected form in `heritage_raw_pairs.txt` (see the docstrings in the code for more details)
 - generate the diff to get back to the lemma and the un-sandhied initial character of next word

##### Output
 - `total_output.txt` (see [here](../README.md) for a description)
