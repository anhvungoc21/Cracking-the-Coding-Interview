# Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but may not copy the elements into any other data structure such as an array. The stack supports: push, pop, peek, isEmpty

# Tower-of-hanoi ish?
#? Idea: Move all elements to a separate `unsorted` stack, then and gradually move elements into the original stack
#? If an incoming element is larger than elements in the sortedStack, take that element out, pop until satisfactory back into `stack`, insert, then pop back.

def sortStack(stack):
    # Will use Python lists to mimic stacks
    unsorted = []
    
    # Move all elements to the new stack to return the original stack
    while stack:
        unsorted.append(stack.pop())

    
    while unsorted:
        popped = unsorted.pop()

        # Temporarily move elements out of `stack` to make space for a "correct" element
        tempCount = 0
        while stack and stack[-1] < popped:
            unsorted.append(stack.pop())
            tempCount += 1
        
        # Move correct element in to `stack`
        stack.append(popped)

        # Pop back into `stack`65
        for _ in range(tempCount):
            stack.append(unsorted.pop())

    return stack

stack = [5, 2, 3, 6, 4, 8, 10, 1]
print(sortStack(stack))


         