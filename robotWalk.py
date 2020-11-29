'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
'''

import math

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = 0
        moveDirection = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        moveTrack = list()
        stack = list()
        stack.append([0, 0]])
        while len(stack) != 0:
            now = stack.pop()
            for i in range(moveDirection):
                if now[0] + i[0] >= 0 and now[1] + i[1] >= 0 and now[0] + i[0] <= m - 1 and now[1] + i[1] <= n - 1:
                    if self.getDigit(now[0] + i[0]) + self.getDigit(now[1] + now[1]) <= k and [now[0] + i[0], now[1], i[1]] not in moveTrack:
                        stack.append([now[0] + i[0], now[1] + i[1]])
                        moveTrack.append([now[0] + i[0], now[1] + i[1]])
                        ans += 1
        return ans
    
    def getDigit(self, num):
        res = 0
        while num != 0:
            res += math.floor(num % 10)
            num = num // 10
        return res

    def movingCount(self, m:int, n: int, k: int) -> int:    # 优化后
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x <= m - 1 and 0 <= y <= n - 1 and self.getDigit(x) + self.getDigit(y) <= k:
                s.add(x, y)
                for xx, yy in [(x + 1, y), (x, y + 1)]:
                    q.put((xx, yy))
        return len(s)