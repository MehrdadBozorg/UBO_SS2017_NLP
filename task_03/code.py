import nltk, random


def make_doc_list():
    fp = open("training.txt")
    data = fp.read()
    list = data.splitlines()
    return list


def read_word_list(file_name):
    fp = open(file_name)
    data = fp.read()
    list = nltk.word_tokenize(data)
    return list


def baseline(sent_list):
    pos_file = "Positive.txt"
    neg_file = "Negative.txt"
    pos_words = read_word_list(pos_file)
    neg_words = read_word_list(neg_file)
    feature_list = []
    for sent in sent_list:
        print(sent)
        feature_sent = {}
        sent_len = len(sent.split())
        pos_sum = sum(1 for w in sent.lower().split() if w in pos_words)
        neg_sum = sum(1 for w in sent.lower().split() if w in neg_words)
        feature_sent["pos"] = pos_sum / sent_len
        feature_sent["neg"] = neg_sum / sent_len
        feature_list.append((feature_sent, int(sent[0])))
        print(feature_sent)
    return feature_list


if __name__ == "__main__":

    #########
    sent_list = make_doc_list()
    taged_sents = baseline(sent_list)

    #####Bayesian Training#####
    random.shuffle(taged_sents)
    size = int(len(taged_sents) * 0.1)
    train_set, test_set = taged_sents[size:], taged_sents[:size]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    out = nltk.classify.accuracy(classifier, test_set)
    print(out)
    target = open("output_baseline.txt", 'w')
    target.write(str(out))


