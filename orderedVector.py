import numpy

class OrderedVector:
    def __init__(self,size):
        self.size = size
        self.last_position = -1
        self.valors = numpy.empty(self.size,dtype= object)

    def insert(self,adj):
        if self.last_position == self.size - 1:
            print("Full vector!")
            return
        pos = 0
        for i in range(self.last_position + 1):
            pos = i
            if self.valors[i].astar_distance > adj.astar_distance:
                break
            if i == self.last_position:
                pos = i + 1

        x = self.last_position
        while x >= pos:
            self.valors[x + 1] = self.valors[x]
            x-=1
        
        self.valors[pos] = adj
        self.last_position += 1


