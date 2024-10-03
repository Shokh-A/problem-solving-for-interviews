from collections import defaultdict

# Problem:
# Check Permutation: Given two strings, write a method to decide if one is a permutation
# of the other.

# Brainstorming:
# ASCII or Unicode?
# Is case sensitive?
# Does whitespace matter?
# Can we transform strings?
# Count occurance of each character in two strings and compare if it is equal.
# If permutation, both strings should be of equal length


class Solution:

  def isPermutation(self, a: str, b: str) -> bool:
    if len(a) != len(b):
      return False
    
    occ = defaultdict(int)
    n = len(a)
    for char in a:
      occ[char] += 1

    for char in b:
      occ[char] -= 1
      if occ[char] < 0:
        return False
    
    return True
  
  # Time: O(nlogn)
  # Space: O(1)
  def isPermutation_1(self, a: str, b: str) -> bool:
    # Sort both strings and compare each letter
    if len(a) != len(b):
      return False
    
    return sorted(a) == sorted(b)
  
# Test
sol = Solution()

# Test case 1
print("1st test case, expected True:", sol.isPermutation(a = "abc", b = "cab"))
# Test case 2
print("2nd test case, expected False:", sol.isPermutation(a = "abc", b = "cad"))
# Test case 3
print("3rd test case, expected False:", sol.isPermutation(a = "aa", b = ""))
# Test case 4
print("4th test case, expected True:", sol.isPermutation(a = "aabbcc", b = "bacbac"))
# Test case 5
print("5th test case, expected False:", sol.isPermutation(a = "aaabbcced", b = "bbbaaeedd"))
# Test case 6
print("6th test case, expected False:", sol.isPermutation(a = "Abc", b = "AbC"))
# Test case 7
print("7th test case, expected False:", sol.isPermutation(a = "aaa  bbcced", b = "aaabbcced"))




