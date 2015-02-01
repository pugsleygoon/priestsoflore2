
# Copyright (C) Johan Ceuppens 2015
# Copyright (C) Johan Ceuppens 2014
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

# Also under Python Foundation License 2.0


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

from kivy.base import runTouchApp
### from keyb import *

class Maproombase(Widget):
    def __init__(self, x,y,w,h, bgfilename,**kwargs):
	# with what you collide :
	self.polygons = []

	self.relativex = x 
	self.relativey = y	
	self.w = w
	self.h = h 
	self.bgfilename = bgfilename
        super(Maproombase, self).__init__(**kwargs)
        with self.canvas:
        	Color(1, 1, 1, 1)
		self.bg = Rectangle(pos=(self.relativex,self.relativey), size=(self.w,self.h), source=self.bgfilename)
	
    def draw(self):
	self.canvas.clear()
        with self.canvas:
        	Color(1, 1, 1, 1)
		self.bg = Rectangle(source=self.bgfilename, pos=(self.relativex,self.relativey), size=(self.w,self.h))

    def sortleft(self,player):
	polygons = []
	for p in self.polygons:
		p.transform(self)
		if p.sortleft(player):
			polygons.append(p)
		p.untransform(self)

	return polygons

    def sortright(self,player):
	polygons = []
	for p in self.polygons:
		p.transform(self)
		if p.sortright(player):
			polygons.append(p)
		p.untransform(self)

	return polygons

    def sortup(self,player):
	polygons = []
	for p in self.polygons:
		p.transform(self)
		if p.sortup(player):
			polygons.append(p)
		p.untransform(self)

	return polygons

    def sortdown(self,player):
	polygons = []
	for p in self.polygons:
		p.transform(self)
		if p.sortdown(player):
			polygons.append(p)
		p.untransform(self)

	return polygons

##############################################################################
# NOTE : the room moves left but the other things on screen collide right
##############################################################################

    def move_left(self, player):
	polygons = self.sortright(player)
	### print "player dir = %d x = %d polygons=%s" % (player.direction, self.relativex, polygons)
	for p in polygons:
		p.transform(self)
		if p.collideright(player):
			print "***collide right"
			self.relativex += 1 
			p.untransform(self)	
			return
		p.untransform(self)	
	self.relativex -= 1 
	self.bg.pos = (self.relativex, self.relativey)
	
    def move_right(self, player):
	polygons = self.sortleft(player)
	### print "player dir = %d x = %d polygons=%s" % (player.direction, self.relativex, polygons)
	for p in polygons:
		p.transform(self)
		if p.collideleft(player):
			print "***collide left"
			self.relativex -= 1 
			p.untransform(self)
			return
		p.untransform(self)
	self.relativex += 1 
	self.bg.pos = (self.relativex, self.relativey)

    def move_up(self, player):
	polygons = self.sortdown(player)
	for p in polygons:
		p.transform(self)
		if p.collidedown(player):
			print "***collide down"
			self.relativey += 1 
			p.untransform(self)
			return
		p.untransform(self)
	self.relativey -= 1 
	self.bg.pos = (self.relativex, self.relativey)
	
    def move_down(self, player):
	polygons = self.sortup(player)
	for p in polygons:
		p.transform(self)
		if p.collideup(player):
			print "***collide up"
			self.relativey -= 1
			p.untransform(self)
			return
		p.untransform(self)
	self.relativey += 1 
	self.bg.pos = (self.relativex, self.relativey)
	

