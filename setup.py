#!/usr/bin/env python3

# Templ - A simple HTML generator written in Python
# Copyright (C) 2012 Zachary Dziura
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(
	name='Templ',
	version='0.1dev',
	description='A beautiful, little HTML templating engine',
	packages=['templ'],
	scripts=['templ.conf'],
	author='Zachary Dziura',
	author_email='zcdziura@gmail.com',
	license='GPLv3',
	long_description=open('README.txt').read(),
	install_requires = ['PyYAML >= 3.10'],
)
