### 2018-01-31 solved ###
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            j = i + 1
            while (j != len(nums)):
                if (nums[i] + nums[j] == target):
                    res.append(i)
                    res.append(j)
                    return res
                j = j + 1
        return res
