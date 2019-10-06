from requests import get
from lxml import etree
from functools import reduce
from pickle import load, dump
from os import path, makedirs


def to_mv(artifact):
    groupId, artifactId, version = artifact.split(':')
    return f'{groupId.replace(".", "/")}/{artifactId}/{version}/{artifactId}-{version}'


class Resolver:
    local: str
    remote: str
    cache: dict

    def __init__(self, local, remote):
        self.local = local
        self.remote = remote
        self.cache = {}

    def __enter__(self):
        if not path.exists(self.local):
            makedirs(self.local)
        if path.exists(f'{self.local}/resolver.cache'):
            with open(f'{self.local}/resolver.cache', 'rb') as data:
                self.cache = load(data)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if not path.exists(self.local):
                makedirs(self.local)
            with open(f'{self.local}/resolver.cache', 'wb') as data:
                dump(self.cache, data)

    def __call__(self, artifact):
        if artifact in self.cache:
            return self.cache[artifact]

        dependencies = reduce(lambda x, y: x | y, [
            self(dependency)
            for dependency in self.dependencies(artifact)
        ], {artifact})

        self.cache[artifact] = dependencies

        with open(f'{self.local}/{artifact}.jar', 'wb') as data:
            data.write(self.data(artifact))

        return dependencies

    def data(self, artifact):
        return get(f'{self.remote}/{to_mv(artifact)}.jar').content

    def metadata(self, artifact):
        return get(f'{self.remote}/{to_mv(artifact)}.pom').content

    def dependencies(self, artifact):
        ns = {"namespaces": {"n": "http://maven.apache.org/POM/4.0.0"}}
        tree = etree.fromstring(self.metadata(artifact))
        for sub in tree.xpath('''/n:project/n:dependencies/n:dependency[contains(n:scope/text(),'compile')]''', **ns):
            groupId = sub.xpath("n:groupId/text()", **ns)[0]
            artifactId = sub.xpath("n:artifactId/text()", **ns)[0]
            version = sub.xpath("n:version/text()", **ns)[0]
            yield f'{groupId}:{artifactId}:{version}'
