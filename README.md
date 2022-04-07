# QWERTY WEIGHTED LEVENSHTEIN

Implementation of Levensthtein and Damerau-Levenshtein edit distances (and similarity) weighted on the QWERTY keyboard proximity.

Not all edits are equal! Insertions and substitutions of characters should be considered differently if the characters are close to each other in a standard QWERTY keyboard.

This library it gives different distances based on the closeness of characters in the keyboard and it returns the Levensthtein edit distance (insertion, deletion, substition of characters) as well as Damerau-Levenshtein distance

It also provides similarity scores from 0.0 to 1.0 denoting how similar the two strings are.

## Install

```terminal
pip install qwerty_weighted_levenshtein
```

## Usage

Basic use:

```python
from qwerty_weighted_levenshtein import qwerty_weighted_levenshtein
qwerty_weighted_levenshtein("test", "pest") # It returns 1.0 as it requires one substitution (t > p = 1.0)
qwerty_weighted_levenshtein("test", "yest") # It returns 0.7 as t and y are close in the keyboard (t > y = 0.7)
```

## More info

- [Weighting Edit Distance to
Improve Spelling Correction in
Music Entity Search](http://www.diva-portal.org/smash/get/diva2:1116701/FULLTEXT01.pdf): Master's thesis of A. Samuellson implementing same principle for Spotify Search engine and showing correlation between physical position of keys on the keyboard and spelling mistakes/
- [infoscout/weighted-levenshtein](https://github.com/infoscout/weighted-levenshtein): Cython library implementing weighted Levensthein distance function.
- [Damerau-Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance#Distance_with_adjacent_transpositions)

## License

Released under the MIT license.

```txt
MIT License

Copyright (c) 2022 Daniele Volpi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
