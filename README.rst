scons-tool-clang
==================

.. image:: https://badge.fury.io/py/scons-tool-clang.svg
    :target: https://badge.fury.io/py/scons-tool-clang
    :alt: PyPi package version

.. image:: https://travis-ci.org/ptomulik/scons-tool-clang.svg?branch=master
    :target: https://travis-ci.org/ptomulik/scons-tool-clang
    :alt: Travis CI build status

SCons_ support for LLVM_ clang_ C compiler.

Important note
--------------

SCons currently provides ``clang`` tool which replaces this one. See SCons user
documentation, especially the `tool list`_. This package is left here for
historical reasons and for some experimental purposes.

Installation
------------

There are few ways to install this tool to your project.

From pypi_
^^^^^^^^^^

.. code-block:: shell

      pip install scons-tool-loader scons-tool-clang

or, if your project uses pipenv_:

.. code-block:: shell

      pipenv install --dev scons-tool-loader scons-tool-clang

Alternativelly, you may add this to your ``Pipfile``

.. code-block::

    [dev-packages]
    scons-tool-loader = "*"
    scons-tool-clang = "*"


The tool will be installed as a namespaced package ``sconstool.clang``
in project's virtual environment. You may further use scons-tool-loader_
to load the tool.

As a git submodule
^^^^^^^^^^^^^^^^^^

#. Create new git repository:

   .. code-block:: shell

      mkdir /tmp/prj && cd /tmp/prj
      touch README.rst
      git init

#. Add the `scons-tool-clang`_ as a submodule:

   .. code-block:: shell

      git submodule add git://github.com/ptomulik/scons-tool-clang.git site_scons/site_tools/clang

Usage example
-------------

#. Create simple C file

   .. code-block:: c

      // test.c
      int main()
      {
        return 0;
      }

#. Create simple SConstruct file

   .. code-block:: python

      # SConstruct
      # TODO: uncomment following lines if the tool is installed via pip/pipenv
      # import sconstool.loader
      # sconstool.loader.extend_toolpath(transparent=True)
      env = Environment(tools = ['default', 'clang'])
      print(env.subst("using $CC $CCVERSION"))
      env.Program('test.c')

#. Try it out:

   .. code-block:: shell

      scons

LICENSE
-------

Copyright (c) 2014-2018 by Pawel Tomulik <ptomulik@meil.pw.edu.pl>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

.. _LLVM: http://llvm.org/
.. _clang: http://clang.llvm.org/
.. _scons-tool-clang: https://github.com/ptomulik/scons-tool-clang
.. _scons-tool-loader: https://github.com/ptomulik/scons-tool-loader
.. _SCons: http://scons.org
.. _pipenv: https://pipenv.readthedocs.io/
.. _pypi: https://pypi.org/
.. _tool list: https://scons.org/doc/HTML/scons-user.html#app-tools

.. <!--- vim: set expandtab tabstop=2 shiftwidth=2 syntax=rst: -->
