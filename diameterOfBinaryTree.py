'''
Question 543
'''
class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(p):
            if not p:
                return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.ans
        
         
        