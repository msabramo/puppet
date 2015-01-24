# coding: utf-8

from .parser import parse_doc, parse_argv


class Flags:
    def __init__(self, argv=[], doc=''):
        argv, args = parse_argv(argv)
        self.argv = argv
        self.args = args
        self.doc = parse_doc(doc)
        self.build_alias()

    def build_alias(self):
        setters = self.doc['setters']
        for name, value in list(self.argv.items()):
            setter = setters.get(name, None)
            setter and setter(self.argv, value)

    def __getattr__(self, name):
        return self.get(name)

    def __getitem__(self, name):
        return self.get(name)

    def get(self, name):
        return self.argv.get(name, None)
