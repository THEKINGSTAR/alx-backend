#!/usr/bin/python3
"""
LFU Caching
"""


from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """put in the cahse function
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None,
        this method should not do anything.
        If the number of items in self.cache_data
        is higher that BaseCaching.MAX_ITEMS:
        you must discard the least frequency used item (LFU algorithm)
        if you find more than 1 item to discard,
        you must use the LRU algorithm to discard
        only the least recently used
        you must print DISCARD:
        with the key discarded and following by a new line
        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            return

        return

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None
        or if the key doesn’t exist in self.cache_data,
        return None.
        Args:
            key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
