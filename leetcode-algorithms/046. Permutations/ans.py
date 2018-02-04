### 2018-02-03 solved ###
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        flag = [False for i in range(len(nums))]

        def dfs(cur):
            end = True
            for i in range(len(nums)):
                if flag[i] == False:
                    flag[i] = True
                    end = False
                    cur.append(nums[i])
                    dfs(cur)
                    cur.pop()
                    flag[i] = False
            if end:
                ans.append(list(cur))

        cur = []
        dfs(cur)
        return ans
s = Solution()
print(s.permute([1,2,3]))