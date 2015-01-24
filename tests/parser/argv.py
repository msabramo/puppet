# coding: utf-8

import sure
from puppet.parser.argv import *


def test_extract_option_name():
    data = [
        ('--long', 'long'),
        ('-s123', 's'),
        ('-s', 's')
    ]

    for d in data:
        name = extract_option_name(d[0])
        name.should.equal(d[1])


def test_parse_option_name():
    data = [
        {
            'state': {
                'index': 0,
                'name': None,
                'val': None
            },
            'arg': 'qq',
            'exp_ret': None,
            'exp_name': None
        },
        {
            'state': {
                'index': 0,
                'name': None,
                'val': None
            },
            'arg': '--abc',
            'exp_ret': True,
            'exp_name': 'abc'
        },
        {
            'state': {
                'index': 0,
                'name': '...',
                'val': None
            },
            'arg': '--qq',
            'exp_ret': None,
            'exp_name': '...'
        }
    ]

    for d in data:
        ret = parse_option_name(d['state'], d['arg'])
        ret.should.equal(d['exp_ret'])
        d['state']['name'].should.equal(d['exp_name'])


def test_parse_option_value():
    data = [
        {
            'state': {
                'name': None,
                'val': None,
                'argv': {},
                'args': [],
                'index': 0
            },
            'arg': 'abc',
            'exp_ret': None
        },
        {
            'state': {
                'name': 'gg',
                'val': None,
                'argv': {},
                'args': [],
                'index': 0
            },
            'arg': 'abc',
            'exp_ret': True
        },
        {
            'state': {
                'name': 'gg',
                'val': None,
                'argv': {},
                'args': [],
                'index': 0
            },
            'arg': '-abc',
            'exp_ret': None
        },
        {
            'state': {
                'name': 'gg',
                'val': None,
                'argv': {},
                'args': [],
                'index': 0
            },
            'arg': '--abc',
            'exp_ret': None
        }
    ]

    for d in data:
        ret = parse_option_value(d['state'], d['arg'])
        ret.should.equal(d['exp_ret'])
