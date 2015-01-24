# coding: utf-8

import os
import sure
from puppet.parser.doc import *
from puppet.parser.types import *


def test_parse_normal_section():
    state = {
        'name': 'test'
    }

    data = [
        {
            'ctx': {'state': state, 'sections': {}},
            'doc': '\nabc',
            'exp': 'abc'
        },
        {
            'ctx': {'state': state, 'sections': {}},
            'doc': 'abc\n123',
            'exp': 'abc\n123'
        }
    ]

    for d in data:
        parse_normal_section(d['doc'], d['ctx'])
        des = d['ctx']['sections']['test']
        des.should.equal(d['exp'])


def test_parse_options_section():
    data = [
        {
            'ctx': {'args': [], 'setters': {}, 'arg_map': {}, 'length': 0},
            'doc': '-n<int>, --num <int>, --number=<int>',
            'exp_names': set(['n', 'num', 'number']),
            'exp_type': int,
            'exp_desc': ''
        },
        {
            'ctx': {'args': [], 'setters': {}, 'arg_map': {}, 'length': 0},
            'doc': '-h, --help',
            'exp_names': set(['h', 'help']),
            'exp_type': mix,
            'exp_desc': ''
        },
        {
            'ctx': {'args': [], 'setters': {}, 'arg_map': {}, 'length': 0},
            'doc': '-h, --help  output usage information',
            'exp_names': set(['h', 'help']),
            'exp_type': mix,
            'exp_desc': 'output usage information'
        }
    ]

    for d in data:
        parse_options_section(d['doc'], d['ctx'])
        arg = d['ctx']['args'][0]
        arg['type'].should.equal(d['exp_type'])
        arg['names'].should.equal(d['exp_names'])
        arg['desc'].should.equal(d['exp_desc'])


def test_create_option_setter():
    args = [
        {
            'names': set(['n', 'num', 'number']),
            'type': int,
            'value': '123',
            'expect': 123
        },
        {
            'names': set(['h', 'help']),
            'type': mix,
            'value': None,
            'expect': True
        },
        {
            'names': set(['f', 'file']),
            'type': path,
            'value': 'tests',
            'expect': os.path.abspath('tests')
        },
        {
            'names': set(['j', 'json']),
            'type': json,
            'value': '{"hello": "world"}',
            'expect': {'hello': 'world'}
        }
    ]

    for arg in args:
        setter = create_option_setter(arg)
        flags = {}
        setter(flags, arg['value'])

        for name in arg['names']:
            flags[name].should.equal(arg['expect'])
