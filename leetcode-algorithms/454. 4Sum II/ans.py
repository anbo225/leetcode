### 2018-01-28 solved ###
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        towSum = {}
        ans = 0
        for a in A:
            for b in B:
                if a + b in towSum:
                    towSum[a + b] += 1
                else:
                    towSum[a + b] = 1

        for c in C:
            for d in D:
                if -c - d in towSum:
                    ans += towSum[-c - d]

        return ans


