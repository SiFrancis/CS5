import heapq

class Order:
    def __init__(self, id:int, urgency:int, timestamp:str):
        self.id = id
        self.urgency = urgency
        self.timestamp = timestamp

class OrderQueue:
    def __init__(self):
        self.main_queue = [] # contains Order instances
        self.order_heap = [] # only contains urgency numbers

    def insert(self, item:Order):
        self.main_queue.append(item)
        self.order_heap = [-x.urgency for x in self.main_queue]
        heapq.heapify(self.order_heap)
        self.main_queue.sort(key=lambda order: -order.urgency)
    
    def retrieve(self):
        heapq.heappop(self.order_heap)
        out = self.main_queue[0]
        self.main_queue = self.main_queue[1:]
        return f"Order({out.id}, {out.urgency}, {out.timestamp})"

# ==============SAMPLE CODE FROM QUESTION==============

# Create a queue
order_queue = OrderQueue()

# Insert orders
order_queue.insert(Order(1, 5, "2024-11-29 10:00"))
order_queue.insert(Order(2, 3, "2024-11-29 10:05"))
order_queue.insert(Order(3, 8, "2024-11-29 10:10"))

# Retrieve orders in order of highest urgency
print(order_queue.retrieve())  # Should print the order with urgency 8
print(order_queue.retrieve())  # Should print the order with urgency 5
print(order_queue.retrieve())  # Should print the order with urgency 3