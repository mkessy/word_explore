import pprint
import nltk
import simplejson as json
import segmenter

#word segmentation testing and methods


def extract_words(sent):
    """Extracts word tokens from sentences.
    Uses the TreebankWordTokenizer. Returns a generator
    of the tokenized sentence."""

    wordToken = nltk.tokenize.TreebankWordTokenizer()
    return iter(wordToken.tokenize(sent))





def token_test():
    """Test the quality of the word tokenizer based on a
    list of predfined words that have been gold standardized."""

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
    test_sents = [(test_word, list(extract_words(sent)) for test_word, sent in test_sents]

    for word, sents in test_sents:
        print "\nWord:\t%s\n" % (word)
        for i, sent in enumerate(sents):
            print "SENTENCE: #%s\n" % (i)
            print "\t\t" + repr(sent)

if __name__ == '__main__':
    token_test()




