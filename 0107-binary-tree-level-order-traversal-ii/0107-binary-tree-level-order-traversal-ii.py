# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1

    def push(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
        
    
    def pop(self):
        if self.front==-1:
            return -1
        
        x=self.q[self.front]
        self.front+=1
        if self.front ==len(self.q):
            self.q=[]
            self.front=-1
        
        return x
    
    def size(self):
        if self.front ==-1:
            return 0
        return len(self.q)-self.front

    def get_front(self):
        if len(self.q)==0:
            return -1
        return self.q[self.front]







class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        queue=Queue()
        if root is None:
            return []
        queue.push(root)
        answer=[]
        answer.append([root.val])

        while(queue.size()>0):
            level=[]
            
            
            for i in range(queue.size()):
                x=queue.pop()
                if x.left != None:
                    queue.push(x.left)
                    level.append(x.left.val)
                if x.right != None:
                    queue.push(x.right)
                    level.append(x.right.val)
            if len(level)>0:
                answer.append(level)
        answer.reverse()
        return answer
            