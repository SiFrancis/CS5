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
        pass
    
    def insert(self, item):
        self.heap_list.append(item)
        self.upheap()
        