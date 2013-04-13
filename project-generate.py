#!/usr/bin/env python2
from random import normalvariate

from numpy import array

from nltk.tokenize import wordpunct_tokenize #, word_tokenize, sent_tokenize
from nltk.probability import LidstoneProbDist #LaplaceProbDist
from nltk import NgramModel

MINIMUM_DESCRIPTION_LENGTH = 120
def description_length_func(subdescriptions):
    'Create a function that chooses the length of a description.'
    a = array([len(d) for d in subdescriptions])
    mean = a.mean()
    std = a.std()
    def description_length():
        l = normalvariate(mean, std)
        return int(max(MINIMUM_DESCRIPTION_LENGTH, l))
    return description_length

def train_subdescription(subdescriptions):
    '''
    :param subdescriptions: a list of training texts
    :type subdescriptions: list(list(str))
    '''
    train = [wordpunct_tokenize(d) for d in subdescriptions]
    lm = NgramModel(3, train, estimator = (lambda fdist, bins: LidstoneProbDist(fdist, 0.2)))

    length = description_length_func(subdescriptions)

    return lm, length

if __name__ == '__main__':
    import os
    import json

    descriptions = filter(None, [project['description'] for project in json.load(open(os.path.join('output', 'projects.json')))])
    print descriptions[0]
    for key in ['what', 'why', 'need']:
        subdescriptions = [d[key] for d in descriptions]
        lm, length = train_subdescription(subdescriptions)
