# Structure of binary tree node
'''
class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None
'''
class Solution:
    #Complete the function below
    def verticalSum(self, root):
        
        if root==None:
            return [root.data]
        
        leftSize=0
        rightSize=0
  
        firstTime=True
        
        def dfs(curNode,curLine):
            nonlocal firstTime,leftSize,rightSize
            if curNode==None:
                return
            
            if firstTime:
                leftSize=min(leftSize,curLine)
                rightSize=max(rightSize,curLine)
            else:
                lineSum[curLine]+=curNode.data
            
            dfs(curNode.left,curLine-1)
            dfs(curNode.right,curLine+1)
            
        
        dfs(root,0)
        
        leftSize*=-1
        lineSum=[0]*(leftSize+1+rightSize)
        # lineSum[leftSize]=root.data
        firstTime=False
        
        dfs(root,leftSize)
        
        return lineSum
    
        # code here
