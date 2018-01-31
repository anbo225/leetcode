### 2018-01-31 solved ###
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解题方法： 扫一遍
        if s == None:
            return 0
        d = {}
        for ch in s:
            d[ch] = d[ch] + 1 if ch in d else 1

        ans = 0
        flag = False  # 标记是否可以形成 奇数形 回文串
        for _, value in d.items():
            if value % 2 == 0:
                ans += value
            else:
                flag = True
                ans += int(value -1 )
        if flag:
            return ans + 1
        else:
            return ans


s= Solution()
print(s.longestPalindrome("ccc"))