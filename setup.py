#! /usr/bin/env python
# -*- coding: iso-8859-15 -*-
from distutils.core import *
from distutils      import sysconfig
import numpy as np
import os
import sys


extra_compile_args = ['-std=c++14', '-D_GLIBCXX_USE_CXX11_ABI=0', '-Wno-deprecated-declarations', '-Wno-unused-local-typedefs']
include_dirs=set()
library_dirs=[ '.']
include_dirs.add(sysconfig.get_python_inc())
include_dirs.add(np.get_include())
include_dirs.add('boost_numpy')
library_dirs += ['boost_numpy/lib']
libraries = set(['boost_python', 'boost_numpy'])
include_dirs = list(include_dirs)
libraries = list(libraries)

test = Extension("pkg.test",
    ["pkg/test.cpp"],
    libraries=libraries,
    include_dirs = include_dirs,
    language='c++',
    library_dirs=library_dirs,
    extra_compile_args = extra_compile_args + ["-fPIC"],
    extra_link_args = []
)

# NumyTypemapTests setup
setup(  name        = 'pkg',
    description = "Boost numpy array test",
    author      = "taylan.toygarlar@imc.nl",
    version     = "0",
    license     = "2",
    long_description = "Check type compatibility",
    options     = {'build_ext':{'swig_opts':'-c++ -I' +" -I".join(include_dirs)}},
    ext_modules = [test],
    packages=['pkg'], 
    package_dir = {'pkg': 'pkg'},
)

