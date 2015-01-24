# coding: utf-8

import re
from .types import json, path, mix

# Usage: ...
NEW_SECTION_RE = re.compile('^\s*([^\[\]:]+):')

# Optinos: ...
OPTS_SETION_RE = re.compile('options', re.I)

# --name=<type>
# --name <type>
# -n=<type>
# -n <type>
# -n<type>
ARG_RE = re.compile('(?:'
                    '-(?P<long>-)?(?P<name>(?(long)[^\s=,]+|.))'
                    '(?:[\s=]?(?:<(?P<type>[^\s\.]+)>))?)')

# -n=<type>, --name=<type>    description
ARG_DESC_RE = re.compile('^'
                         '(?P<args>'                            # arg start
                         '(?:\s*'                               # indent
                         '(?:-(?P<long>-)?(?(long)[^\s=,]+|.)'  # name
                         '(?:[\s=]?(?:<[^\s\.]+>))?)'           # type
                         '(?:,|\s+|$)'                          # separator
                         ')+'                                   # arg end
                         ')'                                    # args end
                         '(?P<desc>'                            # desc start
                         '.*?'                                   # desc
                         '(?:\[default:\s*(?P<def>.*?)\])?'     # default value
                         ')'                                    # desc end
                         '$')


types = {
    'n': int, 'num': int, 'number': int,
    'i': int, 'int': int, 'integer': int,
    's': str, 'str': str, 'string': str,
    'f': float, 'float': float,
    'j': json, 'json': json,
    'path': path, 'file': path,
    'dir': path, 'directory': path, 'folder': path,
    'mix': mix, None: mix
}


def parse(doc):
    context = {
        'usage': doc,
        'sections': {},
        'setters': {},
        'arg_map': {},
        'args': [],
        'length': 0,
        'state': {
            'name': 'header',
            'is_options': False
        }
    }

    lines = doc.strip().splitlines()

    for line in lines:
        update_state(line, context)\
            or parse_line(line, context)

    return context


def update_state(line, context):
    match = NEW_SECTION_RE.match(line)

    if match:
        name = match.group(1).lower()

        state = {
            'name': name,
            'is_options': name == 'options'
        }

        context['state'] = state

        if not OPTS_SETION_RE.match(line):
            parse_normal_section(NEW_SECTION_RE.sub('', line), context)

    return match


def parse_line(line, context):
    state = context['state']

    if state['is_options']:
        parse_options_section(line, context)
    else:
        parse_normal_section(line, context)


def parse_normal_section(content, context):
    state = context.get('state', {})
    section = context['sections'].get(state['name'], '')
    section = section + '\n' + content
    context['sections'][state['name']] = section.strip()


def parse_options_section(content, context):
    match = ARG_DESC_RE.match(content)

    if not match:
        return

    context['length'] += 1

    arg = {
        'id': context['length'],
        'names': set(),
        'type': mix,
        'desc': match.group('desc'),
        'default': match.group('def')
    }

    for arg_match in ARG_RE.finditer(match.group('args')):
        name, type_name = arg_match.group('name', 'type')
        arg['type'] = types[type_name]
        arg['names'].add(name)
        context['arg_map'][name] = arg

    setter = create_option_setter(arg)
    context['args'].append(arg)

    for name in arg['names']:
        context['setters'][name] = setter


def create_option_setter(arg):
    def setter(flags, value):
        for name in arg['names']:
            flags[name] = arg['type'](value)
    return setter
