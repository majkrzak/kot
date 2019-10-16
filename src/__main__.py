from functools import reduce
from json import load

from src import args
from .resolver import Resolver

from .idefix import Idefix
from .resolver import Resolver

REMOTE = 'https://jcenter.bintray.com/'
LOCAL = '.lib/'


with open(args.structure) as f:
    structure = load(f)

name = structure['name']
dependencies = structure['dependencies']
modules = structure['modules']

with Resolver(LOCAL, REMOTE) as resolver:
    libs = {artifact: resolver(artifact) for artifact in filter(lambda x: not x.startswith(':'),
                   reduce(lambda x, y: set(x) | set(y), structure['modules'].values(), set()))}
    Idefix(name, libs, modules)()
