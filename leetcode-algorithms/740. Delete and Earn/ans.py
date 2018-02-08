### 2018-02-04 solved ###
class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dic = {}
        largest = 0
        for num in nums:
            if num >= largest:
                largest = num
            if num in dic:
                dic[num]+= 1
            else:
                dic[num] = 1

        dp = [0 for i in range(largest + 1)]
        dp[1] = 1 * dic.get(1,0)
        for i in range(2, largest+1 ):
            dp[i] = max( dp[i - 2] + i * dic.get(i,0), dp[i - 1])

        return dp[largest]

s = Solution()
print(s.deleteAndEarn([1,1,1,2,4,5,5,5,6]))