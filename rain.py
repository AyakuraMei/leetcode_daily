'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        nowHeight = 0
        ans = 0
        for i in range(1, len(height) - 1): # 最左右两端一定会漏走，所以范围是 [1, len() - 1]
            for j in range(i, len(height)): # 对于向右的每个柱子
                maxRight = max(maxRight, height[j])
            for k in range(i, 0, -1):   # 对于向左的每个柱子
                maxLeft = max(maxLeft, height[k])
            ans += min(maxLeft, maxRight) - height[i]   # 获得两边柱子的最小值，减去当前的柱子
        return ans

class Solution2:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0 for i in range(len(height))]
        maxRight = [0 for i in range(len(height))]
        ans = 0
        for i in range(1, len(height)): # 从左往右
            maxLeft[i] = max(height[i], maxLeft[i - 1])
        for i in range(len(height) - 2, -1, -1):    # 从右往左
            maxRight = max(height[i], maxRight[i + 1])
        for i in range(len(height)):
            ans += min(maxLeft[i], maxRight[i]) - height[i]
        return ans
