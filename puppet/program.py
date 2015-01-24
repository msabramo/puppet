# coding: utf-8

import os
import sys
from . import handlers, util
from .flags import Flags
from subprocess import call


main = sys.modules['__main__']
main_module_location = os.path.dirname(main.__file__)
main_module_location = os.path.abspath(main_module_location)


class Program:
    def __init__(self, name=sys.argv[0],
                 version='0.1.0',
                 doc=main.__doc__,
                 argv=sys.argv[1:],
                 subcmd=False):

        self.origin_argv = argv
        self.name = name if name else sys.argv[0]
        self.version = version
        self.subcmd = subcmd
        self.flags = Flags(argv, doc)

    @property
    def doc(self):
        return self.flags.doc

    @property
    def argv(self):
        return self.flags.argv

    @property
    def args(self):
        return self.flags.args

    @property
    def usage(self):
        return self.doc['usage']

    def start(self):
        if self.subcmd:
            self.run_subcmd()

        self.run_handlers()
        main_function = getattr(main, 'main', None)
        if main_function:
            main_function(self)

    def run_subcmd(self, index=0):
        bin_file = self.subcmd_bin_file(index)

        if bin_file is None:
            return

        args = [bin_file] + self.origin_argv
        code = call(args, stdin=sys.stdin,
                    stdout=sys.stdout, stderr=sys.stderr)

        sys.exit(code)

    def subcmd_bin_file(self, index=0):
        name = self.subcmd_name(index)
        if name:
            name = '%s-%s' % (self.name, name)
            paths = os.environ['PATH'].split(os.pathsep)
            paths.insert(0, main_module_location)
            return util.which(name, paths)

    def subcmd_name(self, index=0):
        if len(self.args) > 0:
            return self.args[0]

    def run_handlers(self):
        called = {}

        for name in self.flags.argv:
            arg = self.get_arg(name)
            if not arg or arg['id'] in called:
                continue

            called[arg['id']] = 1
            handler = self.get_handler(arg)
            if handler:
                handler(self, self.flags[name])

    def get_arg(self, name):
        return self.flags.doc['arg_map'].get(name, None)

    def get_handler(self, arg):
        for name in arg['names']:
            if hasattr(main, name):
                return getattr(main, name)
            if hasattr(handlers, name):
                return getattr(handlers, name)
