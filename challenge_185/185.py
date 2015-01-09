# this program takes in a text file filled with words, 
# takes all the words that start with 'at', and 
# replaces it with '@', for twitter names.  It then orders 
# the options by the 10 longest and 10 shortest.

import sys


arg1 = sys.argv[1]
    
words = open(arg1)
words = words.read()
words.splitlines()
word_list = words.split()
        
final_list = []
        
for x in word_list:
    if x[0] == 'a' and x[1] == 't':
		final_list.append(x)
    				
final_list.sort()
final_list.sort(key=len)

x = final_list[:10]
y = final_list[-10:]

print "The shortest words are ..."
for t in x:
	print "%s : %s" % (t.replace('at', '@'), t)

print "And the longest words are ..."
for u in y:
	print "%s : %s" % (u.replace('at', '@'), u)