### 2018-02-04 solved ###
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False

        target = int(total / k)

        nums = sorted(nums, reverse=True)

        def dfs(nums, k, cur):  # 能否在现有的基础上找到k个组合
            if k == 0:
                return True if not nums else False
            if not nums:
                return False

            for i in range(len(nums)):
                if nums[i] < target - cur:
                    if dfs(nums[:i] + nums[i + 1:], k, cur + nums[i]):
                        return True
                elif nums[i] == target - cur:
                    return dfs(nums[:i] + nums[i + 1:], k - 1, 0)
                else:
                    return False

            return False

        return dfs(nums, k, 0)
