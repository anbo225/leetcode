### 2018-02-08 solved ###
class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        ans = 0
        dp = [0 for i in range(26)]  # 记录以26个小写字母结尾的字符串的最大长度，目的在保证子串的唯一性

        pre = 1  # 记录前一个字符匹配到的长度
        for i, ch in enumerate(p):
            if i == 0:
                dp[ord(ch) - ord('a')] = 1
            elif ord(p[i - 1]) + 1 == ord(ch) or (p[i - 1] == 'z' and ch == 'a'):
                pre = pre + 1
                dp[ord(ch) - ord('a')] = max(pre, dp[ord(ch) - ord('a')])
            else:
                pre = 1
                dp[ord(ch) - ord('a')] = max(pre, dp[ord(ch) - ord('a')])

        return sum(dp)

