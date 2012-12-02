from distutils.core import setup
from distutils.extension import Extension
setup(
    name = 'example2',
    ext_modules = [Extension("example2p", ["example2p.c"])])
