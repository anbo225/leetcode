### 2018-02-04 solved ###
class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        # DP : dp[i][j] : s1匹配到i,s2匹配到j，需要花费的最小代价
        len1 = len(s1)
        len2 = len(s2)

        dp = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]

        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = min(ord(s1[i - 1]) + dp[i - 1][j], ord(s2[j - 1]) + dp[i][j - 1])
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                    # dp[i][j] = dp[i-1][j-1]

        return dp[len1][len2]


