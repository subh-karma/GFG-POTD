from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        adj = defaultdict(list)
        
        # Build the adjacency list
        for u, v in edges:
            adj[u].append(v)
        
        visited = [False] * V
        recStack = [False] * V
        
        def dfs(v):
            visited[v] = True
            recStack[v] = True
            
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True
            
            recStack[v] = False
            return False
        
        for node in range(V):
            if not visited[node]:
                if dfs(node):
                    return True
        return False
