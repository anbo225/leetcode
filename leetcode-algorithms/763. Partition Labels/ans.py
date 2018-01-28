### 2018-01-28 solved ###
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 1:
            return [1]

        count = {}
        for ch in S:
            count[ch] = 1 if ch not in count else count[ch] + 1

        ans = []
        counts = count[S[0]] - 1
        partition = [S[0]]
        start = 0
        end = 1

        while (end < len(S)):

            if S[end] in partition:
                counts -= 1
            else:
                if counts == 0:
                    partition = [S[end]]
                    counts = count[S[end]] -1
                    ans.append(end - start)
                    start = end
                else:
                    partition.append(S[end])
                    counts = counts +  count[S[end]] - 1
            end += 1
        ans.append(end - start)
        return ans

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))