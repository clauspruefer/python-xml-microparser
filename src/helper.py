# ]*[ --------------------------------------------------------------------- ]*[
#  .                     XML Microparser Python Module                       .
# ]*[ --------------------------------------------------------------------- ]*[
#  .                                                                         .
#  .  Copyright Claus Prüfer 2016-2024                                       .
#  .                                                                         .
#  .                                                                         .
# ]*[ --------------------------------------------------------------------- ]*[

import logging


class Looper():
    """ Looper Class.
    """

    def __init__(self, *, payload, function, methods=None):
        """ Loops over payload items. For each item:

        - applies methods given in methods list.
        - calls function reference given in function argument using item as argument.

        :param list[str] payload: payload list
        :param str function: function reference
        :param list[str]: list of methods applied to payload items
        :ivar list[str] _payload: payload items to be processed
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
