from nltk.corpus import stopwords
import collections, re, nltk
from nltk.corpus import wordnet as wn


##############
# Remove stopwords using nltk stopwords
def stopword_nltk(sent):
    stops = set(stopwords.words('english'))
    print(sent)
    for w in sent.split():
        if w.lower() not in stops:
            print(w, '\n' + 'done by nltk')

##############

# My own stopwords function
###############
def stopword_myown(sent):
    stopwords_list = ['am', 'are', 'i', 'you']
    line = sent
    for w in stopwords_list:
        pattern = r'\b' + w + r'\b'
        line = re.sub(pattern, '', line)
    print('your sentence is: ', sent, '\n' + 'after removing stopwords: ', line)

###############

# Bag of words function #####
def word_bag(texts):
    bagsofwords = [collections.Counter(re.findall(r'\w+', txt))
                   for txt in texts]
    sumbags = sum(bagsofwords, collections.Counter())
    histo_list = []
    histogram = {}
    for item in bagsofwords:
        for key in sumbags:
            if key in item:
                histogram[key] = item[key]
            else:
                histogram[key] = 0
        histo_list.append(histogram)
        print(histogram.values())
    print(sumbags)


# Function to define the sense of word
def wordnet_sense(your_word):
    print(wn.synsets(your_word))


if __name__ == "__main__":

    # Test stopwords function.
    sentence = input('write a sentence: ')
    try:
        sent = str(sentence)
        stopword_nltk(sent)
        stopword_myown(sent)
    except ValueError:
        print("Invalid word")
    ########

    # Test BoW
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open("myText.txt")
    data = fp.read()
    texts = tokenizer.tokenize(data)
    word_bag(texts)
    #########

    # Test sense of word
    word = input('write a word: ')
    try:
        w = str(word)
        wordnet_sense(w)
    except ValueError:
        print("Invalid word")


