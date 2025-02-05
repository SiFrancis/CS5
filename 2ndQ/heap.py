class BinaryMinHeap:
    def __init__ (self):
        self.heap_list = [0]
        self.size = len(self.heap_list) - 1
        
    def upheap(self, idx=self.size):
        while idx // 2 > 0:
            child = self.heap_list[i]
            parent = self.heap_list[i//2]
            if child > parent:
                child, parent = parent, child
            idx //= 2
    
    def downheap(self, idx):
        while idx * 2 <= self.size:
            parent = self.heap_list[i]
            min_child = min(self.heap_list[i*2], self.heap_list[i*2+1])
            parent, min_child = min_child, parent
        idx = self.heap_list.index(min_child)
    
    def insert(self, item):
        self.heap_list.append(item)
        self.upheap()
        
    def extract(self, item):
        pass
        