# encoding: utf8

from distutils.core import setup, Extension

setup(name="Simple SWIG + distutil example",
      version="1.0",
      ext_modules=[Extension("_SillyCrossbow", ["SillyCrossbow.i", "silly-crossbow.cpp"])],
      options={
          'build_ext': {
              'swig_opts': '-c++'
          }
      }
      )
