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

 - `<sandhied_inflected_form>,<initial>~<diffs>/<initial_diff>=<sandhi_type>`
 - `<diffs>`: `<diff_to_1st_lemma>;<diff_to_2nd_lemma>;…`
 - `<diff_to_nth_lemma>`: `-<number_of_chars_to_delete>+<chars_to_add>`
 - `<initial_diff>`: `-<sandhied_initial>+<initial>`
 - `<sandhi_type>`:  
 					- 0: no sandhi
 					- 1: vowel sandhi
 					- 2: consonant sandhi 1
 					- 3: consonant sandhi 2
 					- 4: visarga sandhi
 					- 5: absolute finals sandhi
 					- 6: "cC"-words sandhi
 					- 7: special sandhi: "punar" 

The space between the sandhied words is preserved except for the vowel sandhis where the final and initial vowels coalesce.

###### Example 1: `prezyate,a~-1+;-6+I/-'+a=1`,

 - inflected form: `prezyate`
 - initial character of next word: `a`
 - diff of first corresponding lemma: `-1+` (lemma = `prezyat`)
 - diff of second corresponding lemma: `-6+I` (lemma = `prI`)
 - diff to undo sandhi of initial character of next word: `-'+a` (initial = `a`, sandhied initial = `'`)
 - sandhi type: `=1`, vowel sandhi 

###### Example 2: `aprezyata,A:i:u:U:f:e:E:o:O~-1+;-6+I/=1`

 - inflected form: `aprezyata`
 - possible initial characters for this inflected form: `A`, `i`, `u`, `U`, `f`, `e`, `E`, `o` and `O`
 - diff of first corresponding lemma: `-1+` (lemma = `aprezyat`)
 - diff of second corresponding lemma: `-6+I` (lemma = `aprI`)
 - sandhi type: `=1`, vowel sandhi

Note: see [this readme](./sandhify/Readme.md)