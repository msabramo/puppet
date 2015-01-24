# coding: utf-8

import re

SINGL_ARG_OPT_RE = re.compile('^-(?P<long>-)?(?P<name>(?(long)[^=]+|.))'
                              '=?(?P<value>.*?)$')
ARG_NAME_RE = re.compile('^-(?P<long>-)?(?P<name>(?(long).+|.))')


def parse(argv):
    state = {
        'index': 0,
        'name': None,
        'val': None,
        'argv': {},
        'args': []
    }

    count = len(argv)

    while state['index'] < count:
        arg = argv[state['index']]
        flush_boolean_option(state, arg)
        arg = argv[state['index']]
        parse_option(state, arg)

    flush_boolean_option(state, '--')

    return state['argv'], state['args']


def parse_option(state, arg):
    parse_single_arg_option(state, arg)\
        or parse_normal_option(state, arg)\
        or skip(state, arg)


def parse_single_arg_option(state, arg):
    if need_option_name(state) and is_option_name(arg):
        option = extract_single_arg_option(arg)

        if option and option[1]:
            state['name'], state['val'] = option
            flush(state)
            state['index'] += 1
            return True


def parse_normal_option(state, arg):
    return parse_option_name(state, arg)\
        or parse_option_value(state, arg)


def parse_option_name(state, arg):
    if need_option_name(state) and is_option_name(arg):
        state['name'] = extract_option_name(arg)
        state['index'] += 1
        return True


def parse_option_value(state, arg):
    if need_option_value(state) and not is_option_name(arg):
        state['val'] = arg
        flush(state)
        state['index'] += 1
        return True


def skip(state, arg):
    if not is_option_name(arg):
        state['args'].append(arg)
        state['index'] += 1


def flush_boolean_option(state, arg):
    if need_option_value(state) and is_option_name(arg):
        flush(state)


def flush(state):
    name = state['name']
    value = state['val']
    state['argv'][name] = value
    state['name'] = None
    state['val'] = None


def need_option_value(state):
    return not need_option_name(state)\
        and state['val'] is None


def need_option_name(state):
    return state['name'] is None


def is_option_name(arg):
    return len(arg) > 1 and arg[0] is '-'


def extract_single_arg_option(arg):
    match = SINGL_ARG_OPT_RE.match(arg)

    if not match:
        return None

    return (match.group('name'), match.group('value'))


def extract_option_name(arg):
    match = ARG_NAME_RE.match(arg)
    return match.group('name')
