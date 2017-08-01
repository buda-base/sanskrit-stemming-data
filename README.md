# Data for testing the Sanskrit Lucene analyzers

## Generated resources

##### `output/heritage_forms_total.txt`
A general purpose Sanskrit word-list.
Each line is formatted as follows: `inflected<space>operation`

`operation` (to reconstruct the lemma) can have the following values:
  - `\lemma`: the lemma is inserted when more than the operations below are required to find it from the inflected form 
  - `\=`: the inflected form and the lemma are identical
  - `\>NUM`: remove NUM characters at the end of the inflected form
  - `\<NUM`: remove NUM characters at the beginning of the inflected form
  - `\<NUMa>NUMb`: remove NUMa characters at the beginning and NUMb characters at the end of the inflected form

##### Test-set 

###### minimal
 - `test_sentence.txt`: 
 - `test_vocab.txt`: 

###### kautalyarthasastra

