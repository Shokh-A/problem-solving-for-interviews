class Solution:
  def URLify(self, s: str, l: int) -> str:
    return s[:l].replace(" ", "%20")
  
  def urlify_manual(self, string, true_length):
    # Convert the string to a list to simulate in-place modification
    chars = list(string)
    space_count = 0
    
    # Count spaces within the true length
    for i in range(true_length):
        if chars[i] == ' ':
            space_count += 1
    
    # Calculate the new index based on the number of spaces
    index = true_length + space_count * 2
    result = [''] * index  # Create a new list with the necessary length

    # Traverse the string in reverse, replacing spaces with '%20'
    for i in range(true_length - 1, -1, -1):
        if chars[i] == ' ':
            result[index - 1] = '0'
            result[index - 2] = '2'
            result[index - 3] = '%'
            index -= 3
        else:
            result[index - 1] = chars[i]
            index -= 1

    return ''.join(result)
  

# Test
sol = Solution()
# Test case 1
print("1st test case:", sol.urlify_manual("Mr John Smith   ", 13))
