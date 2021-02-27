from heap import *
import math

class k_Heap:
    length = 0
    data = []
    k = 0

    def __init__(self, values, k):
        self.data = values
        self.length = len(values)
        self.k = k
        self.build_heap(values)

    def build_heap(self, values):
        for i in range(self.length // self.k - 1, -1, -1):
            self.sink(i)

    def parent(self, i):
        return (i + (self.k - 1)) // self.k - 1

    def children(self, i):
        children = []
        for c in range(1,self.k+1):
            if(self.k * i + c < self.length):
                children.append(self.k * i + c)
        return children

    def sink(self, i):
        largest_known = i
        for c in self.children(i):
            if(self.data[c] > self.data[largest_known]):
                largest_known = c
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, self.k))
        whitespace = self.k ** height
        s = ""
        for i in range(height):
            for j in range(self.k ** i - 1, min(self.k ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // self.k
        return s

#heap_2 = k_Heap([8,9,7,2,1,5,3,20,10], 2)
#print(heap_2.data)

#heap_3 = k_Heap([8,9,7,2,1,5,3,20,10], 3)
#print(heap_3.data)

#heap_4 = k_Heap([8,9,7,2,1,5,3,20,10], 4)
#print(heap_4.data)