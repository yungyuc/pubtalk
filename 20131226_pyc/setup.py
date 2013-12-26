from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [Extension("example2s", ["example2b.pyx"])]
setup(
    name = 'example2',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules)
