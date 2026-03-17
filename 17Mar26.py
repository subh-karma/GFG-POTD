'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import defaultdict, deque

class Solution:
    def minTime(self, root, target):
        adjList = defaultdict(set)
        queue = deque([(root)])
        while(queue):
            node = queue.popleft()
            
            if node.left:
                adjList[node.data].add(node.left.data)
                adjList[node.left.data].add(node.data)
                queue.append(node.left)
            if node.right:
                adjList[node.data].add(node.right.data)
                adjList[node.right.data].add(node.data)
                queue.append(node.right)
        
        res = 0
        queue = deque([(target)])
        vis = set([target])
        while queue:
            size = len(queue)
            ok = False
            for _ in range(size):
                src = queue.popleft()
                
                for nbr in adjList[src]:
                    if nbr not in vis:
                        vis.add(nbr)
                        queue.append(nbr)
                        ok = True
            if ok:
                res += 1
        return res


        # code here
