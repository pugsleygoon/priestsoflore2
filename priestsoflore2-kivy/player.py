
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
from kivy.core.image import Image
### from objloader import ObjFile

import pygame
from pygame.locals import *
from stateimagelibrary import *
from stateimagetexturelibrary import *

class Player(Widget):
    ""
    def __init__(self, xx,yy,ww,hh, **kwargs):
        self.x = xx
	self.y = yy
	self.w = ww
	self.h = hh 
        self.hitpoints = 1200 #FIX else wall/floor disappears
	super(Player, self).__init__(**kwargs)

	self.LEFT = 0
	self.RIGHT = 1
	self.UP = 2
	self.DOWN = 3
	self.direction = self.LEFT

	self.fightcounter = 0

	self.stimlibright = Stateimagetexturelibrary()
	self.imager = Image('./pics/player-right-1.png')
	self.stimlibright.add(self.imager)

	self.stimlibleft = Stateimagetexturelibrary()
	self.imagel = Image('./pics/player-left-1.png')
	self.stimlibleft.add(self.imagel)

	self.stimlibup = Stateimagetexturelibrary()
	self.imageu = Image('./pics/player-up-1.png')
	self.stimlibup.add(self.imageu)

	self.stimlibdown = Stateimagetexturelibrary()
	self.imaged= Image('./pics/player-down-1.png')
	self.stimlibdown.add(self.imaged)

	self.stimlibfightleft = Stateimagetexturelibrary()
	self.imagelf= Image('./pics/player-left-fight-1.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-1.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-1.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-1.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-1.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-1.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-2.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-2.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-2.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-2.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-2.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-2.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-3.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-3.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-3.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-3.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-3.png')
	self.stimlibfightleft.add(self.imagelf)
	self.imagelf= Image('./pics/player-left-fight-3.png')
	self.stimlibfightleft.add(self.imagelf)

	self.stimlibfightright = Stateimagetexturelibrary()
	self.imagefr= Image('./pics/player-right-fight-1.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-1.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-1.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-1.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-1.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-1.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-2.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-2.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-2.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-2.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-2.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-2.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-2.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-3.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-3.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-3.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-3.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-3.png')
	self.stimlibfightright.add(self.imagefr)
	self.imagefr= Image('./pics/player-right-fight-3.png')
	self.stimlibfightright.add(self.imagefr)

	self.stimlibfightup = Stateimagetexturelibrary()
	self.imageuf= Image('./pics/player-up-fight-1.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-1.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-1.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-1.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-1.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-1.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-2.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-2.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-2.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-2.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-2.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-2.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-3.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-3.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-3.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-3.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-3.png')
	self.stimlibfightup.add(self.imageuf)
	self.imageuf= Image('./pics/player-up-fight-3.png')
	self.stimlibfightup.add(self.imageuf)

	self.stimlibfightdown = Stateimagetexturelibrary()
	self.imagedf= Image('./pics/player-down-fight-1.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-1.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-1.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-1.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-1.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-1.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-2.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-2.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-2.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-2.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-2.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-2.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-3.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-3.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-3.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-3.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-3.png')
	self.stimlibfightdown.add(self.imagedf)
	self.imagedf= Image('./pics/player-down-fight-3.png')
	self.stimlibfightdown.add(self.imagedf)

	self.image = Image('./pics/player-right-1.png')
	Color(0,0,0,0,mode='rgba')
	self.image = Rectangle(texture=self.image.texture, pos=(self.x,self.y), size=(self.w,self.h))

    def updateplayer(self, room):
	if self.fightcounter == 0:
		if self.direction == self.LEFT:
			self.stimlibleft.update(self.image, self.x,self.y)
		elif self.direction == self.RIGHT:
			self.stimlibright.update(self.image, self.x,self.y)	
		elif self.direction == self.UP:
			self.stimlibdown.update(self.image, self.x,self.y)
		elif self.direction == self.DOWN:
			self.stimlibup.update(self.image, self.x,self.y)
	elif self.fightcounter > 0: 
		self.fightcounter -= 1
		if self.direction == self.LEFT:
			self.stimlibfightleft.update(self.image, self.x, self.y)	
		elif self.direction == self.RIGHT:
			self.stimlibfightleft.update(self.image, self.x, self.y)
		elif self.direction == self.UP:
			self.stimlibfightup.update(self.image, self.x, self.y)	
		elif self.direction == self.DOWN:
			self.stimlibfightdown.update(self.image, self.x, self.y)

    def draw(self, room):
	self.image

    def fight(self, room):
	self.fightcounter = 3*6
	room.fight(self)

    def roll(self):
	###return self.rng.damage(-1)
	return 1
				
