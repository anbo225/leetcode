### 2018-01-31 solved ###
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def dfs(i, j):
            if j == 9 and i == 0:  # 边界条件
                return True

            if board[i][j] != '.':  # 如果当前位置有值，则搜索一下个位置
                next_i, next_j = getNext(i, j)
                return dfs(next_i, next_j)
            else:  # 当前位置为空位置，搜索下一个位置
                for value in range(1, 10):
                    if validate(i, j, str(value)):  # 这个值可以放置，则尝试
                        board[i][j] = str(value)
                        next_i, next_j = getNext(i, j)
                        if dfs(next_i, next_j):
                            return True
                        board[i][j] = '.'  # 失败，则回溯
                return False  # 所有尝试都失败，则返回false

        def validate(i, j, value):
            # 检查当前行
            for j_index in range(0, 9):
                if value == board[i][j_index] :
                    return False
            # 检查当前列
            for i_index in range(0, 9):
                if value == board[i_index][j] :
                    return False
                    # 检查当前正方形
            for i_index in range(int(i / 3) * 3, int(i / 3) * 3 +3):
                for j_index in range(int(j / 3) * 3, int(j / 3) *3 + 3):
                    if value == board[i_index][j_index] and i != i_index and j != j_index:
                        return False
            return True

        def getNext(i, j):
            i = i + 1
            if i > 8:
                return i % 9, j + 1
            else:
                return i, j

        dfs(0, 0)