#!/usr/bin/env python2
from lxml.html import parse

def backgrounds(html):
    'This project needs...'
    b = {
        'Developers': False,
        'Designers': False,
        'Artists': False,
        'Writers': False,
        'Scientists': False,
    }
    text_nodes = set(map(unicode, html.xpath('id("seeking")/descendant::b/text()')))
    for k in b.keys():
        if k in text_nodes:
            b[k] = True
    return b


def answers(html):
    return backgrounds(html)


if __name__ == '__main__':
    print answers(parse('downloads/2013-04-13 15:10:54-04:00/23.html'))
    #main()
