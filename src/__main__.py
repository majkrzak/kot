from functools import reduce
from json import load
from sys import argv

from .builder import Builder
from .idefix import Idefix
from .resolver import Resolver

REMOTE = 'https://jcenter.bintray.com/'
LOCAL = '.lib/'
BUILD = '.out/'

with open(argv[1]) as f:
    structure = load(f)

if len(argv) < 3:
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
elif argv[2] == 'build':
    builder = Builder(BUILD)
    builder(structure['modules'].keys())

