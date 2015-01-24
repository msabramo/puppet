# coding: utf-8

import os
import sys


def which(bin_file, paths=[]):
    base, ext = os.path.splitext(bin_file)

    if (sys.platform == 'win32' or os.name == 'os2') and (ext != '.exe'):
        bin_file = bin_file + '.exe'

    if not os.path.isfile(bin_file):
        for path in paths:
            file_path = os.path.join(path, bin_file)
            if os.path.isfile(file_path):
                return file_path
        bin_file = None

    return bin_file
