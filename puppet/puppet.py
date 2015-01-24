# coding: utf-8

import atexit
from .program import Program
from threading import Thread, current_thread


def puppet(*args, **kargs):
    program = Program(*args, **kargs)
    t = Thread(target=start(program))
    t.daemon = True
    t.start()
    atexit.register(end, t)


def start(program):
    t = current_thread()

    def start():
        t.join()
        program.start()

    return start


def end(t):
    t.join()
