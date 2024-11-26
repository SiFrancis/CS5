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

c1, c2, c3 = Column(), Column(), Column()            
columns = [c1, c2, c3]
steps = 0

def transfer(n, colFrom, colTo):
    if n:
        colTo.push(colFrom.peek())
        colFrom.pop()

def view():
    for col in columns:
        print(col.items)
    print(False not in [col.isValid() for col in columns])
    print()

def algo(n, startCol, endCol):
    global steps
    cols_list = columns.copy()
    cols_list.remove(startCol)
    cols_list.remove(endCol)
    otherCol = cols_list[0]
    if n == 1:
        transfer(n, startCol, endCol)
        steps += 1
        print(f'Step {steps}')
        view()
    elif n > 1:
        algo(n-1, startCol, otherCol)
        transfer(n, startCol, endCol)
        steps += 1
        print(f'Step {steps}')
        view()
        algo(n-1, otherCol, endCol)

def main():
    discs_num = 20
    for i in reversed(range(discs_num)):
        c1.push(i+1)
    print("START:")
    view()
    algo(discs_num, c1, c3)
    print("END:")
    view()
    print()
    print(steps)

if __name__ == "__main__": main()