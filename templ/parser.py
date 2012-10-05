#!/usr/bin/env python3

# This file is a part of Templ
# Copyright (C) 2012 Zachary Dziura
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class Parser:

	"""Parses .tmpl file to be outputted as an html file. """

	def __init__(self, config_file = ""):
		config_file = config_file
		self.tree = {}
		self.rules = {
			"doctype": "<!DOCTYPE html>",
			"language": "en",
			"charset": "utf-8"
		}

	def parse(self):
		"""Parse the input file and output a syntax tree.

		Parameters:
			input_file -- A string representing the config file name
				If none exists, default to rules found in the Parser class
		
		"""

class Tree:

	"""A parser syntax tree."""

	def __init__(self):
		self.nodes = {}

	def add_node(self, node):
		"""Adds a node to the tree."""
		
		self.nodes[node.name] = node.elements

	def remove_node(self, node):
		"""If the node exists in the tree, remove it. Returns an error message otherwise."""

		if node.name in self.nodes:
			del self.nodes[node.name]
		else:
			print(node.name + " does not exist in the tree.")

class Node:
	
	"""Element found within parser syntax tree."""

	def __init__(self, name, elements = {}):
		self.name = name
		self.elements = elements
