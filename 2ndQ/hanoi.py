class Column:
    # Column is a type of stack
    
    # default stack operations
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def copyFrom(self, target):
        self.items = target.items
    
    # custom operations for column
    def isValid(self):
        valid = True
        for idx, val in enumerate(self.items[:-1]):
            if val < self.items[idx+1]: valid = False
        return valid
            

def transfer(colFrom, colTo):
    colTo.push(colFrom.peek())
    colFrom.pop()

def view(*cols):
    for col in cols: print(col.items)

c1 = Column()
c1.push(4)
# c1.push(3)
c1.push(2)
c1.push(1)
c2, c3 = Column(), Column()

transfer(c1, c3)

view(c1, c2, c3)