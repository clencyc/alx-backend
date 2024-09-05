#!/usr/bin/python3
"""
MRU caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache class.
    
    Inherits from BaseCaching and implements a caching system
    where the most recently used items are discarded first when
    the cache reaches its maximum capacity.
    """
    
    def __init__(self):
        """ Initialize the MRUCache.
        
        Initializes the cache data from the parent class and
        an additional list to keep track of the order of keys.
        """
        super().__init__()
        self.keys = []
    
    def put(self, key, item):
        """ Add an item to the cache.
        
        If the cache is at its maximum capacity, it discards the
        most recently used item before adding the new item.
        
        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = self.keys.pop()
            del self.cache_data[last]
            print("DISCARD: {}".format(last))

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Retrieve an item from the cache.
        
        Moves the accessed item to the end of the tracking list
        to mark it as the most recently used.
        
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
        return self.cache_data[key]
