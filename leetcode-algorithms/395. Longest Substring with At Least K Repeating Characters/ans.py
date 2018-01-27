### 2018-01-27 solved ###
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 算法1： 分治法 ； 算法2 ：tow-pointer，需要对问题进行转换,转换成只含有1-26个元素的时候

        def divideConquer(s):
            count = {}
            for ch in s:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1
            # 是否能解决问题?

            flag = True
            for ch in s:
                if count[ch] < k:
                    flag = False
            if flag:
                return len(s)

            # Divide the string by the chars that appear no more than k times
            start = 0
            ans = 0
            for i in range(len(s)):
                if count[s[i]] < k:
                    ans = max(ans, divideConquer(s[start:i]), )
                    start = i + 1

            return max(ans, divideConquer(s[start:]))

        return divideConquer(s)

s = Solution()
print(s.longestSubstring("baaabcb",3))