import numpy as np
import time

class MyArray:
    def __init__(self, lista=None):
        if lista is None:
            self.n = 0
            self.capacidade = 1
            self.array = np.empty(self.capacidade, dtype=object)
        else:
            self.n = len(lista)
            self.capacidade = len(lista)
            self.array = np.array(lista, dtype=object)

    def __str__(self):
        return "[" + ", ".join(repr(self.array[i]) for i in range(self.n)) + "]"

    def __len__(self):
        return self.n
    
    def _resize(self, new_cap):
        new_array = np.empty(new_cap, dtype=object)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacidade = new_cap

    def __getitem__(self, index):
        index = index % self.n 
        return self.array[index]

    def append(self, item):
        if self.n == self.capacidade:
            self._resize(2 * self.capacidade)
        self.array[self.n] = item
        self.n += 1

    def pop(self):
        item = self.array[self.n - 1]
        self.array[self.n - 1] = None
        self.n -= 1
        return item
    

my_array = MyArray([1, 2, 3])
print(my_array)
my_array.append(4)
print(my_array)
print(my_array.pop())
print(my_array)
