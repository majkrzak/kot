from json import load
from sys import argv
from .resolver import Resolver
from .idefix import Idefix

REMOTE = 'https://jcenter.bintray.com/'
LOCAL = '.lib/'

with open(argv[1]) as f:
    structure = load(f)

with Resolver(LOCAL, REMOTE) as resolver:
    Idefix(
        structure['name'],
        {
            artifact: resolver(artifact)
            for artifact in structure['dependencies']
        },
        structure['modules']
    )()
