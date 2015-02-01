
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
from rng import *

import pygame
from pygame.locals import *

class Entity(Widget):
    ""
    def __init__(self, xx,yy,ww,hh, **kwargs):
        self.x = xx
	self.y = yy
	self.w = ww
	self.h = hh

	self.hitpoints = 1
	
	self.rng = RNG(self)
 
        super(Entity, self).__init__(**kwargs)

    def update(self, room):
	1

    def collide(self, room, player):
	if (player.x + room.relativex >= self.x and 
		player.x + room.relativex <= self.x + self.w and
		player.y + room.relativey >= self.y and 
		player.y + room.relativey <= self.y + self.h):
		return 1
	return 0

    def collidefight(self, room, player):
	if (player.x + player.w >= self.x + room.relativex and 
		player.x - player.w <= self.x + self.w + room.relativex and
		player.y + player.h >= self.y + room.relativey and 
		player.y - player.h <= self.y + self.h + room.relativey):
		return 1
	return 0

    def hit(self, room, player):
	self.hitpoints -= self.rng.hitwithplayer(player)	
    	
    def damage(self, n):
	self.hitpoints -= n	
