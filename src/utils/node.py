"""mode.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""


class Node:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, value, link_node=None):
        """
        __init__ _summary_

        _extended_summary_

        Args:
            value (_type_): _description_
            link_node (_type_, optional): _description_. Defaults to None.
        """
        self.value = value
        self.link_node = link_node

    def set_next_node(self, link_node):
        """
        set_next_node _summary_

        _extended_summary_

        Args:
            link_node (_type_): _description_
        """
        self.link_node = link_node

    def get_next_node(self):
        """
        get_next_node _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return self.link_node

    def get_value(self):
        """
        get_value _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return self.value
