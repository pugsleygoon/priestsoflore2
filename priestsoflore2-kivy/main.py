
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
from maproomcavern import *
from maproomgaiasnavel import *
from maproomhauntedforest import *
from maproomhauntedforestcanon import *
from player import *
from text import *
from scrollingtext import *
from functools import partial

class Renderer(Widget):
    def __init__(self, **kwargs):
        self.x = 0 
        self.y = 0 
        self.w = 2000 
        self.h = 400 
        self.z = 1.0
        super(Renderer, self).__init__(**kwargs)
        with self.canvas:
		self.maproom = Maproomgaiasnavel(-250,0,1536,1536,'./pics/bg-gaiasnavel-1.png')
		self.player = Player(300,300,32,32)
		self.text = Scrollingtext(0,580,5,"you are in the woods")
        Clock.schedule_interval(partial(self.update, self.maproom, self.player), 1 / 60.)
	###self.add_widget(self.maproom)
	###self.add_widget(self.player)

    def update(self, room, player, *largs):
	location = self.maproom.updateroom(room, player)
	if location:
		if location == "Haunted Forest Canon":
			self.canvas.clear()
			with self.canvas:
				self.maproom = Maproomhauntedforestcanon(0,-100,251,350, './pics/bg-hauntedforest-canon-1.png')	
				self.player = Player(50,0,32,32)
				self.text = Scrollingtext(0,580,5,"you are in the woods")
		elif location == "Haunted Forest":
			self.canvas.clear()
			with self.canvas:
				self.maproom = Maproomhauntedforest(0,-100,500,850, './pics/bg-hauntedforest-1.png')	
				self.player = Player(200,0,32,32)
				self.text = Scrollingtext(0,580,5,"you are in the woods")
        	elif location == "Gaia's Navel":
			self.canvas.clear()
			with self.canvas:
				self.maproom = Maproomgaiasnavel(-50,-1000,1536,1536,'./pics/bg-gaiasnavel-1.png')
				self.player = Player(300,300,32,32)
				self.text = Scrollingtext(0,580,5,"you are in the woods")
	player.updateplayer(self.maproom)

    def move_left(self):
	self.player.direction = self.player.LEFT
	self.maproom.move_right(self.player)

    def move_right(self):
	self.player.direction = self.player.RIGHT
	self.maproom.move_left(self.player)

    def move_up(self):
	self.player.direction = self.player.UP
	self.maproom.move_down(self.player)

    def move_down(self):
	self.player.direction = self.player.DOWN
	self.maproom.move_up(self.player)

### kivy widget docs
    def on_touch_down(self, touch):
	
	# push the current coordinate, to be able to restore it later
    	touch.push()

    	# transform the touch coordinate to local space
    	touch.apply_transform_2d(self.to_local)
	if touch.is_double_tap:
		print ('Renderer : Touch is double tap -> fight!')
		self.player.fight(self.maproom)
    	# dispatch the touch as usual to children
    	# the coordinate in the touch is now in local space
    	###ret = super(..., self).on_touch_down(touch)

    	# whatever the result, don't forget to pop your transformation
    	# after the call, so the coordinate will be back in parent space
    	touch.pop()

    	# return the result (depending what you want.)
    	###return ret

    def on_touch_move(self, touch):
	if touch.dx > 1:
       		self.move_left()
	elif touch.dx < -1:
       		self.move_right()
	if touch.dy > 1:
       		self.move_up()
	elif touch.dy < -1:
       		self.move_down()
        ###else:
	###	super(Widget, self).on_touch_down(touch)
 
class RendererApp(App):
##    runTouchApp(MyKeyboardListener())
##    Renderer()
##    runTouchApp(MyKeyboardListener())
##    def __init__(self, kbl):
##    def on_touch_move(self, touch):
##        print(touch.profile)      
##        ### return super(...,self).on_touch_move(touch)

    def build(self):
        ###self.add_widget(Renderer())
        return Renderer() 

if __name__ == "__main__":
    RendererApp().run()
    ### RendererApp()
