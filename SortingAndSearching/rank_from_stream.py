# Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x). Implement the data structures and algorithms to support these operations. That is, implement the method track(int x), which is called when each number if generated, and the method getRankOfNumber(int x), which returns the number of values less than or equal to x (not including this instance of x itself)

# ? If node is on right sub-tree of another: Rank = parent.leftsize() + 1 + Recurse(parent.right)
# ? If node is on left sub-tree of another: Rank = Recurse(parent.left)


class RankNode:
    def __init__(self, data):
        self.data = data
        self.left_size = 0
        self.left = None
        self.right = None

    def insert(self, new_data):
        # Insert smaller into left
        if (new_data <= self.data): # Equality also counts duplicates
            self.left_size += 1

            if not self.left:
                self.left = RankNode(new_data)
            else:
                self.insert(self.left)

        # Insert larger into right
        else:
            if not self.right:
                self.right = RankNode(new_data)
            else:
                self.insert(self.right)

    def getRank(self, data):
        if data == self.data: 
            return self.left_size

        elif data < self.data:
            if not self.left: 
                return -1
            return self.left.getRank()
        
        else:
            right_rank = self.right.getRank() if self.right else -1
            if right_rank == -1:
                return -1
            else:
                return self.left_size + 1 + right_rank


    
            
        
