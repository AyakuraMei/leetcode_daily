class Solution:
    def isSymmetric(self, root):
        def solve(q, p):
            if p == None:
                return q == None
            if q == None:
                return p == None
            if p.val == q.val:
                return solve(p.left, q.right) and solve(p.right, q.left)
            return False
            
        if root == None:
            return True
        else:
            return solve(root.left, root.right)