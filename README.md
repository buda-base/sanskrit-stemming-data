# Data for the Sanskrit Lucene analyzers 

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

#### `output/trie_content.txt`
A word-list containing all the sandhied inflected forms in Heritage's XML files and the files in `input/custom_entries/`.

Since this file is 128mo at writing time, it won't be included in the repository, but will need to be generated with the following command:
```
python3 sandhify/sandhifier.py
```

Each line is formatted as follows:

 * `<sandhied_inflected_form>,<initial>$<diffs>/<initial_diff>=<sandhi_type>#<POS>`
 * `<diffs>`: `<diff_to_1st_lemma>;<diff_to_2nd_lemma>;…`
 * `<diff_to_nth_lemma>`: `-<number_of_chars_to_delete>+<chars_to_add>`
 * `<initial_diff>`: `-<sandhied_initial>+<initial>`
 * `<sandhi_type>`:  
    * `0`: no sandhi
    * `1`: vowel sandhi
    * `2`: consonant sandhi 1
    * `3`: consonant sandhi 2
    * `4`: visarga sandhi
    * `5`: absolute finals sandhi
    * `6`: "cC"-words sandhi
    * `7`: special sandhi: "punar" 
 * `<POS>`:
    * `-1`: multi-token lemma (see below)
    * `0`: Indeclinable
    * `1`: Noun
    * `2`: Pronoun
    * `3`: Verb
    * `4`: Preverb

The space between the sandhied words is preserved except for the vowel sandhis where the final and initial vowels coalesce.

###### Example 1: `prezyate,a$-1+;-6+I/-'+a=1`,

 - inflected form: `prezyate`
 - initial character of next word: `a`
 - diff of first corresponding lemma: `-1+` (lemma = `prezyat`)
 - diff of second corresponding lemma: `-6+I` (lemma = `prI`)
 - diff to undo sandhi of initial character of next word: `-'+a` (initial = `a`, sandhied initial = `'`)
 - sandhi type: `=1`, vowel sandhi 

###### Example 2: `aprezyata,A:i:u:U:f:e:E:o:O$-1+;-6+I/=1`

 - inflected form: `aprezyata`
 - possible initial characters for this inflected form: `A`, `i`, `u`, `U`, `f`, `e`, `E`, `o` and `O`
 - diff of first corresponding lemma: `-1+` (lemma = `aprezyat`)
 - diff of second corresponding lemma: `-6+I` (lemma = `aprI`)
 - sandhi type: `=1`, vowel sandhi

#### POS tags

The Part-of-Speech tags are attributed based on the file of origin in the [Sanskrit Heritage Resources](input/Heritage_XML).

 * `SL_indecls.xml`:    Indeclinable
 * `SL_final.xml`:      Noun
 * `SL_nouns.xml`:      Noun
 * `SL_pronouns.xml`:   Pronoun
 * `SL_roots.xml`:      Verb
 * `SL_parts.xml`:      Verb

#### Multi-token Lemmas

As a workaround to the incorrect segmentation that is unavoidable with the Maximal Matching strategy,
we provide support for multi-token lemmas.

For ex., `atikramati` should be segmented in `ati kramati`, yet `atikrama` is longer than `ati`. 
So, the Maximal Matching algorithm will take the longest existing word and segment it as `atikrama ti`.
We propose to add to the lexical resources a new entry for `atikramati` as a whole, with the following format:

 * `<inflected_form>,<multi-token_lemma>`
 * `<multi-token_lemma>`: `<token1>⟾<token2>⟾<tokenN>`
 * `<token>`: `<token_string><POS_number>_<indices>`
 * `<indices>`: `<start>><end>` (from the first character)

Thus, `atikramati,ati4_1>3⟾kram3_4>10_-1` is analyzed as follows:

 * `atikramati`: inflected form
 * `ati4_1>3`: lemma: `ati`, POS: `Preverb`, starting char: `1`, ending char: `3`
 * `kram3_4>10`: lemma: `kram`, POS: `Verb`, starting char: `4`, ending char: `10`
 * `_-1`: POS: `multi-lemma token`

Note: see [this readme](./sandhify/Readme.md)
