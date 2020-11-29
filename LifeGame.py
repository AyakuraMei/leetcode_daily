'''
根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

1 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
2 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
3 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
4 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbours = [(-1, -1), (0, -1), (1, -1), (-1, 0),
         (1, 0), (-1, 1), (0, 1), (1, 1)] # 方向

        # 边界
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                liveNeighbours = 0
                for neighbour in neighbours:
                    r = row + neighbour[0]
                    c = col + neighbour[1]
                    if(r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        liveNeighbours += 1
                # rule 1 or rule 3
                if(liveNeighbours < 2 or liveNeighbours > 3) and board[row][col] == 1:
                    board[row][col] = -1    # -1 说明这个细胞之前是活的，现在是死的
                # rule 4
                if(board[row][col] == 0 and liveNeighbours == 3):
                    board[row][col] == 2 # 2 代表这个细胞之前是死的，但是现在是活的
        
        for row in range(rows):
            for col in range(cols):
                if(board[row][col] > 0):
                    board[row][col] = 1
                else:
                    board[row][col] = 0