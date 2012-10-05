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

	name = ""
	attributes = {}
	text = ""
	padding = 0 # How many tabs to add to the line beginning; used in formatting
	child_elements = []
	valid_tags = ()

	def validate(self):
		if self.name in valid_tags:
			return True
		else:
			raise InvalidTagError(self.name, self.name + " is not a valid HTML tag.")

    
class BlockHtmlTag(HtmlTag):

    """Object representation of a block-level HTML tag."""

    valid_tags = (
        "article", "aside", "blockquote", "body", "br", "button",
        "canvas", "caption", "col", "colgroup", "dd", "div", "dl", "dt",
        "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1-6",
        "header", "hgroup", "hr", "li", "map", "object", "ol", "output", "p",
        "pre", "progress", "section", "table", "tbody", "textarea", "tfoot",
        "th", "tr", "ul", "video"
    )

    def __init__(self, name, attributes = {}, text = "", padding = 0):
		super().__init__()

        self.name = name
        self.attributes = attributes
        self.text = text
        self.padding = padding

class InlineHtmlTag(HtmlTag):

	"""Object representation of an inline-level HTML tag."""

	valid_tags = (
		"a", "abbr", "address", "area", "audio", "bm", "cite", "code", "del",
		"details", "dfn", "command", "datalist", "em", "font", "i", "iframe",
		"img", "input", "ins", "kbd", "label", "legend", "link", "mark",
		"meter", "nav", "optgroup", "option", "q", "small", "select", "source",
		"span", "strong", "sub", "summary", "sup", "tbody", "td", "time", "var"
	)

	def __init__(self, name, attributes = {}, text = "", padding = 0):
		super().__init__()

		self.name = name
		self.attributes = attributes
		self.text = text
		self.padding = padding

class InvalidTagError(Exception):
    
    """Error to be raised when given HTML tag isn't valid.
    
    Attributes:
        expression -- The expression in which the error occured
        message -- Explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
