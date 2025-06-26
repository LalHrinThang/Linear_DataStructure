class Stack:
    # constructor
    def __init__(self):
        self.item = []
    
    def isEmpty(self):
        return self.item == []
    
    def push(self,element):
        self.item.append(element)
    
    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]
    
s = Stack()
print(s.isEmpty())
s.push("hello")
s.push("world")
print(s.peek())
s.pop()
print(s.peek())