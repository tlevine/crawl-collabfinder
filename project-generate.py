#!/usr/bin/env python2



if __name__ == '__main__':
    import os
    import json

    descriptions = filter(None, [project['description'] for project in json.load(open(os.path.join('output', 'projects.json')))])
