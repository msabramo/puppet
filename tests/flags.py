# coding: utf-8

import sure
from puppet.flags import *


def test_flags_init():
    data = [
        {
            'argv': ['--boolean', '-sabc', '--number', '123', '--hello=world'],
            'doc': '''
            Options:
                -b, --boolean
                -s<str>
                --number <num>
                --hello=<str>
            ''',
            'exp_opts': [
                ('boolean', True),
                ('b', True),
                ('s', 'abc'),
                ('number', 123),
                ('hello', 'world')
            ],
            'exp_secs': []
        },
        {
            'argv': ['-h'],
            'doc':'''
            haeder

            Usage:
                abc 123\nggg hhh

            Options:
                -h, --help
            ''',
            'exp_opts': [
                ('h', True),
                ('help', True)
            ],
            'exp_secs': [
                ('usage', 'abc 123\nggg hhh')
            ]
        }
    ]

    for d in data:
        flags = Flags(d['argv'], d['doc'])

        for name, value in d['exp_opts']:
            flags[name].should.equal(value)

        for name, value in d['exp_secs']:
            actual = flags.doc['sections'][name]
            actual.should.equal(value)
