from json import load
from sys import argv
from .resolver import Resolver

REMOTE = 'https://jcenter.bintray.com/'
LOCAL = '.lib/'

with open(argv[1]) as f:
    structure = load(f)

with Resolver(LOCAL, REMOTE) as resolver:
    dependencies = {
        artifact: resolver(artifact)
        for artifact in structure['dependencies']
    }

print(structure)
print(dependencies)
