# coding: utf-8

import os
import re
from json import loads as json_loads

FLOAT_RE = re.compile('^(?P<int>\d+)?\.(?(int)(?:\d+)?|\d+)$')
REL_PATH_RE = re.compile('^\.\.?' + os.sep)
JSON_RE = re.compile('^[{\[\'"n]')


def json(value):
    return json_loads(value)


def path(value):
    if os.path.isabs(value):
        return value
    return os.path.abspath(value)


def mix(value):
    if value is None:
        return True

    if not isinstance(value, str):
        return value

    if value.isdigit():
        return int(value)

    if FLOAT_RE.match(value):
        return float(value)

    if os.path.isabs(value):
        return value

    if REL_PATH_RE.match(value):
        return path(value)

    if JSON_RE.match(value):
        try:
            return json(value)
        except:
            pass

    return value
