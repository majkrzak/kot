class Builder:
    build: str

    def __init__(self, build):
        self.build = build

    def __call__(self, module):
        print(f'kotlin {module}')
