# encoding: utf8
from os import path
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.command.install_lib import install_lib
import shutil

source_dir = path.dirname(path.abspath(__file__))
build_dir = source_dir + '/SillyCrossbow'
output_dir = build_dir + '/SillyCrossbow'


class Building(build_ext):
    def __init__(self, *args, **kwargs):
        build_ext.__init__(self, *args, **kwargs)

    def run(self):
        self.spawn(['cmake',
                    source_dir,
                    '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + output_dir,
                    '-DCMAKE_RUNTIME_OUTPUT_DIRECTORY=' + output_dir,
                    '-DCMAKE_SWIG_OUTDIR=' + output_dir,
                    ])
        self.spawn(['cmake', '--build', source_dir, '--clean-first'])


class Installation(install_lib):
    def __init__(self, *args, **kwargs):
        install_lib.__init__(self, *args, **kwargs)
        self.build_dir = build_dir


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
          'build_ext': Building
          , 'install_lib': Installation
      }
      )
