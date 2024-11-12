# -*- coding: utf8 -*-

import pytest
import logging
import microparser


class TestElement():

    def test_attribute_add_valid_types(self, caplog):

        caplog.set_level(logging.DEBUG)

        e = microparser.Element(
            name = 'element1',
            id = 1,
            line_nr = 1,
            parent_id = None
        )

        e = microparser.Element(
            name = 'element2',
            id = 100,
            line_nr = 10,
            parent_id = 10
        )

    def test_attribute_add_invalid_types(self, caplog):

        caplog.set_level(logging.DEBUG)

        with pytest.raises(AssertionError):
            e = microparser.Element(
                name = 1,
                id = 1,
                line_nr = 1,
                parent_id = None
            )

        with pytest.raises(AssertionError):
            e = microparser.Element(
                name = 'element',
                id = 'name',
                line_nr = 1,
                parent_id = None
            )

        with pytest.raises(AssertionError):
            e = microparser.Element(
                name = 'element',
                id = 1,
                line_nr = {},
                parent_id = None
            )

        with pytest.raises(AssertionError):
            e = microparser.Element(
                name = None,
                id = 1,
                line_nr = 1,
                parent_id = 10
            )

        with pytest.raises(AssertionError):
            e = microparser.Element(
                name = 'element',
                id = 1,
                line_nr = 1,
                parent_id = 'test'
            )

    def test_get_element_by_id(self, caplog):

        caplog.set_level(logging.DEBUG)

        p = microparser.Parser('')

        p._elements.append(
            microparser.Element(
                name = 'element1',
                id = 101,
                line_nr = 100,
                parent_id = None
            )
        )

        p._elements.append(
            microparser.Element(
                name = 'element2',
                id = 210,
                line_nr = 101,
                parent_id = 101
            )
        )

        p._elements.append(
            microparser.Element(
                name = 'element3',
                id = 28,
                line_nr = 200,
                parent_id = 101
            )
        )

        r = p.get_element_by_id(210)

        assert r._id == 210
        assert r._name == 'element2'
        assert r._parent_id == 101
