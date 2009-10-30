#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of Liquid Ice Server.
# Copyright (C) 2009 Anthony Bourguignon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup

setup(name='liquidice-server',
      version='0.1',
      description='Liquid Ice Server',
      long_description='Liquid Ice is a restful based news aggregator. This is the server part.',
      author='Anthony Bourguignon',
      author_email='contact@toniob.net',
      url='http://liquid-ice.org/',
      license='AGPLv3+',
      package_dir={'': 'src'},
      packages=[''],
     )

