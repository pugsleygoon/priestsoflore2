
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
from maproomdungeon import *

class Maproomcavern(Maproomdungeon):
    def __init__(self, x,y,w,h, bgfilename,**kwargs):
	Maproomdungeon.__init__(self, x,y,w,h,bgfilename,**kwargs)
	self.snail = Snail(0,0,48,48)
	self.entities.append(self.snail)
	
### kivy widget docs
    def on_touch_move(self, touch):
	if touch.dx > 10:
       		self.move_left()
	elif touch.dx < -10:
       		self.move_right()
        ###else:
	###	super(Widget, self).on_touch_down(touch)
 
class RendererApp(App):
##    runTouchApp(MyKeyboardListener())
##    Renderer()
##    runTouchApp(MyKeyboardListener())
##    def __init__(self, kbl):
    def on_touch_move(self, touch):
        print(touch.profile)      
        ### return super(...,self).on_touch_move(touch)

    def build(self):
        ###self.add_widget(Renderer())
        return Renderer() 

if __name__ == "__main__":
    RendererApp().run()
    ### RendererApp()
