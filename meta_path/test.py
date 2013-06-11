#!/usr/bin/env python

from __future__ import absolute_import, print_function, division

import imp
import sys
import os

class MultipleImporter(object):
    def __init__(self, package_name):
        """Remember of which package we want to customize the importing.
        """
        self.package_name = package_name

    def find_module(self, fullname, path=None):
        """Find the loader (i.e., self).
        """
        if fullname.split('.')[0] != self.package_name:
            return None
        fobj, filepath, desc = self._find_module(fullname, path)
        print(fullname, path, fobj, filepath, desc)
        mod = imp.load_module(fullname, fobj, filepath, desc)
        if fobj:
            fobj.close()
        return self

    @staticmethod
    def _find_module(fullname, path):
        """Find module in all sys.path if the normal try fails.
        """
        tokens = fullname.split('.')
        try:
            fobj, filepath, desc = imp.find_module(tokens[-1], path)
        except ImportError as e:
            path = [os.path.join(it, *tokens[:-1]) for it in sys.path]
            fobj, filepath, desc = imp.find_module(tokens[-1], path)
        return fobj, filepath, desc

    def load_module(self, fullname):
        """Just return the module loaded in :py:meth:`find_module`.
        """
        if fullname in sys.modules:
            return sys.modules[fullname]
        else:
            return None

sys.path.extend(['dir1', 'dir2'])
sys.meta_path.append(MultipleImporter('pkg'))

import amod
import pkg.mod1
print(pkg.mod1)
pkg.mod1.func1()
import pkg.mod2
print(pkg.mod2)
pkg.mod2.func2()
from somepak import bmod
print(bmod)
bmod.funcb()
