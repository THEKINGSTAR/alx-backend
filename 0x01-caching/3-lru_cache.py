#!/usr/bin/python3
""" BaseCaching LIFOCache module
"""


from base_caching import BaseCaching
from collections import OrderedDict



class LRUCache(BaseCaching):
    """ BaseCachin defines:
      - caching system
      - where data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        # self.cache_data = {}
        self.cache_data = OrderedDict()


    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS:
                last = self.cache_data.popitem(last=False)
                print(f"DISCARD: {last[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        key_val = self.cache_data[key]
        return (key_val)
