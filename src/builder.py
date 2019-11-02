from subprocess import run


class Builder:
    dir: str

    def __init__(self, dir):
        self.dir = dir

    def __call__(self, modules):
        run(f'''kotlinc {' '.join(modules)} -cp $(find .lib -name "*.jar" |  xargs | sed 's/ /:/g') -d {self.dir}/''',
            shell=True,
            check=True
            )
