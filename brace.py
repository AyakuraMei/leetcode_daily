'''
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''
from typing import List

# dfs
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        currentStr = ''
        def dfs(currentStr, left, right):
            if left == 0 and right == 0:
                res.append(currentStr)
                return
            if right < left:
                return
            if left > 0:
                dfs(currentStr + '(', left - 1, right)
            if right > 0:
                dfs(currentStr + ')', left, right - 1)
        dfs(currentStr, n, n)
        return res

# dp
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return 
        
        dp = [None for _ in range(n * 2)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                print(left, right)
                for key1 in left:
                    for key2 in right:
                        cur.append('(' + key1 + ')' + key2)
            dp[i] = cur
        return dp[n]

                

if __name__ == "__main__":
    test = Solution2()
    print(test.generateParenthesis(2))