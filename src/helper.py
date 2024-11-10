# ]*[ --------------------------------------------------------------------- ]*[
#  .                     XML Microparser Python Module                       .
# ]*[ --------------------------------------------------------------------- ]*[
#  .                                                                         .
#  .  Copyright Claus Prüfer 2016-2024                                       .
#  .                                                                         .
#  .  XML Parser Helper classes                                              .
#  .                                                                         .
# ]*[ --------------------------------------------------------------------- ]*[

import logging


class Looper():
    """ Looper Class.

    Provides processing of list of input items (type should be irrelevant,
    actually set to type string) applied to multiple processing method
    references (list).

    After single item has been processed by multiple methods specified in
    methods list (e.g. strip), it will be sent to the final processing function.
    """

    def __init__(self, *, payload, function, methods=None):
        """ Loops over payload items. For each item:

        - applies methods given in methods list.
        - calls function reference given in function argument using item as argument.

        :param list[str] payload: payload list
        :param str function: function reference for item processing after methods processing
        :param list[str] methods: list of methods applied to item
        :ivar list[str] _payload: list of payload items to be processed
        :ivar str _function: stored function reference
        :ivar list[str] _methods: list of methods applied to payload items
        :example:

        >>> from microparser import Looper
        >>>
        >>> def myfunction(payload):
        >>>     print(payload)
        >>>
        >>> payload = 'one,two,three'
        >>>
        >>> args = {
        >>>     'payload': payload.split(','),
        >>>     'function': myfunction,
        >>>     'methods': ['strip']
        >>> }
        >>>
        >>> Looper(**args).process()
        """

        self.logger = logging.getLogger(__name__)

        self._payload = payload
        self._function = function
        self._methods = methods

    def process(self):
        """ Process payload elements.
        """
        for element in self._payload:
            for element in self.generate_methods(element):
                self._function(element)

    def generate_methods(self, element):
        """ Generate methods when provided.
        """
        try:
            yield Looper.process_methods(self._methods, element)
        except TypeError:
            yield element

    @staticmethod
    def process_methods(methods, element):
        """ Loop over methods.
        """
        for method in methods:
            func = getattr(element, method)
            return func()
