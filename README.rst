scons-tool-clang
==================

SCons_ support for LLVM_ clang_ C compiler.

Usage example
-------------

Git-based projects
^^^^^^^^^^^^^^^^^^

#. Create new git repository::

      mkdir /tmp/prj && cd /tmp/prj
      touch README.rst
      git init

#. Add the `scon-tool-clang`_ as a submodule::

      git submodule add git://github.com/ptomulik/scons-tool-clang.git site_scons/site_tools/clang

#. Create simple C file

   .. code-block:: cpp

      // test.c
      int main()
      {
        return 0;
      }

#. Create simple SConstruct file

   .. code-block:: python

      # SConstruct
      env = Environment(tools = ['default', 'clang'])
      print env.subst("using $CC $CCVERSION")
      env.Program('test.c')

#. Try it out::

      scons

LICENSE
-------

Copyright (c) 2014 by Pawel Tomulik <ptomulik@meil.pw.edu.pl>

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

.. _LLGM: http://clang.llvm.org/
.. _scons-tool-clang: https://github.com/ptomulik/scons-tool-clang
.. _clang: http://llvm.org/
.. _SCons: http://scons.org

.. <!--- vim: set expandtab tabstop=2 shiftwidth=2 syntax=rst: -->
