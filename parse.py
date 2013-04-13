#!/usr/bin/env python2
from lxml.html import parse

def _backgrounds(html):
    'This project needs...'
    return set(map(unicode, html.xpath('id("seeking")/descendant::b/text()')))

def _description(html):
    '''
    What are you making?
    Why are you making it?
    What do you need help with?
    '''
    questions =['what', 'why', 'need']
    answers = filter(None, map(unicode, html.xpath('//div[@class="column span-18 append-1 border_t_g first last"]/h2[@class="plain"]/text()')))
    return zip(questions, answers)

def _goals(html):
    'Project Goals'
    return map(unicode, html.xpath('id("project_goals")/li/text()'))

def _tags(html):
    'Tags'
    return map(unicode, html.xpath('//ul[@class="bottomend-1 attributes tags"]/li/a/text()'))

def _github(html):
    'Project Github'
    results = html.xpath('//h2[@class="toppend-1 border_t_g"]/a/text()')
    if len(results) == 1:
        return unicode(url)

def answers(html):
    return {
        'backgrounds': _backgrounds(html),
        'description': _description(html),
        'goals': _goals(html),
        'tags': _tags(html),
        'github': _github(html),
    }


if __name__ == '__main__':
    print answers(parse('downloads/2013-04-13 15:10:54-04:00/23.html'))
    #main()
