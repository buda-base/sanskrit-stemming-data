## 1 `input/sandhi-charts` (manually done)

##### Input
 - the 5 sandhi charts found on [UBC Sanskrit](https://ubcsanskrit.ca/lesson3/sandhicharts.html)'s website
 
##### Action
 - The charts are transcoded in [SLP1](https://en.wikipedia.org/wiki/SLP1)
 - The tables are "unpacked" (for ex. [here](../input/sandhi-charts/UBC_sandhi_charts_consonants2.csv))
 - The exceptions and special rules are integrated in the unpacked tables

##### Output
 - `input/sandhi-charts/UBC_sandhi_charts.ods`
 - The corresponding `.csv` files in `input/sandhi-charts/`

## 2 `sandhifier.py`

##### Input
 - `output/heritage_raw_pairs.txt` from `raw_parse_Heritage_XML.py`
 - `sandhi_rules.py`

##### Action
 - generates all the sandhied forms for every inflected form in `heritage_raw_pairs.txt` (see the docstrings in the code for more details)
 - generate the diff to get back to the lemma and the un-sandhied initial character of next word

##### Output
 - `total_output.txt` (see [here](../README.md#outputtotal_outputtxt) for a description)
