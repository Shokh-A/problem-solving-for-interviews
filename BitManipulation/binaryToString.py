# Problem:
# Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately in binary with at
# most 32 characters, print "ERROR:".

# Brainstorming:
#

class Solution:

  def printBinary(self, num):
    if (num >= 1 or num <= 0):
      return "ERROR"
    
    binary = "."
    while num > 0:
      if len(binary) >= 32:
        return "ERROR"
      
      r = num * 2
      if r >= 1:
        binary += "1"
        num = r - 1
      else:
        binary += "0"
        num = r

    return binary

  def printBinary2(self, num):
    if num >= 1 or num <= 0:
      return "ERROR"
    
    binary = "."
    frac = 0.5
    while num > 0:
      if len(binary) > 32:
        return "ERROR"
      if num >= frac:
        binary += "1"
        num -= frac
      else:
        binary += "0"
      frac /= 2
    return binary

# Test
sol = Solution()
# Test case 1
print("1st test case", sol.printBinary(0.72))
print("2st test case", sol.printBinary(0.25)) 
print("3st test case", sol.printBinary(0.48)) 