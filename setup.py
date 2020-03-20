import setuptools

with open('README', 'r') as readme:
    long_desc = readme.read()

setuptools.setup(
    name='jukebox',
    version='0.0.1',
    description='A math project to perform analysis on three sequences, named J, K, and B respectively.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='junk.io',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
