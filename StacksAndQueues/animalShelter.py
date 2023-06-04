# An animal shelter, holding dogs and cats, operates strictly on a "first in, first out" basis
# People must adopt either the "oldest" (based on arrival time) of animals at the shelter, 
# or they can select whether they would prefer a dog or a cat, and will receive the oldest animal of that type. 
# Create the data structures to maintain this system and implement operations such as 
# enqueue, dequeueAny, dequeueDog, dequeueCat
# You may use the built-in LinkedList data structure

#? Idea: Use 2 LinkedLists separately for Dogs and Cats.
#? => IMPORTANT: Number the incoming dog/cat. Keep this running count.
#?               When dequeueAny, compare the 2 linked list heads, and dequeue the "older" one

# Use built-in linked lists
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def insertTail(self, data):
        node = Node(data)

        # First node
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def removeHead(self):
        toRet = self.head

        self.head = self.head.next
        # Final node
        if not self.head:
            self.tail = None

        return toRet

class Animal:
    def __init__(self, typeStr):
        self.dog = typeStr == "dog"

    def __str__(self):
        return "dog" if self.dog else "cat"

    def isDog(self):
        return self.dog
    
    def isCat(self):
        return not self.dog

class AnimalShelter:
    def __init__(self):
        self.dogs = LinkedList(None)
        self.cats = LinkedList(None)
        self.age = 0

    # O(1)
    def enqueue(self, animal: Animal):
        self.age += 1
        if animal.isDog():
            self.dogs.insertTail((self.age, animal))
        else:
            self.cats.insertTail((self.age, animal))

        return self

    # O(1)
    def dequeueAny(self):
        if not self.dogs.head and not self.cats.head: 
            raise Exception("No animal exists!")
        elif not self.cats.head:
            return self.dequeueDog()
        elif not self.dogs.head:
            return self.dequeueCat()
        else:        
          # Compare age of first dog and first cat
          return self.dequeueDog() if self.dogs.head.data[0] < self.cats.head.data[0] else self.dequeueCat()
        
    # O(1)
    def dequeueDog(self):
        if not self.dogs.head: raise Exception("No dog exists!")
        return self.dogs.removeHead().data[1]
    
    # O(1)
    def dequeueCat(self):
        if not self.cats.head: raise Exception("No cat exists!")
        return self.cats.removeHead().data[1]
    

shelter = AnimalShelter()

# dog -> dog -> cat -> dog -> cat
shelter.enqueue(Animal("dog")).enqueue(Animal("dog")).enqueue(Animal("cat")).enqueue(Animal("dog")).enqueue(Animal("cat"))
print(shelter.dequeueAny())
print(shelter.dequeueCat())
print(shelter.dequeueDog())
print(shelter.dequeueCat())
print(shelter.dequeueAny())
print()

shelter.enqueue(Animal("dog")).enqueue(Animal("dog")).enqueue(Animal("cat")).enqueue(Animal("dog")).enqueue(Animal("cat"))
print(shelter.dequeueAny())
print(shelter.dequeueAny())
print(shelter.dequeueAny())
print(shelter.dequeueAny())
print(shelter.dequeueAny())