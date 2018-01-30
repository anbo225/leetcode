### 2018-01-30 solved ###
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==None or len(s)==0:
            return True
        i=0
        j=len(s)-1
        while i <= j:
            if( not s[i].isalnum()):
                i = i+1
                continue
            if( not s[j].isalnum()):
                j = j -1
                continue
            if (s[i].lower() != s[j].lower()):
                return False
            i = i+1
            j = j-1
        return True