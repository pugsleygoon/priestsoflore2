
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
import math

class Polygon:
    "Polygon for collisions"
    def __init__(self, mapheight):
	self.points = []
	self.LEFT = 0
	self.RIGHT = 1
	self.UP = 2
	self.DOWN = 3
	self.mapheight = mapheight

    def transform(self, room):
	points = []
	for p in self.points:
		p = (self.x(p)+room.relativex, self.y(p)+room.relativey)
		points.append(p)
	self.points = points

    def untransform(self, room):
	points = []
	for p in self.points:
		p = (self.x(p)-room.relativex, self.y(p)-room.relativey)
		points.append(p)
	self.points = points

    def x(self, p):
	return p[0]

    def y(self, p):
	return p[1]

    def addpoint(self, p):
	pos = (p[0], self.mapheight-p[1])
	self.points.append(p)

    def removepoint(self, p):
	self.points.remove(p)

    def sortleft(self, player):
	for point in self.points:
		if player.x <= self.x(point):
			return 1
	return 0

    def sortright(self, player):
	for point in self.points:
		if player.x >= self.x(point):
			return 1
	return 0

    def sortup(self, player):
	for point in self.points:
		if player.y <= self.y(point):
			return 1
	return 0

    def sortdown(self, player):
	for point in self.points:
		if player.y >= self.y(point):
			return 1
	return 0 

    def collideleft(self, player):
	p = (player.x, player.y)
	size = (player.w, player.h)
	min = 100000000

	point1 = (0,0)
	point2 = (0,0)
	m = 0
	i = 0
	for point in self.points:
		if abs(self.x(p) - self.x(point)) < min and self.y(p) >= self.y(point) and self.y(p) <= self.y(self.points[m-1]):
			min = abs(self.x(p) - self.x(point))
			point1 = (self.x(point), self.y(point))

			mtmp = m
			if m + 1 >= len(self.points):
				if abs(self.x(p) - self.x(self.points[m-1])) < abs(self.x(p) - self.x(self.points[0])):
					if self.y(p) >= self.y(self.points[m-1]) and self.y(p) <= self.y(self.points[0]):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[0]), self.y(self.points[0]))
				else:
					point2 = (self.x(self.points[0]), self.y(self.points[0]))
			else:
				if abs(self.x(p) - self.x(self.points[m-1])) < abs(self.x(p) - self.x(self.points[m+1])):
					if self.y(p) >= self.y(self.points[m-1]) and self.y(p) <= self.y(self.points[m+1]):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
				else:
					point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
			m = mtmp
			i = m
		m += 1

	points = []
	points.append(point1)	 
	points.append(point2)
		
	n = 0
	for point in points:
		if n == len(self.points)-1: 
			if self.intersectleftp(point,self.points[0], p, size):
				return 1
		else:
			if self.intersectleftp(point,self.points[n+1], p, size):
				return 1
				
		n += 1
	return 0

    def collideright(self, player):
	p = (player.x, player.y)
	size = (player.w, player.h)
	min = 100000000

	point1 = (0,0)
	point2 = (0,0)
	m = 0
	i = 0
	for point in self.points:
		if abs(self.x(p) - self.x(point)) < min and self.y(p) >= self.y(point) and self.y(p) <= self.y(self.points[m-1]):
			min = abs(self.x(p) - self.x(point))
			point1 = (self.x(point), self.y(point))

			mtmp = m
			if m + 1 >= len(self.points):
				if abs(self.x(p) - self.x(self.points[m-1])) < abs(self.x(p) - self.x(self.points[0])):
					if self.y(p) >= self.y(self.points[m-1]) and self.y(p) <= self.y(self.points[0]):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[0]), self.y(self.points[0]))
				else:
					point2 = (self.x(self.points[0]), self.y(self.points[0]))
			else:
				if abs(self.x(p) - self.x(self.points[m-1])) < abs(self.x(p) - self.x(self.points[m+1])):
					if self.y(p) >= self.y(self.points[m-1]) and self.y(p) <= self.y(self.points[m+1]):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
				else:
					point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
			m = mtmp
			i = m
		m += 1

	points = []
	points.append(point1)	 
	points.append(point2)
		

	n = 0
	for point in points:
		if n == len(self.points)-1: 
			if self.intersectrightp(point,self.points[0], p, size):
				return 1
		else:
			if self.intersectrightp(point,self.points[n+1], p, size):
				return 1
				
		n += 1
	return 0

    def collideup(self, player):
	p = (player.x, player.y)
	size = (player.w, player.h)

	min = 100000000

	point1 = (0,0)
	point2 = (0,0)
	m = 0
	i = 0
	for point in self.points:
		if abs(self.y(p) - self.y(point)) < min and self.x(p) >= self.x(point) and self.x(p) <= self.x(self.points[m-1]):
			min = abs(self.y(p) - self.y(point))
			point1 = (self.x(point), self.y(point))

			mtmp = m
			if m + 1 >= len(self.points):
				if self.x(p) >= self.x(self.points[m-1]) and self.x(p) <= self.x(self.points[0]):
					if abs(self.y(p) - self.y(self.points[m-1])) < abs(self.y(p) - self.y(self.points[0])):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[0]), self.y(self.points[0]))
				else:
					point2 = (self.x(self.points[0]), self.y(self.points[0]))
			else:
				if self.x(p) >= self.x(self.points[m-1]) and self.x(p) <= self.x(self.points[m+1]):
					if abs(self.y(p) - self.y(self.points[m-1])) < abs(self.y(p) - self.y(self.points[m+1])):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
				else:
					point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
			m = mtmp
			i = m
		m += 1

	points = []
	points.append(point1)	 
	points.append(point2)
		

	n = 0
	for point in points:
		if n == len(self.points)-1: 
			if self.intersectupp(point,self.points[0], p, size):
				return 1
		else:
			if self.intersectupp(point,self.points[n+1], p, size):
				return 1
				
		n += 1
	return 0

    def collidedown(self,  player):
	p = (player.x, player.y)
	size = (player.w, player.h)
	min = 100000000

	point1 = (0,0)
	point2 = (0,0)
	m = 0
	i = 0
	for point in self.points:
		if abs(self.y(p) - self.y(point)) < min and self.y(p) >= self.y(point) and self.y(p) <= self.y(self.points[m-1]):
			min = abs(self.y(p) - self.y(point))
			point1 = (self.x(point), self.y(point))

			mtmp = m
			if m + 1 >= len(self.points):
				if self.x(p) >= self.x(self.points[m-1]) and self.x(p) <= self.x(self.points[0]):
					if abs(self.y(p) - self.y(self.points[m-1])) < abs(self.y(p) - self.y(self.points[0])):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[0]), self.y(self.points[0]))
				else:
					point2 = (self.x(self.points[0]), self.y(self.points[0]))
			else:
				if self.x(p) >= self.x(self.points[m-1]) and self.y(p) <= self.y(self.points[m+1]):
					if abs(self.y(p) - self.y(self.points[m-1])) < abs(self.x(p) - self.x(self.points[m+1])):
						point2 = (self.x(self.points[m-1]), self.y(self.points[m-1]))
					else:
						point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
				else:
					point2 = (self.x(self.points[m+1]), self.y(self.points[m+1]))
			m = mtmp
			i = m
		m += 1

	points = []
	points.append(point1)	 
	points.append(point2)
		

	n = 0
	for point in self.points:
		if n == len(self.points)-1: 
			if self.intersectdownp(point,self.points[0], p, size):
				return 1
		else:
			if self.intersectdownp(point,self.points[n+1], p, size):
				return 1
				
		n += 1
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
