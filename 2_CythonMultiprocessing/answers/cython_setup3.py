#!/usr/bin/env python3

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
  
ext_modules=[
	Extension("cython_dot3",
		["cython_dot3.pyx"],
		libraries=["m"],
		extra_compile_args = ["-O3", "-ffast-math", "-march=native","-fopenmp"],	
		#extra_link_args=['-fopenmp']
       )
]


setup(
	name = "cython_dot3",
	cmdclass = {"build_ext": build_ext},
 	ext_modules = ext_modules,
	include_dirs = [np.get_include()]
	)
