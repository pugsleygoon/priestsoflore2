
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
from polygon import *
from buzzbee import *

from kivy.base import runTouchApp
### from keyb import *
from maproomdungeon import *

class Maproomhauntedforest(Maproomdungeon):
    def __init__(self, x,y,w,h, bgfilename,**kwargs):
	Maproomdungeon.__init__(self, x,y,w,h,bgfilename,**kwargs)
	self.locationtext = "Haunted Forest"

    def exitp(self, player):
	print "player x=%d y=%d relx=%d rely=%d" % (player.x, player.y,self.relativex, self.relativey)
	if self.relativey > -100 and self.relativex <= 0 and self.relativex >= -100:
		return "Gaia's Navel"
	elif self.relativey <= -180 and self.relativey >= -220 and self.relativex <= -250 and self.relativex >= -350:
		return "Haunted Forest Canon"
