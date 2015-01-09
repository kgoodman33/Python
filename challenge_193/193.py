# this program takes in a sentence, and if ther are
# acronyms in it, spells them out as full words.
# ex) "Hey guys lol hf!" > "Hey guys laugh out loud have fun!"

import sys
    
arg1 = sys.argv[1]
    
phrases = {
    'lol': "laugh out loud",
    'dw': "don't worry",
    'hf': "have fun",
    'gg': "good game",
    'brb': "be right back",
    'g2g': "got to go",
    'wtf': "what the fuck",
    'wp': "well played",
    'gl': "good luck",
    'imo': "in my opinion",
    	
}    

words = []
words = arg1.split(" ")
sentence = []
for word in words:
    if word in phrases:
    	sentence.append(phrases[word])
    else:
    	sentence.append(word)
print " ".join(sentence)