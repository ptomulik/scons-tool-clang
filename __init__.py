# -*- coding: utf-8 -*-
"""sconstool.clang

Tool-specific initialization for clang.

There normally shouldn't be any need to import this module directly.
It will usually be imported through the generic SCons.Tool.Tool()
selection method.

"""

#
# Copyright (c) 2014-2020 by Paweł Tomulik
# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013 The SCons Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# Based on SCons/Tool/gcc.py

import os
import re
import subprocess
import sys

import SCons.Util
import SCons.Tool.cc

try:
    from SCons.Tool.clangCommon import get_clang_install_dirs
    has_clangCommon = True
except ImportError:
    has_clangCommon = False


compilers = ['clang']

def generate(env):
    """Add Builders and construction variables for clang to an Environment."""
    SCons.Tool.cc.generate(env)

    if has_clangCommon and env['PLATFORM'] == 'win32':
        # Ensure that we have a proper path for clang
        clang = SCons.Tool.find_program_path(env, compilers[0],
                                             default_paths=get_clang_install_dirs(env['PLATFORM']))
        if clang:
            clang_bin_dir = os.path.dirname(clang)
            env.AppendENVPath('PATH', clang_bin_dir)

    env['CC'] = env.Detect(compilers) or 'clang'
    if env['PLATFORM'] in ['cygwin', 'win32']:
        env['SHCCFLAGS'] = SCons.Util.CLVar('$CCFLAGS')
    else:
        env['SHCCFLAGS'] = SCons.Util.CLVar('$CCFLAGS -fPIC')

    # determine compiler version
    if env['CC']:
        pipe = SCons.Action._subproc(env, [env['CC'], '--version'],
                                     stdin='devnull',
                                     stderr='devnull',
                                     stdout=subprocess.PIPE)
        if pipe.wait() != 0: return
        # clang -dumpversion is of no use
        line = pipe.stdout.readline()
        if sys.version_info[0] > 2:
            line = line.decode()
        match = re.search(r'clang +version +([0-9]+(?:\.[0-9]+)+)', line)
        if match:
            env['CCVERSION'] = match.group(1)

def exists(env):
    return env.Detect(compilers)

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
