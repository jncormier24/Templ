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
	padding = 0 # How many tabs to add to the line beginning; used in formatting
	text = ""
    child_elements = {}

    
    def __init__(self, name, text = "", attributes = {}, padding = 0):
        self.name = name
        self.text = text
        self.attributes = attributes
        self.padding = padding

class BlockHtmlTag(HtmlTag):

    """Object representation of a block-level HTML tag."""

    _valid_tags = (
        "article", "aside", "blockquote", "body", "br", "button",
        "canvas", "caption", "col", "colgroup", "dd", "div", "dl", "dt",
        "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1-6",
        "header", "hgroup", "hr", "li", "map", "object", "ol", "output", "p",
        "pre", "progress", "section", "table", "tbody", "textarea", "tfoot",
        "th", "tr", "ul", "video"
    )

    def validate(self):
        if self.name in _valid_tags:
            return True
        else:
            pass
