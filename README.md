# NLP - Part-of-Speech Tagger
Implementation of a first-order maximum entropy Markov model for part-of-speech tagging. The tags used are those in the [Penn Treebank](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html).

## Test Set Model Accuracy: 96.3%

## Feature Classes
### 1. Bigrams
This feature class included two kinds of bigrams: `<current word, previous word>` and `<current word, next word>`. It also featurized whether the word is the first or last word of the corresponding sequence.
<br>**Ablation:** -0.014
### 2. Trigrams
This feature class generated a trigram: `<previous word, current word, next word>`, thus conditioning on both the past and the future.
<br>**Ablation:** -0.004
### 3. Prefixes
A general prefix of the word which factored in the first three letters of a word was used as a feature. Moreover, common prefixes were also featurized.
Common prefixes: `anti-`, `pre-`, `dis-`, `mis-`, `inter-`, `un-`, `non-`, `over-`, `under-`, `in-`, `im-`, `en-`, `em-`
<br>**Ablation:** -0.005
### 4. Suffixes
A general suffix of the word which factored in the last two letters of a word was used as a feature. Moreover, common suffixes were also featurized.
Common suffixes: `-ly`, `-ing`, `-ness`, `-ity`, `-ed`, `-able`, `-s`, `-ion`, `-al`, `-ive`, `-er`, `-est`, `-day`
<br>**Ablation:** -0.019
### 5. Miscellaneous
This feature class included a random mix of simple features, with the intention to slightly improve the baseline accuracy: `<word, previous tag>`, whether the word is in ALL CAPS, whether the word begins with a capital letter, whether the word is hyphenated, whether the word contains a numeral.
<br>**Ablation:** -0.009
### 6. Specials
This feature class included two special features. One was to featurize if the previous word is a determiner – ‘a’, ‘an’ or ‘the’. The second was intended to featurize the name of a company. The way this was attempted was that if the word began with a capital letter and had the words ‘co.’, ‘inc.’, ‘llc’, ‘ltd.’, ‘pvt.’, ‘company’ or ‘corp’ within 3 words before or after it, it would be featurized as the name of a company.
<br>**Ablation:** -0.002

## Dataset
Penn Treebank / Wall Street Journal
