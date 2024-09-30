from collections import defaultdict

# Problem:
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat'; "atc o eta·; etc.)

# Brainstorming:
# What is palindrome? What is permutation?
# Whitespace, special characters matter?
# What about case?

class Solution:
  # Time - O(n)
  # Space - O(128) if ASCII, O(256) if Unicode ==> O(1)
  # Space - O(k), where k is number of disctinct characters,
  # which in ASCII is at most 128, and 256 in Unicode.
  def isPalindromePermutation(self, s: str) -> bool:
    s = s.lower()
    char_cnt = defaultdict(int)
    for char in s:
      if char == " ":
        continue
      char_cnt[char] += 1
    
    uneven_cnt_appeared = False
    for cnt in char_cnt.values():
      if (cnt % 2) == 1 and uneven_cnt_appeared:
        return False
      elif (cnt % 2) == 1:
        uneven_cnt_appeared = True
    return True
  
  def isPalindromePermutation_1(self, s: str) -> bool:
    odd_cnt = 0
    char_cnt = defaultdict(int)
    for char in s.lower():
      if not char.isalpha():
        continue
      char_cnt[char] += 1
      if char_cnt[char] % 2 == 1:
        odd_cnt += 1
      else:
        odd_cnt -= 1

    return odd_cnt <= 1

  def isPalindromePermutation_2(self, s: str) -> bool:
    # Initialize a variable to track the odd counts
    bit_vector = 0
    
    # Iterate through each character in the string
    for char in s.lower():
        if char.isalpha():  # Consider only alphabetic characters
            # Get the position of the character (a=0, b=1, ..., z=25)
            index = ord(char) - ord('a')
            # Toggle the corresponding bit using XOR
            bit_vector ^= (1 << index)
    
    # Check if at most one bit is set in the bit vector
    # A number has at most one bit set if (n & (n - 1)) == 0
    return bit_vector == 0 or (bit_vector & (bit_vector - 1)) == 0

# Test
sol = Solution()
# Test case 1
print("1st test case:", sol.isPalindromePermutation_1("Tact coa"))
# Test case 2
print("2nd test case:", sol.isPalindromePermutation_1(""))
# Test case 3
print("3rd test case:", sol.isPalindromePermutation_1("Tact        coaa"))
# Test case 4
print("4th test case:", sol.isPalindromePermutation_1("t"))
