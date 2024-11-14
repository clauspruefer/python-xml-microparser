.. examples

========
Examples
========

The following examples and use cases show how to cope with the XML parser.

.. warning::

    Ech line **MUST** end with a "**\\\\n**", otherwise expect undefined behaviour!

.. note::

    **Loop over results** shows how to efficiently use XML data as configuration
    method for your projects.

Use complete XML
================

Transform the complete XML to internal dict/JSON.

.. code-block:: python

    import microparser

    payload = """
        <tag1>\n
            <tag2 a="1" b="value1">\n
                <tag3 c="2" d="value2">value3</tag3>\n
            </tag2>\n
        </tag1>"""

    parser = microparser.Parser(payload)

    parser.build_serializer()
    parser.process_json()

    r = parser.get_root_element().get_json_dict()

    print(r)

Output (Printed Representation)

.. code-block:: python

    {'tag1': {'tag2': {'tag3': 'value3', 'attributes': {'a': '1', 'b': 'value1'}}, 'attributes': {}}}

Get element by name
===================

Get element value by name (if unique).

.. code-block:: python

    import microparser

    payload = """
        <tag1>\n
            <tag2 a="1" b="value1">\n
                <tag3 c="2" d="value2">value3</tag3>\n
            </tag2>\n
        </tag1>"""

    parser = microparser.Parser(payload)

    parser.build_serializer()
    parser.process_json()

    r = parser.get_element_by_name('tag2').get_json_dict()

    print(r)

Output (Printed Representation)

.. code-block:: python

    {'tag2': {'tag3': 'value3', 'attributes': {'a': '1', 'b': 'value1'}}}

Get element by id
=================

Get element value by id.

.. code-block:: python

    import microparser

    payload = """
        <tag1>\n
            <tag2 a="1" b="value1">\n
                <tag3 c="2" d="value2">value3</tag3>\n
            </tag2>\n
        </tag1>\n"""

    parser = microparser.Parser(payload)

    parser.build_serializer()
    parser.process_json()

    r = parser.get_element_by_id('tag2').get_json_dict()

    print(r)

Duplicate elements (same name)
==============================

Duplicate elements can be used to process multiple configuration items
(e.g. a webserver configuration with multiple virtual hosts).

.. note::

    If element is duplicate, it will be appended (order retained) to an
    internal list (see result dict and **Loop over results** to see how to
    loop over.

.. note::

    You also can add nested elements to group your vhost configuration,
    examples will be added in next realeases.

.. code-block:: python

    import microparser

    payload = """
        <config>\n
            <vhosts\n
                <vhost name="vhost1" prop1="value1"></vhost>\n
                <vhost name="vhost2" prop1="value2"></vhost>\n
                <vhost name="vhost3" prop1="value3"></vhost>\n
            </vhosts>\n
        </config>\n"""

    parser = microparser.Parser(payload)

    parser.build_serializer()
    parser.process_json()

    r = parser.get_root_element().get_json_dict()

    print(r)

Output (Printed Representation)

.. code-block:: python

    {'config': 
        {'vhosts':
            {
                'vhost': [
                    {'vhost': {'attributes': {'name': 'vhost1', 'prop1': 'value1'}}, 'attributes': {}},
                    {'vhost': {'attributes': {'name': 'vhost2', 'prop1': 'value2'}}, 'attributes': {}},
                    {'vhost': {'attributes': {'name': 'vhost3', 'prop1': 'value3'}}, 'attributes': {}}
                ],
                'attributes': {}
            },
            'attributes': {}
        }
    }

Loop over results
=================

To loop over the results (for each vhost) from the previous example, do the
following:

.. code-block:: python

    parser = microparser.Parser(payload)

    parser.build_serializer()
    parser.process_json()

    r = parser.get_root_element().get_json_dict()

    # note that you have to add the 'vhost' list at the end
    for element in r['config']['vhosts']['vhost']:
        vhost_attributes = element['vhost']['attributes']
        vhost_name = vhost_attributes['name']
        vhost_attribute_prop1 = vhost_attributes['prop1']
