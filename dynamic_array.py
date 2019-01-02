import ctypes

class DynamicArray(object):
    
    def __init__(self):
        
        self.n = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)


    def __len__(self):
        
        return self.n


    def __getitem__(self, k):
        
        if not 0 <= k < self.n:
            return IndexError('K is outof bounds')
            
        return self.array[k]


    def append(self, el):
        
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.n] = el
        self.n += 1


    def _resize(self, new_capacity):
        
        new_array = self.make_array(new_capacity)

        for k in range(self.n):
            new_array[k] = self.array[k]

        self.array = new_array

        self.capacity = new_capacity


    def make_array(self, new_capacity):
        
        return (new_capacity * ctypes.py_object)()

