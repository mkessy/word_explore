


import pickle

words = pickle.load(open('word_files/words.txt'))

#for word, defn in words.items():
#    print word+'\n\n'
#    print defn+'\n\n'

foreigns = pickle.load(open('word_files/foreigns.txt'))
for word in foreigns:
    print word

crossrefs = pickle.load(open('word_files/crossrefs.txt'))
for word in crossrefs:
    print word
