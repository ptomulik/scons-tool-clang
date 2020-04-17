#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2020 by Paweł Tomulik <ptomulik@meil.pw.edu.pl>
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

import TestSCons
import json

_exe = TestSCons._exe
test = TestSCons.TestSCons()

if not test.where_is('clang'):
    test.skip_test("Could not find 'clang', skipping test.\n")

test.file_fixture('../../../__init__.py', 'site_scons/site_tools/clang/__init__.py')


test.write('SConstruct', """\
import SCons.Environment
import json
env = SCons.Environment.Base()
platform = env['PLATFORM']
if platform == 'posix':
    filename_options = ['foo.os']
    libraryname = 'libfoo.so'
elif platform == 'darwin':
    filename_options = ['foo.os']
    libraryname = 'libfoo.dylib'
elif platform == 'win32':
    filename_options = ['foo.obj','foo.os']
    libraryname = 'foo.dll'
else:
    test.fail_test()

info = {'filename_options': filename_options, 'libraryname': libraryname}

with open('info.json', 'wt') as f:
    f.write(json.dumps(info))
""")

test.run()
test.must_exist(test.workpath('info.json'))

with open(test.workpath('info.json')) as f:
    info = json.loads(f.read())

test.write('SConstruct', """\
DefaultEnvironment(tools=[])
env = Environment(tools=['clang', 'link'])
env.SharedLibrary('foo', 'foo.c')
""")

test.write('foo.c', """\
int bar() {
    return 42;
}
""")

test.run()

test.must_exist_one_of([test.workpath(f) for f in info['filename_options']])
test.must_exist(test.workpath(info['libraryname']))

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
