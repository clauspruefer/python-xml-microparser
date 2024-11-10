# ]*[ --------------------------------------------------------------------- ]*[
#  .                     XML Microparser Python Module                       .
# ]*[ --------------------------------------------------------------------- ]*[
#  .                                                                         .
#  .  Copyright Claus Prüfer 2016-2024                                       .
#  .                                                                         .
#  .  Lightweight XML Parser and JSON Transformer Module                     .
#  .                                                                         .
# ]*[ --------------------------------------------------------------------- ]*[

import re
import json
import logging

from xmlmicroparser.transformer import JSONTransformer
from xmlmicroparser.helper import Looper


class Parser():
    """ XML MicroParser class.

    Parses simple raw XML data not including DTD or XSLT model description.
    This data has to be ommitted and would lead to misbehaviour when provided.
    Also XML namespace parsing is not supported.

    The XML will be transformed to internal JSON structs which can easily be
    iterated over or printed out.

    Actually all lines **MUST** end with a "\\\\n" otherwise input will be
    treated as a single line and tag closings will not be recognized correctly.

    See :doc:`examples` section for valid input, generated output and supported
    features.

    Processing flow:

    - Process xml input data line by line (add to internal processing list).
    - Setup Element() instances for each found element in list, add properties.
    - Add elements to Parser._elements list.
    - Run Serializer (add/link child elements in OOP based manner).
    - Easily iterate (automatically recursive) over the given result elements.

    Class Inheritance/Dependencies:

    - microparser.Element->microparser.Serializer->transformer.JSONTransformer

    The microparser.Serializer class provides members/methods for recursive
    transformation processing for different transformer module/class types.

    Actually only xml transformation is provided, the transformer module is
    built for future expansion (add multiple formats, e.g. yaml or else).
    """

    def __init__(self, payload):
        """
        :param str payload: xml payload data
        :ivar list[Element] _elements: runtime xml item object storage
        :ivar Element _current_element: current processed element
        :ivar int _current_line_nr: current processed source line number
        :ivar int _current_item_id: current processed numerical internal xml item id
        :example:

        >>> import microparser
        >>>
        >>> payload = '' \\
        >>>     '<tag1>\\n' \\
        >>>     '    <tag2 a="1" b="value1">\\n' \\
        >>>     '        <tag3 b="1" c="value2">value3</tag3>\\n' \\
        >>>     '    </tag2>\\n' \\
        >>>     '</tag1>\\n'
        >>>
        >>> parser = microparser.Parser(payload)
        >>>
        >>> parser.build_serializer()
        >>> parser.process_json()
        >>>
        >>> r1 = parser.get_root_element().get_json_dict()
        >>> r2 = parser.get_element_by_name('tag2').get_json_dict()
        >>> r3 = parser.get_element_by_id(2).get_json_dict()
        >>>
        >>> print(r1)
        >>> print(r2)
        >>> print(r3)
        """

        self.logger = logging.getLogger(__name__)

        self._elements = []
        self._current_element = None
        self._current_line_nr = self._current_line_nr_gen()
        self._current_item_id = self._current_item_id_gen()

        args = {
            'payload': payload.split('\n'),
            'function': self._parse_line,
            'methods': ['strip']
        }

        Looper(**args).process()

    def __repr__(self):
        return str(self.get_elements())

    def build_serializer(self):
        """ Build hierarchical serializer by adding all found elements
        starting with root element.
        """
        self._add_child_elements_recursive(self.get_root_element())

    def get_element_by_id(self, id):
        """ Get element by internal numerical id.

        :param int id: internal numerical element id
        :return: found element
        :rtype: Element or None
        """
        for element in self._elements:
            if element.get_id() == id:
                return element

    def get_element_by_name(self, name):
        """ Get element by xml element id.

        :param str element: xml tag id
        :return: found element
        :rtype: Element or None
        """
        for element in self._elements:
            if element.get_name() == name:
                return element

    def get_elements(self):
        """ Return processed elements list.

        :return: processed elements
        :rtype: list[Element] self._elements
        """
        return self._elements

    def get_root_element(self):
        """ Return root element.

        :return: root element
        :rtype: self._elements[0]
        """
        return self._elements[0]

    def get_child_elements_by_id(self, id):
        """ Return elements children searched by element numerical id.

        :param int id: element internal numerical id
        :yield: found item
        :rtype: elements (list of objects) or None
        """
        for item in self._elements:
            if item.get_parent_id() == id:
                yield item

    def get_child_element(self, name):
        """ Return elements children searched by element name.

        :param string name: element tag name
        :yield: found item
        :rtype: element or None
        """
        for item in self._elements:
            r_name = item.get_name()
            if r_name == name:
                yield item

    def process_json(self):
        """ Process json transformation.
        """

        root_element = self.get_root_element()

        while root_element.get_child_element_count() > 0:
            process_ids = []
            for element in root_element.iterate():
                if element.get_child_element_count() == 0:
                    process_ids.append(element.get_id())

            for id in process_ids:
                root_element.get_element_by_element_id(id).json_transform()

        root_element.set_json_attributes()

    def dump(self):
        """ Send self (__repr__) to logger (debug)
        """
        self.logger.debug(self)

    def _parse_attributes(self, attributes):
        """ Parse attribute var/value keypairs from string and add to
        current processed element item.

        :param str attributes: tag attributes unparsed string
        """

        var_value_pairs = attributes.split()

        self.logger.debug('attributes:{} pairs:{}'.format(attributes, var_value_pairs))

        for var_value_pair in var_value_pairs:
            (var, separator, value) = var_value_pair.partition('=')
            value = value.replace('"', '')
            self._current_element.add_attribute(var, value)

    def _get_last_unclosed_element_id(self):
        """ Get last unprocessed/unclosed element id.

        :return: last non closed element numerical id
        :rtype: int or None
        """
        unclosed_items = []
        for item in self._elements:
            if item.get_line_end() is None:
                unclosed_items.append(item)

        return unclosed_items[-1].get_id() if len(unclosed_items) > 0 else None

    def _add_child_elements_recursive(self, element):
        """ Add child elements recursive.

        :param Element element: xlm start element
        """

        element_id = element.get_id()

        element.set_parent_element(
            self.get_root_element().get_element_by_element_id(
                element.get_parent_id()
            )
        )

        for child_element in self.get_child_elements_by_id(element_id):
            element.add_child_element(child_element)
            self._add_child_elements_recursive(child_element)

    def _current_line_nr_gen(self):
        """ Current line number generator. Simple iterator.
        Start value 0, incremented by 1 (while True).

        :rtype: Iterator[int]
        """
        line_nr = -1
        while True:
            line_nr += 1
            yield line_nr

    def _current_item_id_gen(self):
        """ Current item id generator. Simple iterator.
        Start value 1, incremented by 1 (while True).

        :rtype: Iterator[int]
        """
        id = 0
        while True:
            id += 1
            yield id

    def _parse_line(self, line):
        """ Parse single xml data line.
        """

        line_nr = self._current_line_nr.__next__()

        self.logger.debug('processing line_nr:{}'.format(line_nr))

        try:

            element_id = re.compile("^<([a-zA-Z0-9]+) *").search(line).group(1)
            attributes_start_pos = len(element_id)+1
            attributes_end_pos = line.find(">")
            attributes = line[attributes_start_pos:attributes_end_pos]

            args = {
                'name': element_id,
                'id': self._current_item_id.__next__(),
                'line_nr': line_nr,
                'parent_id': self._get_last_unclosed_element_id()
            }

            self._current_element = Element(**args)
            self._parse_attributes(attributes)
            self._elements.append(self._current_element)

            line = line[attributes_end_pos+1:]

        except AttributeError:
            element_id = None

        try:

            end_tag = re.compile("</(.+)>$").search(line).group(1)
            last_element_id = self._get_last_unclosed_element_id()

            self.get_element_by_id(last_element_id).set_line_end(line_nr)

            self.logger.debug('last_element_id:{} line_nr:{}'.format(
                    last_element_id,
                    line_nr
                )
            )

            len_end_tag = len(end_tag)+3
            line = line[:-len_end_tag]

        except AttributeError:
            end_tag = None

        if element_id and end_tag and len(line) > 0:
            self._current_element.add_content(line)


class Serializer(JSONTransformer):
    """ Serializer class.

    Provides methods for element dependency handling. 

    #TODO:
    This class should be (syntactically correct) moved to own "xml" module
    (xml.Element.Serializer).
    """

    def __init__(self):
        """ Elements hierarchical connector.
        """
        self._clear_child_elements()

        super().__init__()

    def __iter__(self):
        """ Overloaded iterator.

        Will be called on 'yield self', iterate() method makes it recursive.

        :return: iter(list[Element])
        :rtype: iterator
        """
        return iter(self._child_elements)

    def _clear_child_elements(self):
        """ Reset self._child_elements list.
        """
        self._child_elements = []

    def _remove_child_element(self, index):
        """ Remove_element from child_elements list.

        :param int index: child element list position (index)
        """
        del self._child_elements[index]

    def add_child_element(self, element):
        """ Append object to self._child_elements list.

        :param Element element: append element
        """
        self._child_elements.append(element)

    def get_child_elements(self):
        """ Get child elements..

        :return: child elements list
        :rtype: list[Element]
        """
        return self._child_elements

    def iterate(self):
        """ Recursive iterate through hierarchical objects.
        """
        yield self
        for x in self:
            for y in x.iterate():
                yield y

    def get_child_element_count(self):
        """ Return child element count.

        :return: actual child element count
        :rtype: int
        """
        return len(self._child_elements)

    def get_element_by_element_id(self, element_id):
        """ Get element by element numerical id.

        :return: found element
        :rtype: Element or None
        """
        for element in self.iterate():
            if element.get_id() == element_id:
                return element

    def get_element_by_element_name(self, element_name):
        """ Get element by element numerical id.

        :return: found element
        :rtype: Element or None
        """
        for element in self.iterate():
            if element.get_name() == element_name:
                return element


class Element(Serializer):
    """ XML Element container class.

    Provides methods for xml parsing. Inherits from Serializer class.
    As well hierarchical assignment by parent element/numerical id is
    part of this class.

    #TODO:
    This class should be (syntactically correct) moved to own "xml" module
    (xml.Element).
    """

    def __init__(self, *, name, id, line_nr, parent_id):
        """
        :param str name: xml element name (id)
        :param int id: xml element internal processing id
        :param int line_nr: line number of found xml opening tag in payload data
        :param int parent_id: parent element numerical id
        :ivar str _name: xml element id
        :ivar int _id: internal numerical element id
        :ivar int _parent_id: internal numerical parent id (self._id reference)
        :ivar dict[str] _attributes: xml tag attributes var/value pairs
        :ivar str _content: tag inner content (if no sub elements found)
        :ivar int _line_start: start line of found xml opening tag
        :ivar int _line_end: end line of found xml closing tag
        """

        assert isinstance(name, str), 'name must be string type'
        assert isinstance(id, int), 'id must be int type'
        assert isinstance(line_nr, int), 'id must be int type'

        if parent_id is not None:
            assert isinstance(parent_id, int), 'parent_id must be int type'

        self._name = name
        self._id = id
        self._parent_id = parent_id
        self._parent_element = None
        self._attributes = {}
        self._content = ''
        self._line_start = line_nr
        self._line_end = None

        super().__init__()

    def __repr__(self):
        return 'name:{} id:{} p_id:{} attr:{} content:{} l_start:{} l_end:{} json:{}'.format(
            self._name,
            self._id,
            self._parent_id,
            self._attributes,
            self._content,
            self._line_start,
            self._line_end,
            self._json
        )

    def add_attribute(self, name, value):
        """ Add attribute/value pair to self._attributes dictionary.

        :param str name: attribute name
        :param str value: attribute value
        """

        self._attributes[name] = value

    def add_content(self, content):
        """ Add content (value found between xml opening and closing tag) to
        self._content.

        :param str content: tag value
        """
        self._content = '{}{}'.format(self._content, content)

    def set_line_end(self, line_nr):
        """ Set line end (tag found at line nr. in payload)

        :param int line_nr: line number
        """
        self._line_end = line_nr

    def set_parent_element(self, element):
        """ Set parent element.

        :param Element element: parent element
        """
        self._parent_element = element

    def get_id(self):
        """ Get numerical element id.

        :return: internal numerical id
        :rtype: int
        """
        return self._id

    def get_parent_id(self):
        """ Get numerical id of elements parent.

        :return: internal numerical parent id
        :rtype: int
        """
        return self._parent_id

    def get_parent_element(self):
        """ Get parent element.

        :return: parent element
        :rtype: Element
        """
        return self._parent_element

    def get_name(self):
        """ Get element name.

        :return: element xml id
        :rtype: str
        """
        return self._name

    def get_content(self):
        """ Get content.

        :return: content (value found between xml opening and closing tag)
        :rtype: str
        """
        return self._content

    def get_line_start(self):
        """ Get line number of found start tag.

        :return: get line number of found start tag
        :rtype: int
        """
        return self._line_start

    def get_line_end(self):
        """ Get line number of found end tag.

        :return: get line number of found end tag
        :rtype: int
        """
        return self._line_end

    def get_attribute_by_name(self, name):
        """ Get attribute value by given attribute name.

        :return: attribute value
        :rtype: str
        """
        if name in self._attributes:
            return self._attributes[name]

    def get_attributes(self):
        """ Get attributes.

        :return: attributes dictionary
        :rtype: dict
        """
        return self._attributes
