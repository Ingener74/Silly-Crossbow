# encoding: utf8
from os import path
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext as _build_ext

import shutil


class MyBuildExt(_build_ext):
    def __init__(self, *args, **kwargs):
        _build_ext.__init__(self, *args, **kwargs)

    def run(self):
        source_dir = path.dirname(path.abspath(__file__))
        self.spawn(['cmake', source_dir])
        self.spawn(['cmake', '--build', source_dir, '--clean-first'])


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
      ext_modules=[Extension('SillyCrossbow', [])],
      packages=['SillyCrossbow'],
      cmdclass={
          'build_ext': MyBuildExt
      }
      )
