'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = none
        self.right = none
'''

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            l = self.isSameTree(p.left, q.left)
            r = self.isSameTree(p.right, q.right)
            return l and r
        else:
            return False
