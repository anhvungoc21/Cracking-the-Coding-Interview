# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element. Push, pop, and min should all operate in O(1) time.

# Idea: Previous mins outlive new mins => Keep a stack of min elements
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    # Push to stack
    # If smaller than top of minStack, also push to minStack
    def push(self, item):
        self.stack.append(item)
        if not self.minStack or item <= self.minStack[-1]: # There may be duplicates of min
            self.minStack.append(item)
        
    # Pop from main stack
    # If item is the same as minStack, also pop from minStack
    def pop(self):
      if not self.stack: raise Exception("Unable to pop from empty stack!")
      popped = self.stack.pop()
      if popped == self.minStack[-1]:
        self.minStack.pop()
      return popped
    
    # Peek minStack
    def min(self):
       if not self.minStack: raise Exception("Unable to peek empty min stack!")
       return self.minStack[-1]
    
    # ---- Utilities ----
    def performOperations(self, operations):
       for op, data in operations:
          if op == "push":
            self.push(data)
            print("pushed")
          elif op == "pop":
            print(self.pop())
          elif op == "min":
            print(self.min())
          else:
            raise Exception("Invalid operation!")
  
stack = MinStack()
ops = [("push", 2), ("min", None), ("push", 1), ("min", None), ("pop", None), ("min", None)]
stack.performOperations(ops)
