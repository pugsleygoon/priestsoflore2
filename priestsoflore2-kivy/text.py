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

from kivy.app import * 
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.widget import Widget
from kivy.resources import resource_find
from kivy.graphics.transformation import Matrix
from kivy.graphics.opengl import *
from kivy.graphics import *
from textfont import * 

class Text(Textfont):
    def __init__(self,xx,yy,nlines,string,**kwargs):
	Textfont.__init__(self, **kwargs)
	super(Text, self).__init__(**kwargs)

	self.x = xx
	self.y = yy
	self.nlines = nlines

	self.lineoffset = 16	
	self.characteroffset = 16/2
	self.blittedstring = string

	Color(.82,.82,.82, .5)
	Rectangle(pos=(self.x, self.y), size=(len(self.blittedstring * self.characteroffset), self.lineoffset*self.nlines))
	Color(.10,.10,.10)
	for i in range(0, len(self.blittedstring)):
		Rectangle(pos=(self.x+self.characteroffset*i,self.y), source=self.letters[self.blittedstring[i]], size=(12,12))	
	Color(.82,.82,.82, 1)
	Line(points=[self.x, self.y, self.x+len(self.blittedstring * self.characteroffset), self.y])
	Line(points=[self.x, self.y+self.lineoffset*self.nlines, self.x+len(self.blittedstring * self.characteroffset), self.y+self.lineoffset*self.nlines])
	Line(points=[self.x, self.y, self.x, self.y+self.lineoffset*self.nlines])
	Line(points=[self.x+len(self.blittedstring * self.characteroffset), self.y, self.x+len(self.blittedstring * self.characteroffset), self.y+self.lineoffset*self.nlines])
	
