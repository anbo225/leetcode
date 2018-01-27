### 2018-01-27 solved ###
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        rows = [list('QWERTYUIOPqwertyuiop'), list('ASDFGHJKLasdfghjkl'), list('ZXCVBNMzxcvbnm')]

        for word in words:
            flag = True
            for row in rows:
                if word[0] in row:
                    for ch in word:
                        if ch not in row:
                            flag = False
                            break
            if flag:
                res.append(word)
        return res

if __name__ == '__main__':
    s = Solution()
    arg = ["Hello", "Alaska", "Dad", "Peace"]
    print(s.findWords(arg))