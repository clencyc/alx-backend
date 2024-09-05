#!/usr/bin/python3
"""
FIFO caching
"""


class FIFOCache:
    """ FIFO cache class """
    def __init__(self):
        """ constructor """
        self.cache_data = {}
    
    def put(self, key, item):
        """ method to store data in cache """
        if key is None or item is None:
            return
        if len(self.cache_data) >= 4:
            keys = list(self.cache_data.keys())
            first = keys[0]
            self.cache_data.pop(first)
            print("DISCARD: {}".format(first))
        self.cache_data[key] = item
    
    def get(self, key):
        """ method to get data in cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]