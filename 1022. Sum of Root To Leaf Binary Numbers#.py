# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            root, val = stack.pop()
            if root is not None:
                val = (val << 1) | root.val
                if root.left is None and root.right is None:
                    ans += val
                else:
                    stack.append((root.right, val))
                    stack.append((root.left, val))
        return ans
