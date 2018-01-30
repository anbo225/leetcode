### 2018-01-30 solved ###
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # 解法： DP + backtracking
        # 1. 利用DP求出所有的回文串
        dp = [[] for i in range(len(s))]
        for i in range(len(s)):
            for j in range(0, i + 1):
                if i == j:  # 初始化奇数回文子串
                    dp[i].append(j)
                elif s[i] == s[j] and j + 1 == i:  # 初始化偶数回文子串
                    dp[i].append(j)
                elif j + 1 in dp[i - 1] and s[i] == s[j]:  # dp状态转移方程 ：dp[j][i] = True if dp[j+1][i-1] and s[i] == s[j]
                    dp[i].append(j)
        # 2. 回溯找到所有答案
        ans = []

        self.backtracking(ans, [], dp, len(s) - 1, s)
        return ans

    def backtracking(self, ans, currentAns, dp, end, s):
        if end < 0:  # 找到了符合条件的ans
            ans.append(list(currentAns[::-1]))
            return

        for start in dp[end]:
            currentAns.append(s[start:end + 1])
            self.backtracking(ans, currentAns,dp ,start - 1, s)
            currentAns.pop()

m = Solution()

print(m.partition("cbbbcc"))




