class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def __len__(self):
        return len(self.items)

class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        return self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def __len__(self):
        return len(self.items)

class Deque():
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

urgent = Stack()
routine = Queue()
flex = Deque()

def add_task(type:str, task:str):
    if type.upper() not in "URF":
        print(f"ERROR: Task '{task}' has invalid type '{type}'.")
    elif type.upper() == "U":
        urgent.push(task)
    elif type.upper() == "R":
        routine.enqueue(task)
    elif type.upper() == "F":
        if len(flex) % 2 == 0:
            flex.add_front(task)
        else:
            flex.add_rear(task)

def process():
    print("Processing Urgent Tasks (LIFO - Stack):")
    for i in range(len(urgent)):
        print("Processing:", urgent.pop())
    print("\nProcessing Routine Tasks (FIFO - Queue):")
    for i in range(len(routine)):
        print("Processing:", routine.dequeue())
    print("\nProcessing Flexible Tasks (Deque operations):")
    for i in range(len(flex)):
        if i % 2 == 0:
            print("Processing from deque front:", flex.remove_front())
        else:
            print("Processing from deque end:", flex.remove_rear())

def task_input():
    running = True
    while running:
        inp = str(input("Enter 'Type [U/R/F] - Task' or 'end' to stop input: \n"))
        if inp == 'end': 
            running = False
            break
        else:
            split_inp = inp.split(" - ")
            add_task(split_inp[0], split_inp[1])

def main():
    task_input()
    process()

if __name__ == "__main__":
    main()