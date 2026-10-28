# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        result=[]
        self.result=result
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        self.result.append(node.val)
        
        
        
        self.inorder(node.right)
        
        return self.result

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result=[]
        self.inorder(root)
        return self.result
        
        