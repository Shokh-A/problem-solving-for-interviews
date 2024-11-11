# Problem:
# Insertion: You are given two 32-bit numbers, N and M, and two bit positions,
# i and j. Write a method to insert M into N such that M starts at bit j and 
# ends at bit i. You can assume that the bits j through i have enough space to
# fit all of M. That is, if M = 10011, you can assume that there are at least 5
# bits between j and i. You would not, for example, have j = 3 and i = 2, because
# M could not fully fit between bit 3 and bit 2.
# EXAMPLE
# Input: N 10000000000, M = 10011, i = 2, j = 6
# Output: N = 10001001100

# Brainstorming:
# 

class Solution:
  def insertBits(self, n, m, i, j):
    allOnes = ~0

    left = allOnes << (j+1)
    right = ((1 << i) - 1)
    mask = left | right

    n_cleared = n & mask
    m_shifted = m << i

    return bin(n_cleared | m_shifted)

# Test
sol = Solution()
# Test case 1
print("1st test case", sol.insertBits(n=int("10000000000", 2), m=int("10011", 2), i=2, j=6))

