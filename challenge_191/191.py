# this program takes in a book in txt form, 
# and counts how many of each word there is.
# it prints out a dictionary of word/word count 
# keys and values

import sys
import string
import re

arg1 = sys.argv[1]

book = open(arg1)
book = book.read()


book = book.translate(None, string.punctuation)

word_list = []

for word in book.split():
	word = word.lower()
	word_list.append(word)


final_list = {}

for word in word_list:
	if word in final_list:
		final_list[word] += 1
	else:
		final_list[word] = 1
	
	

print final_list







