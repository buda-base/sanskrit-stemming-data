## `parse_Heritage_XML.py`

##### Input
 - `input/Heritage_XML/`: The XML files copied from [Heritage Resources](https://gitlab.inria.fr/huet/Heritage_Resources)
 - `input/heritage_ambiguous_stems_corrected.csv`: A renamed copy of `output/heritage_ambiguous_stems.csv` that allows for manually deciding which occurence of the stem-string is the actual stem. To fill in the `Start idx` and `End idx` columns, find the indices counting from 1 for the first letter of the inflected form.

##### Action
 - for every XML file:
    - extracts all the form-stem pairs
    - generate the operation string described [here](../README.md)
    - prepend `\` before each stem and join all possible stems (ex: "Amayatas \>2\>3\am")

##### Output
 - `output/heritage_forms_total.txt`
 - `output/heritage_ambiguous_forms.txt`: all the ambiguous forms extracted from `heritage_forms_total.txt`
 - `output/heritage_ambiguous_stems.txt`: the forms that could not be processed automatically (see Issues)
 - `log.txt`: figures produced while parsing the XML files.

##### Issues
 - `input/heritage_ambiguous_stems_corrected.csv`: These forms contain more than one time the stem. Someone knowledgeable needs to manually process it. See Input section.
 
## `raw_parse_Heritage_XML.py`

##### Input
 - `input/Heritage_XML/`: The XML files copied from [Heritage Resources](https://gitlab.inria.fr/huet/Heritage_Resources)
 
##### Action
 - for every XML file:
    - extracts all the form-stem pairs
    - regroups all the lemmas belonging to the same inflected form, separating them with `/`
 
##### Output
 - `output/heritage_raw_pairs.txt`