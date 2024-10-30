class TreeNode:
  def __init__(self, val, left=None, right=None, parent=None):
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent

  def disp(self, nesting=0):
    indent = " " * nesting * 2
    output = f"{self.val}\n"
    if self.left is not None:
      output += f"{indent}L:"
      output += self.left.disp(nesting + 1)
    if self.right is not None:
      output += f"{indent}R:"
      output += self.right.disp(nesting + 1)
    return output
  
  def __str__(self):
    return self.disp()