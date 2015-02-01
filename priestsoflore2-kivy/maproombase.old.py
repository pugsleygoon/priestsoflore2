
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

	self.relativex = 0
	self.relativey = 0	
	self.w = w
	self.h = h 
	self.bgfilename = bgfilename
        super(Maproombase, self).__init__(**kwargs)
        with self.canvas:
        	Color(1, 1, 1, 1)
		self.bg = Rectangle(pos=(self.x,self.y), size=(self.w,self.h), source=self.bgfilename)
	
    def draw(self):
	self.canvas.clear()
        with self.canvas:
        	Color(1, 1, 1, 1)
		self.bg = Rectangle(source=self.bgfilename, pos=(self.relativex,self.relativey), size=(self.w,self.h))

    def sortleft(self,xx):
	polygons = []
	for p in self.polygons:
		if p.sortleft((xx,0)):
			polygons.append(p)

	return polygons

    def sortright(self,xx):
	polygons = []
	for p in self.polygons:
		if p.sortright((xx,0)):
			polygons.append(p)

	return polygons

    def sortup(self,yy):
	polygons = []
	for p in self.polygons:
		if p.sortup((0,yy)):
			polygons.append(p)

	return polygons

    def sortdown(self,yy):
	polygons = []
	for p in self.polygons:
		if p.sortdown((0,yy)):
			polygons.append(p)

	return polygons

    def move_left(self, player):
	print "player dir = %d" % (player.direction)
	polygons = self.sortleft(self.polygons)	
	for p in polygons:
		if p.collideleft(0, 0, player.direction, (player.x, player.y), (player.w,player.h)):
	
			self.relativex -= 1 
			if player.direction == player.LEFT:
				if p.collideright(self.w,0,player.direction, (player.x,player.y), (player.w,player.h)):
					self.relativex -= 1 
			
			return
	self.relativex += 1 
	self.bg.pos = (self.relativex, self.relativey)
	
    def move_right(self, player):
	print "player dir = %d" % (player.direction)
	polygons = self.sortright(self.polygons)	
	for p in polygons:
		if p.collideright(self.w, 0, player.direction, (player.x, player.y), (player.w,player.h)):
			if player.direction == player.RIGHT:
				self.relativex += 1 
			return
	self.relativex -= 1 
	self.bg.pos = (self.relativex, self.relativey)

    def move_up(self, player):
	print "player dir = %d" % (player.direction)
	polygons = self.sortup(self.polygons)	
	for p in polygons:
		if p.collideup(0, 0, player.direction, (player.x, player.y), (player.w,player.h)):
			if player.direction == player.UP:
				self.relativey -= 1 
			return
	self.relativey += 1 
	self.bg.pos = (self.relativex, self.relativey)
	
    def move_down(self, player):
	print "player dir = %d" % (player.direction)
	polygons = self.sortdown(self.polygons)	
	for p in polygons:
		if p.collidedown(0, self.h, player.direction, (player.x, player.y), (player.w,player.h)):
			if player.direction == player.DOWN:
				self.relativey += 1
			return
	self.relativey -= 1 
	self.bg.pos = (self.relativex, self.relativey)
	

