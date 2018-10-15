# -*- coding: utf-8 -*-
"""scons-tool-clang
"""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

setup(
        name='scons-tool-clang',
        version='0.2.7',
        package_dir={'sconstool.clang': '.'},
        packages=['sconstool.clang'],
        namespace_packages=['sconstool'],
        description='SCons tool for LLVM clang compiler',
        long_description=readme,
        long_description_content_type='text/x-rst',
        url='https://github.com/ptomulik/scons-tool-clang',
        author='Paweł Tomulik',
        author_email='ptomulik@meil.pw.edu.pl'
)

# vim: set expandtab tabstop=4 shiftwidth=4:
