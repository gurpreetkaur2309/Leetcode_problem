# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer=[]

    def preorder(self,root):
        if root is None:
            return
        
        self.answer.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        # self.answer=[]
        self.preorder(root)
        print(self.answer)
        return self.answer
    
        