# coding: utf-8

import os
import sure
from puppet.parser.types import *


def test_json():
    data = [
        ('null', None),
        ('123', 123),
        ('"abc"', 'abc'),
        ('["a", "b", "c"]', ['a', 'b', 'c']),
        ('{"a": "b", "c": "d"}', {'a': 'b', 'c': 'd'})
    ]

    for d in data:
        json(d[0]).should.equal(d[1])


def test_path():
    data = [
        ('/tmp', '/tmp'),
        ('test', os.path.abspath('test')),
        ('./test', os.path.abspath('test'))
    ]

    for d in data:
        path(d[0]).should.equal(d[1])


def test_mix():
    data = [
        (None, True),
        ('123', 123),
        ('abc', 'abc'),
        ('/tmp', '/tmp'),
        ('./test', os.path.abspath('test')),
        ('"abc"', 'abc'),
        ('["a"]', ['a']),
        ('{"b": "c"}', {'b': 'c'})
    ]

    for d in data:
        mix(d[0]).should.equal(d[1])
