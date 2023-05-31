# Given a smaller string `s` and a bigger string `b`, design an algorithm to find all permutations of the shorter string within the longer one. Print the location of each permutation
from collections import Counter


def findPermInString(s, b):
    # Create counter of string s
    sCounter = Counter(s)

    # Create and slide window
    window = Counter(b[:len(s)])
    results = []

    # Initial check
    if window == sCounter:
      results.append(0)

    for i in range(0, len(b) - len(s)):
      # Remove current letter from counter
      window[b[i]] = max(window[b[i]] - 1, 0)

      # Add next letter to counter
      window.update(b[i + len(s)])

      # i + 1 cuz i is removed
      if window == sCounter:
        results.append(i + 1) 

    return results
    
print(findPermInString("abbc", "cbabadcbbabbcbabaabccbabc"))

# Analysis:
# - Time:
#   + Create counter of s: O(|s|)
#   + Create window: O(|s|)
#   + Slide window: O(|b|)
#     - Compare counters: O(1) -- No more than 26 letters
#     - Add/Subtract from counter: O(1) -- Dictionary subclass. Assumed.
# => Total runtime: O(|b|) since |s| < |b|

# - Space: 2 counters. No more than 26 letters => O(1)