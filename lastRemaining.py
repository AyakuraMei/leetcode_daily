'''
    约瑟夫环
'''

class Solution:
    def lastRemaining(self, n: int, m: int,) -> int:
        ans = 0
        # 最后一轮只剩下两个人
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans

# asds
