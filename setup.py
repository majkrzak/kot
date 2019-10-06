import setuptools

setuptools.setup(
    name='kot',
    author='Piotr Majrzak',
    author_email='piotr@majkrzak.dev',
    license='Permission to use, copy, modify, and distribute this software for any '
            + 'purpose with or without fee is hereby granted, provided that the above '
            + 'copyright notice and this permission notice appear in all copies.',
    packages=[
        'kot',
    ],
    package_dir={'kot': './src'},
    install_requires=[
        'requests',
        'lxml'
    ],
    setup_requires=[
        'wheel'
    ]
)
