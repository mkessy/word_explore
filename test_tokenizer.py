
import re
import nltk
import pprint
import pickle

#load up the word files

with open('word_files/p_words.txt', 'r') as words:
    word_dict = pickle.load(words)

with open('word_files/p_foreigns.txt', 'r') as foreigns:
    foreigns = pickle.load(foreigns)

with open('word_files/p_crossrefs.txt', 'r') as crossrefs:
    crossrefs = pickle.load(crossrefs)


def tokenize_and_print(word):

    print '\n'+word.encode('utf-8') + '\n\n'

    print 'Untokenized version of word etymology string\n'
    print '\t'+word_dict[word].encode('utf-8')

    tokenized = nltk.sent_tokenize(word_dict[word])
    print '\n\nTokenized sentences\n'
    print '\n--------\n'.join(map(lambda x: x.encode('utf-8') , tokenized))


def smart_tokenize_and_print(text):

    punkttt = nltk.tokenize.PunktSentenceTokenizer()

    abrvs = ['i.e', 'e.g', 'cf', 'Sgt', 'sgt', ]
    for abbrev in abrvs:
        punkttt._params.abbrev_types.add(abbrev)

    return list(punkttt.sentences_from_text(text, True))


def main():
    #tokenize_and_print('happy (adj.)')
    #tokenize_and_print('sad (adj.)')
    #tokenize_and_print('elation (n.)')
    pprint.pprint(smart_tokenize_and_print(word_dict['sad (adj.)']))

if __name__ == '__main__':
    main()
