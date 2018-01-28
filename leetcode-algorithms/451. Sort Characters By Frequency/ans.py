### 2018-01-28 solved ###
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for ch in s:
            count[ch] = 1 if ch not in count else count[ch] + 1
        valueKeys = sorted(count.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for value, key in valueKeys:
            ans.append(key * value)
        return "".join(ans)


