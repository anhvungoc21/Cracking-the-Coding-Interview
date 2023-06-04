# Implement a data structure SetOfStacks that mimics the behavior of creating a new stack when a previous stack of plates gets too high.
# SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity.
# .pop and .push should behave identically to a single stack
# Also, implement a .popAt(int index) that performs a pop operation on a specific sub-stack

# Push new sub-stack when previous stack runs out
class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, item):
        # Create new sub-stack if stack is empty of previous stack is full
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([item])    
        else:
            self.stacks[-1].append(item)
    
    def pop(self):
        if not self.stacks: raise Exception("Unable to pop from an empty set of stacks")
        
        # Pop from last sub-stack
        popped = self.stacks[-1].pop()

        # Pop last sub-stack if empty
        if not self.stacks[-1]:
            self.stacks.pop()

        return popped
    
    def popAt(self, index):
        popped = self.stacks[index].pop()

        # Remove sub-stack if empty
        if not self.stacks[index]:
            self.stacks.pop(index)
        return popped
    

    # ----
    def pushAll(self, arr):
        for n in arr:
            self.push(n)
        print(self.stacks)

    def popPrint(self):
        print(self.pop())
        print(self.stacks)

    def popAtPrint(self, index):
        print(self.popAt(index))
        print(self.stacks)
    
stacks = SetOfStacks(2)
stacks.pushAll([1, 2, 3, 4, 5, 6, 7])
stacks.popPrint()
stacks.popPrint()
stacks.popAtPrint(1)
stacks.popAtPrint(1)