class stack():
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return True if self.stack[0] == None else False
    
stack1 = stack()
lst = [4,3,25,63,6,4,317,4,39,0,76,91,3,2,8]
for item in lst:
    stack1.push(item)
n = stack1.size()
max = float('-inf')
min = float('inf')
for i in range(n):
    if float(stack1.peek()) > max:
        max = stack1.peek()
    if float(stack1.peek()) < min:
        min = stack1.peek()
    stack1.pop()
print(min,max)