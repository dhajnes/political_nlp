# -*- coding: utf8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.tokenize import RegexpTokenizer
from stemmsk import stem

def clean_slovak_word(word):
    special_chars = {"á": "a", "ä": "a", "č":"c", "ď":"d", "é":"e", "í":"i", "ľ":"l", "ĺ":"l", "ň":"n", "ó":"o", "ô":"o", "ŕ":"r", "š":"s", "ť":"t", "ú":"u", "ý":"y", "ž":"z"}
    chars = []
    for i, char in enumerate(word):
        if char in special_chars.keys():
            chars.append(special_chars[char])
        else:
            chars.append(char)
    return "".join(chars)


text = None
with open("transcripts/fico-kollar-v-politike-gpt3.txt") as txt:
    text = txt.read()

# words = nltk.tokenize.wordpunct_tokenize(text)
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(text)
print(len(words))

freq_dict = {}
for word in words:
    stemmed_word = stem(word)
    if stemmed_word in freq_dict:
        freq_dict[stemmed_word] += 1
    else:
        freq_dict[stemmed_word] = 1

sorted_freq_dict = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)


# Extract labels and counts from the list of tuples
labels, counts = zip(*sorted_freq_dict[25:74])

# Create a histogram

plt_1 = plt.figure(figsize=(25, 10))
plt.bar(labels, counts, width=5)
# print(labels)

plt.xticks(rotation=60)

# Add labels and title
plt.xlabel("Labels")
plt.ylabel("Counts")
plt.title("Histogram of Labels and Counts")
# plt.figure().set_figwidth(15)
# plt.figure().set_figheight(5)

# Show the histogram
# plt.show()
plt.savefig("figs/output.pdf", dpi=300)
