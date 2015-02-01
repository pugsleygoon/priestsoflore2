#!/usr/local/bin/python
# Copyright (C) Johan Ceuppens 2015
# Copyright (C) Johan Ceuppens 2010
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Stateimagetexturelibrary:
    def __init__(self):
	self.index = 0
	self.max = 0
	self.list = []

    def add(self, image):
	self.list.append(image)
	self.max += 1

    def updatestatic(self, imagerect, xx, yy, index):
	if (self.index >= self.max):
            self.index = 0

	
	imagerect.pos = (xx,yy)
	imagerect.texture=self.list[self.index].texture
	imagerect.texture	

    def update(self, imagerect, xx, yy):
	if (self.index >= self.max):
            self.index = 0
	self.index += 1	

	imagerect.pos = (xx,yy)
	imagerect.texture=self.list[self.index-1].texture
	imagerect.texture
