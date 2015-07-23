# encoding: utf8

from distutils.core import setup, Extension

setup(name='Silly Crossbow',
      version='1.0',
      description="""
      Simple SWIG + distutil example
      example implements cropping transparent image borders
      """,
      author='Shnaider Pavel',
      author_email='shnaiderpasha@gmail.com',
      url='https://github.com/Ingener74/Silly-Crossbow',
      ext_modules=[
          Extension(
              "_SillyCrossbow",
              ["SillyCrossbow.i", "silly-crossbow.cpp"],
              swig_opts=['-c++'])
      ]
      )
