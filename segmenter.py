#Segmenter for word explore, contains algorithm and testing suites
import pprint
import nltk
import simplejson as json

#How to add abbreviations to train the punkt tokenizer
#def extract_sentences(text):
#    punkttt = nltk.tokenize.PunktSentenceTokenizer()
#
#    #list of abbreviations remove last period from abbr.
#    # example list: ['i.e','e.g']
#    abbreviations = []
#
#
#    for abbrev in abbreviations:
#        punkttt._params.abbrev_types.add(abbrev)
#    return punkttt.sentences_from_text(text, True)

def extract_sent(text):
    """extracts sentences from text
    returns a generator of sentences"""

    punkt_tokenizer = nltk.tokenize.PunktSentenceTokenizer()

    #abbrevs is a list of abbrevs that punkt should exempt from
    #end of line analysis, for example: 'e.g.' should not be a break
    #point for a new sentence, this list will likely grow as we train
    #the tokenizer are more text

    abbrevs = [
               'cf',
               'e.g',
               'Sgt',
               'sgt',
               'etc',
               'adv',
               'n',
               'v',
               'adj',
               'pron',
               '+',
               ]
    #the text contains many abbreviations for centuries e.g. '12c.' or '14c.'
    #so these must be exempted for causing sentence breaks
    abbrevs = abbrevs + [str(date)+'c' for date in range(1,20)]
    for abbrev in abbrevs:
        punkt_tokenizer._params.abbrev_types.add(abbrev)

    return punkt_tokenizer.sentences_from_text(text, realign_boundaries=True)

def print_test(test_sents):

    for word, tokenized_sent in test_sents:
        print 'Word:\t%s\n\n' % (word)
        pprint.pprint(tokenized_sent)
        print '\n===================================\n'

def seg_test():
    """Tests the quality of the segmenter based of a predefined
    gold standard. Gold standard is loaded from a file."""

    with open('word_files/j_words.txt') as wf:
        words = json.load(wf)

    test_words = [
                  'king (n.)',
                  'bleach (v.)',
                  'antithesis (n.)',
                  'face (n.)',
                  'porpoise (n.)',
                  'dealer (n.)',
                  'poise (n.)',
                  'spirit (n.)',
                  'edgeways',
                  'bunch (n.)',
                  'case (n.2)',
                  'hog (n.)',
                  'begetter (n.)',
                  'cap (n.)',
                 ]

    test_sents = [(test_word, words[test_word].split('\n')[0]) for test_word in test_words]
    test_sents = [(test_word, list(extract_sent(sent))) for test_word, sent in test_sents]
    print_test(test_sents)

if __name__ == '__main__':
    seg_test()
