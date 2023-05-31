# Given an array of distinct integer values, count the number of pairs of integers that have difference k.
# Common problems:
# -- Pairs may be repeated. To avoid this use a set, and add sorted pairs
# -- Need to add both sides to the dictionary
# -- Values in the dictionary may be overridden by (n - k) and (n + k) both adding n. Avoid this by using a list for values

from collections import defaultdict

def findDiffPairs(arr, k):
    myDict = defaultdict(list)
    results = set()
    
    for n in arr:
        # Find counterpart in hash table
        if n in myDict:
            for other in myDict[n]:
                pair = (n, other) if n < other else (other, n)
                results.add(pair)

        # Add to hash table
        myDict[n - k].append(n)
        myDict[n + k].append(n)

    return len(results)

print(findDiffPairs([1, 7, 5, 9, 2, 12, 3], 2))