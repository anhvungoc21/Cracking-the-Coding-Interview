# You have a stack of n boxes, with widths wi, heights hi, and depths di. The boxes cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly larger than the box above it in width, height, and depth. Implement a method to compute the height of the tallest possible stack. The height of the stack is the sum of the heights of each box.


# To avoid 1 level of repetitive checking, we can sort the boxes by 1 level
# "Strictly" larger -> For any boxes with the same w/h/d, we prefer selecting the one with the larger other dimensions. However, there are 2 dimensions left. We cannot make that choice.

# ? Approach 1: Choose each box as a bottom and build
# Optimization: Memoization since we have an enforced direction
# * The optimal solution can just be a few tweaks from the non-optimal one!

def solution(boxes):
    boxes = sorted(boxes, key=lambda box: -box[1])
    boxes_map = [0 for _ in range(len(boxes))]
    max_height = 0
    for index in range(len(boxes)):
        height = stacks_of_boxes(boxes, index, boxes_map)
        max_height = max(max_height, height)

    return max_height

def stacks_of_boxes(boxes, index, boxes_map):
    # Check if already visited
    if boxes_map[index] > 0:
        return boxes_map[index]
    
    # Selected bottom
    cur_bottom = boxes[index]

    # Build highest stack with current bottom
    max_height = 0
    for i in range(index + 1, len(boxes)):
        if larger(cur_bottom, boxes[i]):
            height = stacks_of_boxes(boxes, i, boxes_map)
            max_height = max(max_height, height)

    # Insert into map and return
    max_height += cur_bottom[1]
    boxes_map[index] = max_height
    return max_height

def larger(box1, box2):
    w1, h1, d1 = box1
    w2, h2, d2 = box2
    return w1 > w2 and h1 > h2 and d1 > d2

# ? Approach 2: Use-it or Lose-it for each box
def solution(boxes):
    boxes = sorted(boxes, key=lambda box: -box[1])
    boxes_map = [0 for _ in range(len(boxes))]
    return stacks_of_boxes(boxes, None, 0, boxes_map)


# Boxes_map[i] stores the largest height of stack with boxes[i] as the bottom
def stacks_of_boxes(boxes, cur_bottom, offset, boxes_map):
    # Invalid
    if offset >= len(boxes): return 0
    
    # Use-it (next bottom)
    height_with_bottom = 0
    next_bottom = boxes[offset]
    if not cur_bottom or larger(cur_bottom, next_bottom):
        # Check cache
        if boxes_map[offset] == 0:
            boxes_map[offset] = stacks_of_boxes(boxes, next_bottom, offset + 1, boxes_map)
            boxes_map[offset] += next_bottom[1]
        
        # Get result
        height_with_bottom = boxes_map[offset]        

    # Lose it (next bottom). Since we don't use it, we don't have to store it.
    height_without_bottom = stacks_of_boxes(boxes, cur_bottom, offset + 1, boxes_map)

    return max(height_with_bottom, height_without_bottom)


boxes = [(1, 1, 1), (3, 2, 5), (3, 3, 4), (2, 2, 1), (2, 2, 3)]
print(solution(boxes))