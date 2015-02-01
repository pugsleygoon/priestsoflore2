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
### from objloader import ObjFile

class Textfont(Widget):
    def __init__(self,**kwargs):
	self.letters = dict() 
	self.letters[' '] = './pics/font-space.png'
	self.letters['a'] = './pics/font-a.png'
	self.letters['b'] = './pics/font-b.png'
	self.letters['c'] = './pics/font-c.png'
	self.letters['d'] = './pics/font-d.png'
	self.letters['e'] = './pics/font-e.png'
	self.letters['f'] = './pics/font-f.png'
	self.letters['g'] = './pics/font-g.png'
	self.letters['h'] = './pics/font-h.png'
	self.letters['i'] = './pics/font-i.png'
	self.letters['j'] = './pics/font-j.png'
	self.letters['k'] = './pics/font-k.png'
	self.letters['l'] = './pics/font-l.png'
	self.letters['m'] = './pics/font-m.png'
	self.letters['n'] = './pics/font-n.png'
	self.letters['o'] = './pics/font-o.png'
	self.letters['p'] = './pics/font-p.png'
	self.letters['q'] = './pics/font-q.png'
	self.letters['r'] = './pics/font-r.png'
	self.letters['s'] = './pics/font-s.png'
	self.letters['t'] = './pics/font-t.png'
	self.letters['u'] = './pics/font-u.png'
	self.letters['v'] = './pics/font-v.png'
	self.letters['w'] = './pics/font-w.png'
	self.letters['x'] = './pics/font-x.png'
	self.letters['y'] = './pics/font-y.png'
	self.letters['z'] = './pics/font-z.png'

	super(Textfont, self).__init__(**kwargs)

	self.blittedstring = ""

