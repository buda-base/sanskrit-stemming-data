# Data for testing the Sanskrit Lucene analyzers

## Generated resources

#### `output/heritage_forms_total.txt`
A general purpose Sanskrit word-list.
Each line is formatted as follows: `inflected<space>operation`

`operation` (to reconstruct the lemma) can have the following values:
  - `\lemma`: the lemma is inserted when more than the operations below are required to find it from the inflected form 
  - `\=`: the inflected form and the lemma are identical
  - `\>NUM`: remove NUM characters at the end of the inflected form
  - `\<NUM`: remove NUM characters at the beginning of the inflected form
  - `\<NUMa>NUMb`: remove NUMa characters at the beginning and NUMb characters at the end of the inflected form

Note: see [this readme](./SH_parse/Readme.md)

#### `output/total_output.txt`
A word-list containing all the sandhied inflected forms in Heritage's XML files.

Each line is formatted as follows:

 - `<sandhied_inflected_form>,<initial>,<diffs>/<initial_diff>`
 - `<diffs>`: `<diff_to_1st_lemma>;<diff_to_2nd_lemma>;…`
 - `<diff_to_nth_lemma>: '-<number_of_chars_to_delete>+<chars_to_add>`
 - `<initial_diff>: '-<sandhied_initial>+<initial>`

The space between the sandhied words is preserved except for the vowel sandhis where the final and initial vowels coalesce.

###### Example 1: `prezyate,a,-1+;-6+I/-'+a`,

 - inflected form: `prezyate`
 - initial character of next word: `a`
 - diff of first corresponding lemma: `-1+` (lemma = `prezyat`)
 - diff of second corresponding lemma: `-6+I` (lemma = `prI`)
 - diff to undo sandhi of initial character of next word: `-'+a` (initial = `a`, sandhied initial = `'`) 

###### Example 2: `aprezyata,A:i:u:U:f:e:E:o:O,-1+;-6+I/`

 - inflected form: `aprezyata`
 - possible initial characters for this inflected form: `A`, `i`, `u`, `U`, `f`, `e`, `E`, `o` and `O`
 - diff of first corresponding lemma: `-1+` (lemma = `aprezyat`)
 - diff of second corresponding lemma: `-6+I` (lemma = `aprI`)

Note: see [this readme](./sandhify/Readme.md)