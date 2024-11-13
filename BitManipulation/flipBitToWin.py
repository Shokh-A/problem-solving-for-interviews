# Problem:
# Flip Bit to Win: You have an integer and you can flip exactly one bit from a O to a 1.
# Write code to find the length of the longest sequence of 1 s you could create.
# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8

# Brainstorming:
#

class Solution:

  # Brute force
  def longestSequence(self, n):
    n_str = bin(n)[2:]
    max_cnt, cnt, cnt0 = 0, 0, 0
    i = len(n_str)
    while i:
      if int(n_str[i-1]):
        cnt += 1
      else:
        if cnt0 == 0:
          temp_i = i
          cnt0 = 1
        else:
          max_cnt = max(cnt, max_cnt)
          i = temp_i
          cnt0 = 0
          cnt = 0
      i -= 1
    
    max_cnt = max(cnt, max_cnt)
    return max_cnt + 1
  
  def flipBit(self, n):
    if ~n == 0: return int.bit_count

    curLength = 0
    prevLength = 0
    maxLength = 1
    while n != 0:
      if (n & 1) == 1:
        curLength += 1
      elif n & 1 == 0:
        prevLength = 0 if (n & 2) == 0 else curLength
        curLength = 0
      maxLength = max(prevLength + curLength + 1, maxLength)
      n >>= 1
    return maxLength  

# Test
sol = Solution()
# Test case 1
print("1st test case", sol.flipBit(1775))

