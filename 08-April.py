from collections import defaultdict
       
class Solution:
    def isBridge(self, V, edges, c, d):
        
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(node, visited):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited)
        visited = [False]*V
        components_before=0
        for i in range(V):
            if not visited[i]:
                components_before += 1
                dfs(i, visited)
        
        if d in adj[c]:
            adj[c].remove(d)
        if c in adj[d]:
            adj[d].remove(c)
        visited = [False]*V
        components_after = 0
        for i in range(V):
            if not visited[i]:
                components_after +=1
                dfs(i, visited)
        adj[c].append(d)
        adj[d].append(c)
        return 1 if components_after>components_before else 0
    
