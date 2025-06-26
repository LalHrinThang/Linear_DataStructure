from queue import Queue
    
class PQueue:
    def __init__(self):
        self.items = {}
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item, priority = 0):
        if priority not in self.items:
            self.items[priority] = Queue()
        queue = self.items[priority]
        queue.put(item)
    
    def dequeue(self):
        keys = list(self.items.keys())
        
        if len(keys) > 0:
            cursor = max(keys)
            myqueue = self.items[cursor]
            
            val = myqueue.get()
            
            if myqueue.qsize() == 0:
                del self.items[cursor]
            
            return val
        return ""
    
    def size(self):
        size = 0
        for keyu in self.items.keys():
            size += self.items[key].qsize()
            
        return size
        
q = PQueue()

q.enqueue('testing',1)
q.enqueue('abcd',2)
q.enqueue('efg',2)
q.enqueue('xyz',1)
q.enqueue("HDCS",3)

print(q.dequeue())