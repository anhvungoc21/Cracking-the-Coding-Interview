# Write a method to sort an array of strings so that all the anagrams are next to each other

# Observations:
# - Comparison-based sorting -> Comparator
# - Anagrams: Number of characters -> Assuming English letters, we can compare #a's then #b's and so on
# => Approach 1: Use normal sorting algorithms and use a different comparator
# => Approach 2: There's no requirements about the ordering. We can just group by anagram and insert each into the array.

from collections import defaultdict
def solution(strings):
    # Group by anagram
    groups = defaultdict(list)
    for s in strings:
        groups[get_anagram_key(s)].append(s)

    # Insert back into array
    idx = 0
    for _, anagrams in groups.items():
        for anagram in anagrams:
            strings[idx] = anagram
            idx += 1

    return strings

def get_anagram_key(s):
    # Key by count of characters
    key = [0 for _ in range(26)]
    for char in s:
        key[ord(char.lower()) - ord('a')] += 1
    return str(key)

    # Or, just
    # return str(sorted(s))

strings = ["abc", "ed", "acb", "", "abc", "de", "abb", "cab"]
print(solution(strings))