from functools import reduce
from json import load
from sys import argv

from .idefix import Idefix
from .resolver import Resolver

REMOTE = 'https://jcenter.bintray.com/'
LOCAL = '.lib/'

with open(argv[1]) as f:
    structure = load(f)

with Resolver(LOCAL, REMOTE) as resolver:
    Idefix(
        structure['name'],
        {
            artifact: resolver(artifact)
            for artifact in
            filter(lambda x: not x.startswith(':'),
                   reduce(lambda x, y: set(x) | set(y), structure['modules'].values(), set()))
        },
        structure['modules']
    )()
