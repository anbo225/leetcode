### 2018-02-03 solved ###
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root.left == None and root.right == None):
            return -1
        leftVal = root.left.val
        rightVal = root.right.val

        if leftVal == root.val:
            leftVal = self.findSecondMinimumValue(root.left)
        if rightVal == root.val:
            rightVal = self.findSecondMinimumValue(root.right)

        if leftVal != -1 and rightVal != -1:
            return min(leftVal, rightVal)
        elif leftVal != -1:
            return leftVal
        elif rightVal != -1:
            return rightVal
        else:
            return -1


