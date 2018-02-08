### 2018-02-08 solved ###
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP1: O(n * n)
        # if not nums:
        #     return 0
        # dp = [1 for i in range(len(nums))]
        # ans  = 1
        # for i, num in enumerate(nums):
        #     for j in range(0,i):
        #         if num > nums[j] and dp[j]+1 > dp[i]:
        #             dp[i] = dp[j] + 1
        #     if dp[i] > ans:
        #         ans = dp[i]
        # return ans

        # DP2 : O(n* log(n)) ,以长度为单位进行dp，利用二分查找
        if not nums:
            return 0
        dp = [0 for i in range(len(nums))]

        maxlen = -1

        # 二分查找到dp数组中第一个大于等于key 的index，dp数组本身是有序的
        def binarySearch(key, l, r):  # [l, r]为闭区间
            l, r = l, r
            if dp[r] < key or r == -1:
                return r + 1
            while (l <= r):
                mid = int((l + r) / 2)
                if dp[mid] >= key:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        for i, num in enumerate(nums):
            # 找到num应该放入dp数组中的位置
            index = binarySearch(num, 0, maxlen)
            dp[index] = num
            if index > maxlen:
                maxlen = index

        return maxlen + 1


s = Solution()
print(s.lengthOfLIS([2,2]))