"""

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover.
 On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""

import re

string_til_tall = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def bytt_ord(text):
    for a, b in string_til_tall.items():
        text = text.replace(a, b)
    return text

def kalibrering(text):
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n"))

text = open("dec1.txt").read()
print(kalibrering(text))
print(kalibrering(bytt_ord(text)))