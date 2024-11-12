class Deque():
    # double ended queue
    def __init__(self):
        self.items = []
        
    def __len__(self):
        return len(self.items)
    
    def add_front(self, item):
        self.items.insert(0, item)
    
    def add_rear(self, item):
        self.items.append(item)
        
    def remove_front(self):
        out = self.items[0]
        self.items = self.items[1:]
        return out
    
    def remove_rear(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

def main():
    dq_front, dq_rear = Deque(), Deque()
    inp = str(input("Input: "))
    for char in inp:
        dq_front.add_front(char.lower())
        dq_rear.add_rear(char.lower())
    print("Output:", dq_front.items == dq_rear.items)

if __name__ == "__main__":
    main()