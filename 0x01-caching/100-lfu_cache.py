#!/usr/bin/python3
"""
LFU caching
"""

BaseCaching = __import__('base_caching').BaseCaching

class LFUCache(BaseCaching):
    """ LFU cache class """
    def __init__(self):
        """ constructor """
        super().__init__()
        self.keys = []
        self.freq = {}

    def put(self, key, item):
        """ method to store data in cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
            self.freq[key] += 1
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq.values())
            for k, v in self.freq.items():
                if v == min_freq:
                    break
            del self.cache_data[k]
            del self.freq[k]
            self.keys.remove(k)
            print("DISCARD: {}".format(k))

        self.cache_data[key] = item
        self.keys.append(key)
        self.freq[key] = 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        self.freq[key] += 1
        return self.cache_data[key]
