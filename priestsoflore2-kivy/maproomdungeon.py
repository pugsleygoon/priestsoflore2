
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
from maproombase import *

class Maproomdungeon(Maproombase):
    def __init__(self, x,y,w,h, bgfilename,**kwargs):
	Maproombase.__init__(self, x,y,w,h,bgfilename,**kwargs)
	self.entities = []
	self.locationtext = ""

    def fight(self, player):
	for e in self.entities:
		if e.collidefight(self, player):
			print "***hit!"
			e.hit(self, player)


    def updateroom(self, room, player):
	with self.canvas:
		player.draw(self)
		for e in self.entities:
			if e:
				e.update(self)	
				if e.collide(self, player):
					1
	for e in self.entities:
		if e.hitpoints <= 0:
			1 ### FIXME

	# returns None or the room location text
	return self.exitp(player)

##    def on_touch_move(self, touch):
##	if touch.dx > 20:
##       		self.move_right()
##	if touch.dx < -20:
##       		self.move_left()
##	if touch.dy > 20:
##       		self.move_up()
##	if touch.dy < -20:
##       		self.move_down()
        ###else:
	###	super(Widget, self).on_touch_down(touch)
