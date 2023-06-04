# Implement a MyQueue class which implements a queue using two stacks

#? Idea: Only perform pop operations from the secondary stack
#! IMPORTANT: To minimize the shifting, only move elements from primary to secondary if secondary is empty
class MyQueue:
  def __init__(self):
    self.primary = []
    self.secondary = []

  # O(1)
  def enqueue(self, item):
    self.primary.append(item)
  
  # Amortized O(1)?
  def dequeue(self):
    self.peek()
    return self.secondary.pop()
  
  # O(1)
  def peek(self):
    if self.isEmpty(): raise Exception("Invalid pop/peek on empty queue!")
    if not self.secondary:
      while self.primary:
        self.secondary.append(self.primary.pop())
    return self.secondary[-1]
  
  # O(1)
  def isEmpty(self):
    return not self.primary and not self.secondary
  
  def __str__(self):
    return f"Primary: {self.primary} | Secondary: {self.secondary}"

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
queue.dequeue()
print(queue)
queue.enqueue(5)
queue.dequeue()
print(queue)