import re
from setuptools import setup

with open('puppet/__init__.py') as f:
    m = re.findall(r"__version__\s*=\s*'(.*)'", f.read())
    version = m[0]

setup(
    name='puppet',
    version=version,
    url='https://github.com/poying/puppet',
    license='MIT',
    author='Po-Ying Chen',
    author_email='poying.me@gmail.com',
    packages=[
        'puppet',
        'puppet.parser',
    ],
    platforms='any',
    install_requires=[
        'requests>=2.5.1',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Traditional)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
