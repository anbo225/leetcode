### 2018-01-28 solved ###
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s) + 1)]
        # init
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                if i >= len(word) - 1 and word == s[i - len(word) + 1:i + 1]:  # 如果匹配
                    dp[i + 1] = dp[i + 1 - len(word)] or dp[i + 1]
        return dp[len(s)]



