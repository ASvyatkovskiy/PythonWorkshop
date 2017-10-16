#!/usr/bin/env python3

from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'my dot',
  ext_modules = cythonize("cython_dot.pyx")
)
