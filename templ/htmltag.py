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

class HtmlTag:
	
	"""Object representation of an HTML tag.
    
    A very simple class that encapsulates an HTML tag. It doesn't do
    much other than that, I'm afraid. At least not yet!
    
    """

	def __init__(self):
		self.name = ""
		self.attributes = {}
		self.text = ""
		self.child_elements = []
		self.valid_tags = ()
		
	def validate(self):
		return

class BlockHtmlTag(HtmlTag):

    """Object representation of a block-level HTML tag.
    
    Attributes:
    	name -- The name of the HTML tag (head, body, etc)
    	attributes -- A list of HTML tag attributes
    	text -- The optional text accompanying the tag
    	
    """

    def __init__(self, name, attributes = {}, text = ""):
        self.name = name
        self.attributes = attributes
        self.text = text
        
        self.valid_tags = (
		    "article", "aside", "blockquote", "body", "br", "button",
		    "canvas", "caption", "col", "colgroup", "dd", "div", "dl", "dt",
		    "embed", "fieldset", "figcaption", "figure", "footer", "form",
		    "h1-6", "header", "hgroup", "hr", "li", "map", "object", "ol",
		    "output", "p", "pre", "progress", "section", "table", "tbody",
		    "textarea", "tfoot", "th", "tr", "ul", "video"
    	)

    def validate(self):
        if self.name in self.valid_tags:
            return True
        else:
            raise InvalidTagError(self.name, self.name + " is not a valid HTML tag.")

class InvalidTagError(Exception):
    
    """Error to be raised when given HTML tag isn't valid.
    
    Attributes:
        expression -- The expression in which the error occured
        message -- Explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
