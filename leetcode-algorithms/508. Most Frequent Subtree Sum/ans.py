### 2018-01-27 solved ###
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 解题思路：采用中序遍历树，得到所有子树的sum；
        self.sums = []
        self.helper(root)

        count = {}
        maxCount = 1
        for sum in self.sums:
            if sum in count:
                count[sum] += 1
                if count[sum] > maxCount:
                    maxCount = count[sum]
            else:
                count[sum] = 1

        ans = []
        for key in count.keys():
            if count[key] == maxCount:
                ans.append(key)
        return ans

    def helper(self, root):
        if root == None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)

        sum = left + right + root.val
        self.sums.append(sum)
        return sum




