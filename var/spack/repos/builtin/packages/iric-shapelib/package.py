##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
from spack import *


class IricShapelib(MakefilePackage):
    """Library to read and write ESRI Shapefiles."""

    homepage = "http://shapelib.maptools.org/"
    url      = "file:///home/charlton/iric-shapelib-1.3.0.zip"

    version('1.3.0', 'ed9d5edfa7531e5fd1aefa10a541c477')

    variant('debug', default=False, description='Build a debugging version.')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.include)
        mkdir(prefix.lib)
        make('install', 'PREFIX={0}'.format(prefix))

    def build(self, spec, prefix):
        # todo update for compiler flag specs
        if '+debug' in spec:
            make()
        else:
            # FIXME update for compiler flag specs
            # see https://spack.readthedocs.io/en/latest/basic_usage.html#compiler-flags
            make('CFLAGS=-O3 -DNDEBUG -fPIC')
