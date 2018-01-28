### 2018-01-28 solved ###
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        self.d = {}
        for allow in allowed:
            key = allow[0:2]
            if key in self.d:
                self.d[key].append(allow[2])
            else:
                self.d[key] = list(allow[2])
        return self.dfs(bottom)

    def getValue(self, key):
        if key in self.d:
            return self.d[key]
        else:
            return None

    def findPossibleUpRow(self, bottom, i, ans, upRows):
        values = self.getValue(bottom[i:i+2])
        if values is None:
            return
        else:
            if i == len(bottom) - 2:
                for value in values:
                    upRows.append(ans + value)
            else:
                for value in values:
                    self.findPossibleUpRow(bottom, i + 1, ans + value, upRows)

    def dfs(self, bottom):
        if len(bottom) == 1:
            return True

        # 搜索本层,尝试每一种可行的方法
        upRows = []
        self.findPossibleUpRow(bottom, 0, '', upRows)
        for upRow in upRows:
            if self.dfs(upRow):
                return True

        # 搜索不到，则返回false
        return False

s = Solution()
print(s.pyramidTransition("AABA",["AAA","AAB","ABA","ABB","BAC"]))