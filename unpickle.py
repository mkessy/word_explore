import pickle
import simplejson as json

allwords = pickle.load(open('word_files/p_words.txt'))
foreigns = pickle.load(open('word_files/p_foreigns.txt'))
crossrefs = pickle.load(open('word_files/p_crossrefs.txt'))

print(type(allwords))
print(type(foreigns))
print(type(crossrefs))

with open('word_files/j_words.txt', 'w') as aw:
    json.dump(allwords, aw, indent=4)

with open('word_files/j_foreigns.txt', 'w') as af:
    json.dump(list(foreigns), af)

with open('word_files/j_crossrefs.txt', 'w') as ac:
    json.dump(list(crossrefs), ac)
