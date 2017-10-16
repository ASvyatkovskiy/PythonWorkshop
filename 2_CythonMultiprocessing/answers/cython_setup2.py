#!/usr/bin/env python3

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
  
ext_modules=[
	Extension("cython_dot2",
		["cython_dot2.pyx"],
		libraries=["m"],
		extra_compile_args = ["-O3", "-ffast-math", "-march=native"],
		#extra_link_args=['-fopenmp']
       )
]


setup(
	name = "cython_dot2",
	cmdclass = {"build_ext": build_ext},
 	ext_modules = ext_modules,
	include_dirs = [np.get_include()]
	)
