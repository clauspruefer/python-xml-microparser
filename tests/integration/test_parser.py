# -*- coding: utf8 -*-

import pytest
import logging
import microparser


def check_element(element, properties):
    assert element._id == properties['id']
    assert element._name == properties['name']
    assert element._attributes == properties['attributes']
    assert element._parent_id == properties['parent_id']
    assert element._content == properties['content']
    assert element._line_start == properties['line_start']
    assert element._line_end == properties['line_end']


class TestParser():

    def test_basic_parsing(self, caplog):

        caplog.set_level(logging.DEBUG)

        payload = '' \
            '<outertag test1="string1" test2="string2">\n' \
            '   <innertag1>\n' \
            '       <innertag2>value</innertag2>\n' \
            '   </innertag1>\n' \
            '</outertag>\n'

        p = microparser.Parser(payload)

        elements = p.get_elements()

        props1 = {
            'id': 1,
            'name': 'outertag',
            'attributes': {'test1': 'string1', 'test2': 'string2'},
            'parent_id': None,
            'content': '',
            'line_start': 0,
            'line_end': 4,
        }

        check_element(elements[0], props1)

        props2 = {
            'id': 2,
            'name': 'innertag1',
            'attributes': {},
            'parent_id': 1,
            'content': '',
            'line_start': 1,
            'line_end': 3,
        }

        check_element(elements[1], props2)

        props3 = {
            'id': 3,
            'name': 'innertag2',
            'attributes': {},
            'parent_id': 2,
            'content': 'value',
            'line_start': 2,
            'line_end': 2,
        }

        check_element(elements[2], props3)


class TestJSONTransformer():

    def test_json_basic_transform(self, caplog):

        caplog.set_level(logging.DEBUG)

        payload = '' \
            '<outertag test1="string1" test2="string2">\n' \
            '   <innertag1>\n' \
            '       <innertag2 test3="string3">\n' \
            '           <innertag3>value1</innertag3>\n' \
            '           <innertag4>value2</innertag4>\n' \
            '           <innertag5>\n' \
            '               <property>value1</property>\n' \
            '               <property>value2</property>\n' \
            '           </innertag5>\n' \
            '       </innertag2>\n' \
            '   </innertag1>\n' \
            '   <innertag1a>\n' \
            '       <innertag2a test3="string3">\n' \
            '           <innertag3a>value1</innertag3a>\n' \
            '           <innertag4a>value2</innertag4a>\n' \
            '           <innertag5a>\n' \
            '               <property>value1</property>\n' \
            '               <property>value2</property>\n' \
            '           </innertag5a>\n' \
            '       </innertag2a>\n' \
            '   </innertag1a>\n' \
            '</outertag>\n'

        p = microparser.Parser(payload)
        p.build_serializer()
        p.process_json()
        result_dict = p.get_root_element().get_element_by_element_id(1).get_json_dict()

        expected_dict = {
            "outertag": {
                "innertag1": {
                    "innertag2": {
                            "innertag3": "value1",
                            "innertag4": "value2",
                            "innertag5": {
                                "property": [
                                    "value1",
                                    "value2"
                                ],
                                "attributes": {}
                            },
                            "attributes": {
                                "test3": "string3"
                            }
                    },
                    "attributes": {}
                },
                "innertag1a": {
                    "innertag2a": {
                            "innertag3a": "value1",
                            "innertag4a": "value2",
                            "innertag5a": {
                                "property": [
                                    "value1",
                                    "value2"
                                ],
                                "attributes": {}
                            },
                            "attributes": {
                                "test3": "string3"
                            }
                    },
                    "attributes": {}
                },
                "attributes": {
                    "test1": "string1",
                    "test2": "string2"
                }
            }
        }

        assert result_dict == expected_dict

    def test_json_transform_nested_identic_tags(self, caplog):

        caplog.set_level(logging.DEBUG)

        payload = '' \
            '<outertag>\n' \
            '   <innertag>\n' \
            '       <innertag2>\n' \
            '           <property>value1</property>\n' \
            '           <property>value2</property>\n' \
            '       </innertag2>\n' \
            '       <innertag2>\n' \
            '           <property>value3</property>\n' \
            '           <property>value4</property>\n' \
            '       </innertag2>\n' \
            '       <innertag2>\n' \
            '           <property>value5</property>\n' \
            '           <property>value6</property>\n' \
            '       </innertag2>\n' \
            '   </innertag>\n' \
            '</outertag>\n'

        p = microparser.Parser(payload)
        p.build_serializer()
        p.process_json()
        result_dict = p.get_root_element().get_element_by_element_id(1).get_json_dict()

        expected_dict = {
            "outertag": {
                "innertag": {
                    "innertag2": [
                            {
                                "property": [
                                    "value1",
                                    "value2"
                                ],
                                "attributes": {}
                            },
                            {
                                "property": [
                                    "value3",
                                    "value4"
                                ],
                                "attributes": {}
                            },
                            {
                                "property": [
                                    "value5",
                                    "value6"
                                ],
                                "attributes": {}
                            }
                    ],
                    "attributes": {}
                },
                "attributes": {}
            }
        }

        assert result_dict == expected_dict
