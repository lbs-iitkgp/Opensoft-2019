from collections import deque

from utility import distance_function

class BKTree:
    def __init__(self, items_list = [], items_dict = {}):
        self.tree = None
        
        _add = self.add
        
        for item in items_list:
            _add(item)
        
        for item in items_dict:
            _add(item)
    
    def add(self, item):
        node = self.tree
        
        if node is None:
            self.tree = (item, {})
            return
        
        while True:                              ## for a single distance i.e. for each corresponding distance 1, 2, 3, etc., have only one item 
            parent, children = node
            dist = distance_function(item, parent)
            node = children.get(dist)
            if node is None:
                children[dist] = (item, {})
                break
    
    def find(self, item, n):
        if self.tree is None:
            return []
        
        candidates = deque([self.tree])
        found = []
        
        while candidates:
            candidate, children = candidates.popleft()
            dist = distance_function(item, candidate)
            if dist <= n:
                found.append((dist, candidate))
            
            if children:                          ##??
            	## check for range [d-n, d+n)
                lower = dist - n   
                upper = dist + n
                candidates.extend(c for d, c in children.items() if abs(lower) <= d < upper)

        found.sort()
        return found
    
    def __iter__(self):
        if self.tree is None:
            return
        
        candidates = deque([self.tree])
        
        while candidates:
            candidate, children = candidates.popleft()
            yield candidate
            candidates.extend(children.values())