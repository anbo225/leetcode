### 2018-02-08 solved ###
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [1 for i in range(len(s) + 1)]
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1

        for i in range(2,len(s)+1):
            if s[i-1] == '0' and s[i-2] in '34567890':
                return 0
            elif s[i-1] == '0' and s[i-2] in '12':
                dp[i] = dp[i-2]
            elif s[i-2] == '1' and s[i-1] in '123456789' or s[i-2] == '2' and s[i-1] in '123456':
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]


        return dp[len(s)]


s = Solution()
print( s.numDecodings('1') )