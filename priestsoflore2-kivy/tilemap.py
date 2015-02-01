
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
from gameobject import *

class Tilemap:
    ""
    def __init__(self,box):
	self.box = box
	self.tilew = 96 
	self.tileh = 96

    def draw(self, room):
	for j in range(0, self.box.w / self.tilew):
		Rectangle(source=self.box.gettopimage(),pos=(self.box.x+j*self.tilew+room.relativex, self.box.y+room.relativey))		

#	for i in range(0, self.box.h / self.tileh): # substract one
#		for k in range(0, self.box.w / self.tilew): 
#			screen.blit(self.box.getimage(),(self.box.x+k*self.tilew+room.relativex, self.box.y+i*self.tileh+room.relativey))		
#		
