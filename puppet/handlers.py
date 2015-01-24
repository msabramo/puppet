# coding: utf-8

import sys


def help(program, value):
    print(program.usage)
    sys.exit()


def version(program, value):
    print(program.version)
    sys.exit()
