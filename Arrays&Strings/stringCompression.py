from collections import defaultdict

# Problem:
# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


# Brainstorming:
# What letters are used?
# keep order of character occurence

class Solution:

  # string concatenation takes O(k^2) where k is the number of character sequences 
  # Time - O(p + k^2), where p is the length of the string
  def stringCompressor(self, s: str) -> str:
    res = ""
    cntConsecutive = 0
    for i in range(len(s)):
      cntConsecutive += 1
      if (i + 1 >= len(s) or s[i] != s[i+1]):
        res += s[i] + str(cntConsecutive)
        cntConsecutive = 0 
    return res if len(res) < len(s) else s
  
  # Using list to build answer reduces time complexity as lists are mutable in python, but strings are not
  # Time - O(n)
  def stringCompressor_optimized(self, s: str) -> str:
    res = []
    cntConsecutive = 0
    for i in range(len(s)):
      cntConsecutive += 1
      if (i + 1 >= len(s) or s[i] != s[i+1]):
        res.append(s[i])
        res.append(str(cntConsecutive))
        cntConsecutive = 0
    return "".join(res) if len(res) < len(s) else s


# Test
sol = Solution()
# Test case 1
print("1st test case:", sol.stringCompressor("aabcccccaaa"))
# Test case 2
print("2nd test case:", sol.stringCompressor("abc"))
# Test case 3
print("3rd test case:", sol.stringCompressor("aabbc"))