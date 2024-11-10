# ]*[ --------------------------------------------------------------------- ]*[
#  .                     XML Microparser Python Module                       .
# ]*[ --------------------------------------------------------------------- ]*[
#  .                                                                         .
#  .  Copyright Claus Prüfer 2016-2024                                       .
#  .                                                                         .
#  .  XML Parser JSON Transformer Module                                     .
#  .                                                                         .
# ]*[ --------------------------------------------------------------------- ]*[

import json
import logging


class JSONTransformer():
    """ JSON transformer class.

    Transforms given JSON (text) data into XML format. Data in the first
    step will be transformed to internal JSON structs and afterwards converted
    (recursive) to xml.

    This class will be inherited by the microparser.Serializer class which
    provides base members/methods for recursive transformation processing.
    .
    """

    def __init__(self):
        """ Builds json from serialized (connected) Element object hierarchy.
        """
        self.logger = logging.getLogger(__name__)
        self._json = {}

    def json_transform(self):
        """ Transform xml elements to python dictionary.
        """

        self.set_json_attributes()
        self._set_json_value()

        parent_element = self.get_parent_element()

        parent_element._set_json_attribute(
            self.get_name(),
            self.get_json_dict()[self.get_name()]
        )

        parent_element._remove_child_element(0)

    def set_json_attributes(self):
        """ Set json attributes.
        """
        xml_id = self.get_name()
        if xml_id not in self._json:
            self._json[xml_id] = {}
        self._json[xml_id]['attributes'] = {}
        for key, value in self.get_attributes().items():
            self._json[xml_id]['attributes'][key] = value
        self.logger.debug('element_id:{} json:{}'.format(xml_id, self._json))

    def _set_json_value(self):
        """ Set json value.
        """
        value = self.get_content()
        if len(value) > 0:
            self._json[self.get_name()] = value

    def _set_json_attribute(self, key, value):
        """ Set single json attribute.

        :param str key: attribute key
        :param mixed value: attribute value (str or dict)
        """
        xml_id = self.get_name()
        self.logger.debug('xml_id:{} key:{} value:{}'.format(xml_id, key, value))
        if xml_id not in self._json:
            self._json[xml_id] = {}
        if key in self._json[xml_id] and isinstance(self._json[xml_id][key], list):
            self._json[xml_id][key].append(value)
        elif key in self._json[xml_id]:
            oldvalue = self._json[xml_id][key]
            self._json[xml_id][key] = []
            self._json[xml_id][key].append(oldvalue)
            self._json[xml_id][key].append(value)
        else:
            self.logger.debug('else')
            self._json[xml_id][key] = value

    def get_json_dict(self):
        """ Return internal json dictionary.

        :return: json result dictionary
        :rtype: dict
        """
        return self._json

    def get_json(self):
        """ Return json result.

        :return: json result dictionary (json dumped)
        :rtype: str
        """
        return json.dumps(self._json)
