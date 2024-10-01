from collections import defaultdict

# Problem:
# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Given two 
# strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false

# Brainstorming:
# In case of insertion or deletion, the length of the string is affected
# and since the difference shall be no more 1 edit away, the length difference
# between two strings shall not be greater than 1 too.
# In case of character replacement, the string lenght stays the same, but the
# characters count shall be the same with only one character having count
# difference of 1

class Solution:
  
  # Time - O(n)
  # Space - O(n)
  def oneAway(self, a: str, b: str) -> bool:
    diff_occured = abs(len(a) - len(b))
    if diff_occured > 1:
      return False

    char_cnt = defaultdict(int)
    for char in a:
      char_cnt[char] += 1

    for char in b:
      char_cnt[char] -= 1
    
    for cnt in char_cnt.values():
      if diff_occured > 1:
        return False
      if abs(cnt) != 0:
        diff_occured += 1
    return diff_occured <= 1
  
  def oneEditAway(self, a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
      return False
    
    s1 = b if len(a) > len(b) else a
    s2 = a if len(a) > len(b) else b

    ind1 = 0
    ind2 = 0
    foundDifference = False
    while ind2 < len(s2) and ind1 < len(s1):
      if s1[ind1] != s2[ind2]:
        if foundDifference: return False
        foundDifference = True

        if len(s1) == len(s2):
          ind1 += 1
      else:
        ind1 += 1
      ind2 += 1

    return True 
  

# Test 
sol = Solution()

# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false
# Test case 1
print("1st test case:", sol.oneEditAway("pale", "ple"))
# Test case 2
print("2nd test case:", sol.oneEditAway("pales", "pale"))
# Test case 3
print("3rd test case:", sol.oneEditAway("pale", "bale"))
# Test case 4
print("4th test case:", sol.oneEditAway("pale", "bae"))
# Test case 5
print("5th test case:", sol.oneEditAway("pale", "baee"))
