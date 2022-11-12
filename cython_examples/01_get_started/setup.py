from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules = cythonize(Extension(
           "vecint", # module name
           sources=["vecint.pyx", "vector_int.cpp"],
           language="c++",
           language_level = "3",)))