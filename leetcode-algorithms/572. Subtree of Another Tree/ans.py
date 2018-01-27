### 2018-01-27 solved ###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return False
        if self.helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def helper(self, s, t):
        if s is None and t is None:
            return True
        if (s is None or t is None) or s.val != t.val:
            return False
        return self.helper(s.left, t.left) and self.helper(s.right, t.right)


