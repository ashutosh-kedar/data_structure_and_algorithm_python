from collections import OrderedDict


class LRU_Cache:

    def __init__(self,max_size):
        self.max_size = max_size
        self.ordered_dict = OrderedDict()
        
        

    def get(self,key):
        if key not in self.ordered_dict.keys():
            return -1

        self.ordered_dict.move_to_end(key)
        return self.ordered_dict.get(key,-1)


    def put(self,key,value):
        if key in self.ordered_dict.keys():
            self.ordered_dict.move_to_end(key)
            
        self.ordered_dict[key] = value

        
        while len(self.ordered_dict) > self.max_size:
            self.ordered_dict.popitem(last=False)

        return


c = LRU_Cache(2)
c.put(1, 1)
c.put(2, 2)
print(c.get(1))
c.put(3, 3)
print(c.get(2))

        
