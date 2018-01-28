### 2018-01-28 solved ###
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 解题思路：DP
        target = sum(nums)
        if target % 2 == 1:
            return False
        else:
            target = int(target / 2)


        dp = [[False for j in range(target+1)] for i in range(len(nums) + 1)]

        #Init
        dp[0][0] = True

        for i in range(1,len(nums) + 1):
            for j in range(1,target + 1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j - nums[i-1]]
                dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[len(nums)][target]

s = Solution()
print(s.canPartition([1,5,11,5]))