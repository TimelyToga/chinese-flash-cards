# chinese-flash-cards
Lists of all my Chinese flashcards. I've been studying Chinese since 2014 and have created quite a few flashcards over the years. While not entirely accurate, this list of flashcards is a rough equivalent to the size of my Chinese vocabulary (~1.5k flashcards, and rough vocab of ~2-3k words).

I have included a script `combine.py` that will generate a single file `.tsv` file from all the files in `sets/` and output it in `final/`.

## Run instructions 
In order to generate a new combined flashcard file, simply run: 

```
python3 combine.py
```

The program will print something like the following: 
```
...
Parsing set: sets/第三十一课：爱人，先生，太太.tsv
Parsed 1575 terms
1425 unique terms from 36 files
150 duplicate definitions merged


Successfully wrote 1425 flashcards to final/all-terms__1630538006.tsv.
```

## Contribution 
If you have some Mandarin flashcards that you would like to contribute, feel free to open a PR. 