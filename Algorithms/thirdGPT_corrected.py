class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0

stack1 = Stack()
lst = [4, 3, 25, 63, 6, 4, 317, 4, 39, 0, 76, 91, 3, 2, 8]

# Pushing items one by one into the stack
for item in lst:
    stack1.push(item)

n = stack1.size()

# Initializing max and min with the first element in the list
max_val = float('-inf')
min_val = float('inf')

# Finding max and min using stack
for i in range(n):
    value = stack1.peek()
    
    if value > max_val:
        max_val = value
    if value < min_val:
        min_val = value
        
    stack1.pop()

print(f"Max: {max_val}, Min: {min_val}")
