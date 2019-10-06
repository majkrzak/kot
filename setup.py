import setuptools

setuptools.setup(
    name='kot',
    author='Piotr Majrzak',
    author_email='piotr@majkrzak.dev',
    license='MIT',
    data_files = [("", ["LICENSE"])],
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
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
