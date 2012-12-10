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

import re
import yaml

import htmltag

class Parser:
    """Parses .tmpl file to be outputted as an html file. """
    def __init__(self, config_file = 'templ.conf'):
        self.config_file = config_file
        self.tree = None
        self.rules = {}
        self._load_config()

    def _load_config(self):
        """Loads the configuration settings from the config_file."""
        with open(self.config_file, 'r') as config:
            self.rules = yaml.load(config)

    def parse(self, pray_file):
        """Parse the input file and output a syntax tree.

        Parameters:
        pray_file - The name of the pray file to be parsed.
        
        """
        # Begin parsing the file
        with open(pray_file, 'r') as input_file:
            syntax_tree = Tree()
            lines = []
            # Read the entire file as a list of lines
            for line in input_file:
                line = line.strip('\n')
                
                # First, expand any variables found in the line
                regex = re.compile(r'\$\w+')
                matches = regex.findall(line)
                if len(matches) > 0:
                    for match in matches:
                        replace = match.strip('$')
                        line = line.replace(match, self.rules[replace])
                
                # Second, turn the line into an HTML tag
                if 'DOCTYPE' in line:
                    print('Found')
                else:
                    print('Nope')
     
class NodeNotFoundError(Exception):
    """Error to be thrown when node is not found in tree."""
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return repr(self.name)
                
class Tree:
    """A parser syntax tree.
    
    The syntax tree is nothing more than an encapsulated dictionary. When
    adding nodes to the tree, the node's name parameter is used as the tree's
    key, while the node's dictionary of elements are used as the saved value.
    """
    def __init__(self):
        self.root_node = None

    def add_node(self, node):
        """Add a node to the tree.
        
        Parameters:
        Node - The node to be added to the tree.

        Returns:
        Void
                
        """        
        self.nodes[node.name] = node.elements

    def remove_node(self, node_name):
        """Remove the first node of a given name from the tree.
        
        If the node does not exist in the tree, return a NodeNotFoundError.
        
        Parameters:
        Node_Name - The name of the node to be removed from the tree.

        Returns:
        Void
            
        """
        if node_name in self.nodes:
            del self.nodes[node.name]
        else:
            raise NodeNotFoundError(node_name)
            
    def remove_nodes(self, node_name):
        """Remove all nodes of a given name from the tree.
        
        If no nodes exist in the tree, return a NodeNotFoundError.
        
        Parameters:
        Node_Name - The name of the notes to be removed from the tree.
        
        """

class Node:    
    """Element found within parser syntax tree.
    
    Nodes encapsulate 3 values: a name, a list of containing elements, and a
    list of child elements.
    
    """
    def __init__(self, html_tag, children = []):
        self.html_tag = html_tag
        self.children = children
