# Problem: 
# Is Unique: Implement an algorithm to determine 
# if a string has all unique characters. What if
# you cannot use additional data structures?

# Brainstorming:
# Is input ASCII or Unicode string?
# ASCII has 128 characters, Unicode has 256 characters
# If the string is longer than 128 characters, it must have duplicates
# If the string is ASCII, we can use a boolean array of size 128
# If the string is Unicode, we can use a boolean array of size 256
# If we can not use additional data structures, we can sort the string
# and check if there are any duplicates.

class Solution:

  # Time: O(n)
  # Space: O(1)
  def isUniqueChars(self, s: str) -> bool:
    # Unicode string
    if len(s) > 256: return False
    
    char_set = [False] * 256
    for char in s:
      val = ord(char)
      if char_set[val]:
        return False
      char_set[val] = True
    
    return True

  # Time: O(n)
  # Space: O(1)
  def isUniqueChars_1(self, s: str) -> bool:
    # ASCII string
    if len(s) > 128: return False

    char_set = [False] * 128
    for char in s:
      val = ord(char)
      if char_set[val]:
        return False
      char_set[val] = True
    
    return True
  
  # Time: O(n)
  # Space: O(1)
  def isUniqueChars_2(self, s: str) -> bool:
    checker = 0
    for char in s:
      var = ord(char) - ord('a')
      if (checker & (1 << var)) > 0:
        return False
      checker |= (1 << var)
    
    return True
  
  # Can not use additional data structures
  # Time: O(n^2)
  # Space: O(1)
  def isUniqueChars_3(self, s: str) -> bool:
    s = sorted(s)
    for i in range(len(s) - 1):
      if s[i] == s[i + 1]:
        return False
    return True

# Test Cases
sol = Solution()

# Test Case 1
s = "abcde"
# Expected: True
print("Test Case 1 expected: True")
print("Initial implementation:", sol.isUniqueChars(s))
print("First implementation:", sol.isUniqueChars_1(s))
print("Second implementation:", sol.isUniqueChars_2(s))
print("Third implementation:", sol.isUniqueChars_3(s))

# Test Case 2
s = "abcdea"
# Expected: False
print("Test Case 2, expected: False")
print("Initial implementation:", sol.isUniqueChars(s))
print("First implementation:", sol.isUniqueChars_1(s))
print("Second implementation:", sol.isUniqueChars_2(s))
print("Third implementation:", sol.isUniqueChars_3(s))

# Test Case 3
s = ""
# Expected: True
print("Test Case 3 expected: True")
print("Initial implementation:", sol.isUniqueChars(s))
print("First implementation:", sol.isUniqueChars_1(s))
print("Second implementation:", sol.isUniqueChars_2(s))
print("Third implementation:", sol.isUniqueChars_3(s))

# Test Case 4
s = "121231asdfas"
# Expected: False
print("Test Case 4 expected: False")
print("Initial implementation:", sol.isUniqueChars(s))
print("First implementation:", sol.isUniqueChars_1(s))
# In case of isUniqueChars_2, it can not handle numbers
# print("Second implementation:", sol.isUniqueChars_2(s))
print("Third implementation:", sol.isUniqueChars_3(s))
