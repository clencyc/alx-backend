#!/usr/bin/python3
"""
LRU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache class """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ method to store data in cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.keys.pop(0)
            del self.cache_data[last]
            print("DISCARD: {}".format(last))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]