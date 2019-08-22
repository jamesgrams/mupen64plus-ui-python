# -*- coding: utf-8 -*-
# Author: Milan Nikolic <gen2brain@gmail.com>
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

from optparse import OptionParser

from m64py.core.defs import FRONTEND_VERSION

usage = 'usage: %prog <romfile>'
parser = OptionParser(usage=usage, version="M64Py Version %s" % FRONTEND_VERSION)
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="show verbose output")
parser.add_option("-s", "--savedir", action="store", type="string", dest="savedir", help="specify save directory")
parser.add_option("-c", "--sshotdir", action="store", type="string", dest="sshotdir", help="specify screenshot directory")
parser.add_option("-f", "--fullscreen", action="store_true", dest="fullscreen", help="start fullscreen")
opts, args = parser.parse_args()

VERBOSE = opts.verbose
SAVE_DIR = opts.savedir
SCREENSHOT_DIR = opts.sshotdir
FULLSCREEN = opts.fullscreen
