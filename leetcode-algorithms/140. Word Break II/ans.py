### 2018-01-30 solved ###
class Solution(object):
    def wordBreak_check(self, s, wordDict):
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                if dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
        return dp[-1]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        if not self.wordBreak_check(s, wordDict):
            return []
        mem = {}
        for i in range(len(s)):  # 遍历s中每一个字符
            mem[i + 1] = []
            for word in wordDict:
                if i >= len(word) - 1 and word == s[i + 1 - len(word):i + 1]:
                    if i == len(word) - 1:
                        mem[i + 1].append(word)
                    else:
                        for ans in mem[i - len(word) + 1]:
                            mem[i + 1].append("%s %s" % (ans, word))
        return mem[len(s)]