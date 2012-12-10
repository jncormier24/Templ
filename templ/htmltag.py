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

class _HtmlTag:
    
    """Object representation of an HTML tag.
    
    A very simple class that encapsulates an HTML tag.

    Attributes:
    name - The name of the HTML tag
    attributes - A dict of the attributes associated with the tag
    text - Any text the tag displays
    padding - How many tabs to pad the tag with; used in formatting
    child_elements - A list of any child elements
    valid_tags - Tuple of valid HTML tags
    
    """

    name = ''
    attributes = {}
    text = ''
    padding = 0 # How many tabs to add to the line beginning; used in formatting
    child_elements = []
    valid_tags = ()

    def validate(self):        
        """Validates the proposed tag to verify it's a valid HTML tag.

        If the HTML tag in question exists in the list of valid tags, then 
        validate returns True, otherwise it returns False.

        Parameters:
        None

        Returns:
        True if valid HTML tag
        False if not valid HTML tag

        """
        if self.name in valid_tags:
            return True
        else:
            return False

    def __init__(self):
        self.name = ''
        self.attributes = {}
        self.text = ''
        self.child_elements = []
        self.valid_tags = ()

        self.void_tags = (
            'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
            'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'
        )
        
    def __str__(self):
        begin_tag = '<' + self.name
        end_tag = '</' + self.name + '>'
        for attribute in self.attributes:
            begin_tag += ' ' + attribute + '="' + self.attributes[attribute]\
                + '"'
        begin_tag += '>'
        
class BlockHtmlTag(_HtmlTag):
    """Object representation of a block-level HTML tag.
    
    Attributes:
    name - The name of the HTML tag
    attributes - A dict of the attributes associated with the tag
    text - Any text the tag displays
    padding - How many tabs to pad the tag with; used in formatting
    child_elements - A list of any child elements
    valid_tags - Tuple of valid HTML tags

    """

    def __init__(self, name, attributes = {}, text = '', padding = 0):
        self.name = name
        self.attributes = attributes
        self.text = text
        self.padding = padding

        self.valid_tags = (
            'article', 'aside', 'blockquote', 'body', 'br', 'button',
            'canvas', 'caption', 'col', 'colgroup', 'dd', 'div', 'dl', 'dt',
            'embed', 'fieldset', 'figcaption', 'figure', 'footer', 'form',
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup', 'hr', 'li',
            'map', 'object', 'ol', 'output', 'p', 'pre', 'progress', 'section',
            'table', 'tbody', 'textarea', 'tfoot', 'th', 'tr', 'ul', 'video'
        )

class InlineHtmlTag(_HtmlTag):
    """Object representation of an inline-level HTML tag.
    
    Attributes:
    name - The name of the HTML tag
    attributes - A dict of the attributes associated with the tag
    text - Any text the tag displays
    padding - How many tabs to pad the tag with; used in formatting
    child_elements - A list of any child elements
    valid_tags - Tuple of valid HTML tags
    
    """

    def __init__(self, name, attributes = {}, text = '', padding = 0):
        self.name = name
        self.attributes = attributes
        self.text = text
        self.padding = padding
        
        self.valid_tags = (
            'a', 'abbr', 'address', 'area', 'audio', 'bm', 'cite', 'code',
            'del', 'details', 'dfn', 'command', 'datalist', 'em', 'font', 'i',
            'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'link',
            'mark', 'meter', 'nav', 'optgroup', 'option', 'q', 'small',
            'select', 'source', 'span', 'strong', 'sub', 'summary', 'sup',
            'tbody', 'td', 'time', 'var'
        )
