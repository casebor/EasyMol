#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  handler.py
#  
#  Copyright 2016 Carlos Eduardo Sequeiros Borja <casebor@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class Handler:
    """
    """
    
    def __init__(self, glarea):
	self.glarea = glarea
    
    def switch_ball_stick(self, button):
	""" Turn on/off Ball-Stick representation.
	"""
	try:
	    self.glarea.BALL_STICK = not self.glarea.BALL_STICK
	    self.glarea.draw_ball_stick()
	    self.glarea.queue_draw()
	except AssertionError as ae:
	    self.glarea.BALL_STICK = not self.glarea.BALL_STICK
	    print 'Error en los datos'
	return True
    
    
    def switch_dots(self, button):
	""" Turn on/off Dots representation.
	"""
	self.glarea.DOTS = not self.glarea.DOTS
	self.glarea.draw_dots()
	self.glarea.queue_draw()
	return True
    
    def switch_lines(self, button):
	""" Turn on/off Lines representation.
	"""
	self.glarea.LINES = not self.glarea.LINES
	self.glarea.draw_lines()
	self.glarea.queue_draw()
	return True
    
    def switch_pretty_vdw(self, button):
	""" Turn on/off the Pretty VDW representation.
	"""
	self.glarea.PRETTY_VDW = not self.glarea.PRETTY_VDW
	self.glarea.draw_pretty_vdw()
	self.glarea.queue_draw()
	return True
    
    def switch_ribbon(self, button):
	""" Turn on/off the Ribbon representation.
	"""
	self.glarea.RIBBON = not self.glarea.RIBBON
	self.glarea.draw_ribbon()
	self.glarea.queue_draw()
	return True
    
    def switch_spheres(self, button):
	""" Turn on/off the Sphere representation.
	"""
	self.glarea.SPHERES = not self.glarea.SPHERES
	self.glarea.draw_spheres()
	self.glarea.queue_draw()
	return True
    
    def switch_vdw(self, button):
	""" Turn on/off the Van-Der-Waals representation.
	"""
	self.glarea.VDW = not self.glarea.VDW
	self.glarea.draw_vdw()
	self.glarea.queue_draw()
	return True
    
    def switch_wires(self, button):
	""" Turn on/off the Wires representation.
	"""
	self.glarea.WIRES = not self.glarea.WIRES
	self.glarea.draw_wires()
	self.glarea.queue_draw()
	return True
    
    def load_mol(self, data):
	"""
	"""
	print 'loading'
	














