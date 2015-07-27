# encoding: utf8

from distutils.core import setup, Extension

import shutil

shutil.copyfile('README.md', 'README')

setup(name='Silly Crossbow',
      version='1.0',
      description="""
Simple SWIG + distutil example
example implements cropping transparent image borders
      """,
      long_description=open('README.md').read(),
      author='Shnaider Pavel',
      author_email='shnaiderpasha@gmail.com',
      url='https://github.com/Ingener74/Silly-Crossbow',
      ext_modules=[Extension("_SillyCrossbow", ["SillyCrossbow.i",
                                                "silly-crossbow.cpp"],
                             swig_opts=['-c++', '-outdir', 'SillyCrossbow'],
                             extra_compile_args=['-std=c++11'],
                             #extra_link_args=['-o', '_SillyCrossbow'],
                             define_macros=[('__NO_INLINE__', None)],
                             language='c++'
                             )
                   ],
      packages=['SillyCrossbow']
      )
