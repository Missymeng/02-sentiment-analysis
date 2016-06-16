# -*- coding: utf-8 -*-

senti_dict = {}

fhand = open('AFINN/AFINN-111.txt','r')
for line in fhand:
	line = line.strip()
	columns = line.split('\t')
	senti_dict[columns[0]] = columns[1]

sentence = raw_input('Enter text: ')
sentence_lowed = sentence.lower()
senti_score = 0
for (k,v) in senti_dict.items():
	if k in sentence_lowed:
		senti_score += int(v)

print "The sentiment score of %s is %d" % (sentence,senti_score)



