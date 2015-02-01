
# Copyright (C) Johan Ceuppens 2015 
# Copyright (C) Johan Ceuppens 2014 
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

import pygame
from pygame.locals import *
from enemy import *
import math

class BuzzBee(Enemy):
    ""
    def __init__(self, xx,yy, **kwargs):
	Enemy.__init__(self,xx,yy,31,48,**kwargs)
        self.hitpoints = 1
	super(BuzzBee, self).__init__(xx,yy,31,48,**kwargs)

	self.image = Rectangle(source='./pics/buzzbee-left-1.png', pos=(self.x, self.y), size=(31,48))
	
	self.counter = 0
	self.centerx = self.x

    def update(self, room):

	if self.hitpoints <= 0:
		self.image.source='./pics/buzzbee-dead-1.png'
		self.image.pos = (self.x+room.relativex, self.y+room.relativey)
		return

	self.x = self.centerx + math.sin(self.counter) * 100
	self.counter += 0.01

	self.image.pos = (self.x+room.relativex, self.y+room.relativey)
	self.image

###    def on_touch_down(self, touch):
###	if touch.isdouble_tap:
###		print ('Touch is double tap!')
