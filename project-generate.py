#!/usr/bin/env python2
from nltk.tokenize import wordpunct_tokenize #, word_tokenize, sent_tokenize
from nltk.probability import LidstoneProbDist #LaplaceProbDist
from nltk import NgramModel


def train(descriptions):
    '''
    :param descriptions: a list of training texts
    :type descriptions: list(list(str))
    '''
    train = wordpunct_tokenize(descriptions)
    lm = NgramModel(3, train, estimator = (lambda fdist, bins: LidstoneProbDist(fdist, 0.2)))
    return lm

def main(descriptions):
    for subdescription in ['what', 'why', 'need']:
        lm = train((d[subescription] for d in descriptions))

if __name__ == '__main__':
    import os
    import json

    descriptions = filter(None, (project['description'] for project in json.load(open(os.path.join('output', 'projects.json')))))
    main(descriptions)
