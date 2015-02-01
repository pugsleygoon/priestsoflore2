
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


import pygame
from pygame.locals import *
from gameobject import *

class Polygon:
    "Polygon for collisions"
    def __init__(self):
	self.points = []
	self.LEFT = 0
	self.RIGHT = 1
	self.UP = 2
	self.DOWN = 3

    def x(self, p):
	return p[0]

    def y(self, p):
	return p[1]

    def addpoint(self, p):
	self.points.append(p)

    def removepoint(self, p):
	self.points.remove(p)

    def sortleft(self, p):	
	n = 0
	for point in self.points:
		if self.x(point) < self.x(p):
			n += 1
	if n == len(self.points):
		return self
	else:
		return None

    def sortright(self, p):
	n = 0
	for point in self.points:
		if self.x(point) > self.x(p):
			n += 1
	if n == len(self.points):
		return self
	else:
		return None

    def sortup(self, p):
	n = 0
	for point in self.points:
		if self.y(point) < self.y(p):
			n += 1
	if n == len(self.points):
		return self
	else:
		return None

    def sortdown(self, p):
	n = 0
	for point in self.points:
		if self.y(point) > self.y(p):
			n += 1
	if n == len(self.points):
		return self
	else:
		return None

    def collideleft(self, w,h, direction, p, size):
	pc = (w, h)
	pc2 = (w, h)
	for point in self.points:
		if self.x(point) <= self.x(pc):
			pc2 = (pc[0],pc[1])
			pc = (self.x(point),self.y(point))
			
	if self.intersectleftp(pc, pc2, p, size):
		return 1	
	return 0

    def collideright(self, w,h, direction, p, size):
	pc = (w, h)
	pc2 = (w, h)
	for point in self.points:
		if self.x(point) >= self.x(pc):
			pc2 = (pc[0],pc[1])
			pc = (self.x(point),self.y(point))
			
	if self.intersectrightp(pc, pc2, p, size):
		return 1	
	return 0

    def collideup(self, w,h, direction, p, size):
	pc = (w, h)
	pc2 = (w, h)
	for point in self.points:
		if self.y(point) <= self.y(pc):
			pc2 = (pc[0],pc[1])
			pc = (self.x(point),self.y(point))
			
	if self.intersectupp(pc, pc2, p, size):
		return 1	
	return 0

    def collidedown(self, w,h, direction, p, size):
	pc = (w, h)
	pc2 = (w, h)
	for point in self.points:
		if self.y(point) >= self.y(pc):
			pc2 = (pc[0],pc[1])
			pc = (self.x(point),self.y(point))
			
	if self.intersectdownp(pc, pc2, p, size):
		return 1	
	return 0

    def intersectleftp(self, point1, point2, p, size):
	if self.calcline(point1, point2, p) <= 0:
		return 1 
	return 0

    def intersectrightp(self, point1, point2, p, size):
	if self.calcline(point1, point2, p) >= 0:
		return 1 
	return 0

    def intersectupp(self, point1, point2, p, size):
	if self.calcline(point1, point2, p) <= 0:
		return 1	
	return 0

    def intersectdownp(self, point1, point2, p, size):
	if self.calcline(point1, point2, p) >= 0:
		return 1	
	return 0

    def calcline(self, point1, point2, p):
	if self.x(point2) - self.x(point1) != 0:
		ds = (self.y(point2) - self.y(point1)) / (self.x(point2) - self.x(point1))
	else:
		ds = 1000000000
	if self.y(p) < ds * (self.x(p) - self.x(point1)) + self.y(point1):
		return -1	
	if self.y(p) > ds * (self.x(p) - self.x(point1)) + self.y(point1):
		return 1	
	if self.y(p) == ds * (self.x(p) - self.x(point1)) + self.y(point1):
		return 0	
