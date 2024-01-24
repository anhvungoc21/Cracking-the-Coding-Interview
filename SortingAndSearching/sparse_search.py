# Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.

# Idea: Think what if there are no empty strings
# => Try to achieve exactly that.
# Whenever a mid is calculated, find the nearest "actual" string and recurse

def solution(arr, target):
    # Finding an empty string should be invalid
    if target == "": return -1

    return sparse_search(arr, target)

def sparse_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        # Find nearest real string
        left = right = mid
        while True:
            # ! Important
            if left < low and right > high:
                return - 1
            elif arr[left] != "":
                mid = left
                break
            elif arr[right] != "":
                mid = right
                break
            
            left -= 1
            right += 1

        # Normal binary search
        if arr[mid] == target: 
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

strings = ["abc", "", "", "", "de", "", "", "fgww", "fze", "", "", ""]
print(solution(strings, "fgww"))
