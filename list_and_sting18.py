#!/usr/bin/python
def fanyi(sentence):
    word_list = sentence.split(' ')
    ordered_word_list = []
    for word in word_list:
	ordered_word = word[1:]+word[0].lower() +'ay'
	ordered_word_list.append(ordered_word)
    ordered_word_list[0]=ordered_word_list[0].capitalize()
    ordered_sentence = (' ').join(ordered_word_list)   
    return ordered_sentence


testsentence ="The quick brown fox" 


print "Befor fanyi"
print testsentence
print "After fanyi"
print fanyi(testsentence)
