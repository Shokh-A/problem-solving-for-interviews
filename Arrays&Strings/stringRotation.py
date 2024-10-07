# Problem:
# String Rotation: Assume you have a method isSubstring which checks
# if one word is a substring of another. Given two strings, s1 and s2, 
# write code to check if s2 is a rotation of s1 using only one call to 
# isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

# Brainstorming:
# Does char case matter? Does whitespace matter?
# What is rotation of the string?
# String rotation is when character at the begining is moved to the end,
# shifting the other characters forward one position.

# One solution could be to count how many characters have been rotated 
# from the begining of the string, and then rotate that amount of characters
# back in s2. Then comparing s1 and s2 will show if they are the same string.

class Solution:

  def isSubstring(self, s1: str, s2: str) -> bool:
    return s2 in s1

  # This approach is wrong, since I understood the problem wrongly.
  # Shoul have used isSubstring
  # Time - O(n)
  # Space - O(n), since slicing and concatenation take O(n) space.
  def isRotation(self, s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False
    if s1 == s2: return True

    cnt_rotated = 0
    for i in range(len(s2)-1, -1, -1):
      cnt_rotated += 1
      if s2[i] == s1[0]:
        break
      
    return s1 == s2[len(s2)-cnt_rotated:] + s2[:len(s2)-cnt_rotated]
  
  # Time - O(n), assuming isSubstring time complexity is O(A+B)
  # Space - O(n)
  def isRotation_optimal(self, s1: str, s2: str) -> bool:
    n = len(s1)
    if n == len(s2) and n > 0:
      s1s1 = s1 + s1
      return self.isSubstring(s1s1, s2)

    return False

# Test
sol = Solution()
# Test case 1
print("1st test case:", sol.isRotation_optimal("waterbottle", "erbottlewat"))