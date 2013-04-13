#!/usr/bin/env python2
import re
from string import ascii_letters

from random import normalvariate

from numpy import array

from nltk.tokenize import wordpunct_tokenize #, word_tokenize, sent_tokenize
from nltk.probability import LidstoneProbDist #LaplaceProbDist
from nltk import NgramModel

def detokenize(tokens):
    text = ''
    for token in tokens:
        if token[0] in (ascii_letters + '(['):
            # Add a space
            text += ' '
        elif token[0] in '([':
            # Remove a space
            text = text[:-1]

        text += token
    return re.sub(r'\.[^.]*$', '.', text[1:])

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
    generators={}
    for key in ['what', 'why', 'need']:
        subdescriptions = [d[key] for d in descriptions]
        lm, length = train_subdescription(subdescriptions)
        generators[key] = lambda about: detokenize(lm.generate(length(), wordpunct_tokenize(about)))
