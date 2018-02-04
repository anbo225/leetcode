### 2018-02-03 solved ###
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # 图的算法
        from collections import defaultdict

        g = defaultdict(dict)
        for (start, end), value in zip(equations, values):
            g[start][end] = value
            g[start][start] = 1
            g[end][start] = 1 / value

        for k in g:
            for i in g[k]:
                for j in g[k]:
                    g[i][j] = g[i][k] * g[k][j]  # i 和 j都是k可达的点

        return [g[start].get(end, -1.0) for start, end in queries]





