class Stack:

    def __init__(self, items = [], limit = 100):
      
        self.items = items[:limit]
        self.limit = limit

    def isEmpty(self):
        
        return len(self.items) == 0


    def push(self, item):
        
        if not self.full():
           self.items.append(item) 
        else:
            print('Stack is full, limit reached')

    

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print('stack is empty')  
            
    def peek(self):
        
        return self.items[-1]

    def size(self):
        
        return len(self.items)

    def full(self):
        
        return self.limit is not None and self.size() == self.limit

    def search(self, target):
        

        if target in self.items:
            index = self.items.index(target)
            return len(self.items) - 1 - index
        else:
            return -1