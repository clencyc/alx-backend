#!/usr/bin/python3
"""
LFU caching module.
This module contains the LFUCache class which implements
a Least Frequently Used (LFU) caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching

class LFUCache(BaseCaching):
    """ LFU cache class.
    
    Inherits from BaseCaching and implements a caching system
    where the least frequently used items are discarded first when
    the cache reaches its maximum capacity.
    """
    
    def __init__(self):
        """ Initialize the LFUCache.
        
        Initializes the cache data from the parent class and
        additional structures to keep track of the order of keys
        and their access frequencies.
        """
        super().__init__()
        self.keys = []
        self.freq = {}

    def put(self, key, item):
        """ Add an item to the cache.
        
        If the cache is at its maximum capacity, it discards the
        least frequently used item before adding the new item.
        
        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
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
        """ Retrieve an item from the cache.
        
        Increments the access frequency of the accessed item.
        
        Args:
            key: The key of the item to retrieve.
        
        Returns:
            The item associated with the key, or None if the key
            is not in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        self.freq[key] += 1
        return self.cache_data[key]
