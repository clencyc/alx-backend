#!/usr/bin/env python3
""" Basic caching techniques """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache task """
    def put(self, key, item):
        """ method to store data in cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ method to get data in cache """
        if key is None:
            return
        return self.cache_data.get(key)
