class Solution:
    def findMotherVertex(self, V, edges):
        visited = [False] * V
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        
        def dfs(u):
            q = [u]
            while q:
                v = q.pop()
                if visited[v]:
                    continue
                visited[v] = True
                q.extend(adj[v])
        
        last_unvisited_vertex = 0
        for u in range(V):
            if visited[u]:
                continue
            last_unvisited_vertex = u
            dfs(u)
        visited = [False] * V
        dfs(last_unvisited_vertex)
        if all(visited):
            return last_unvisited_vertex
        else:
            return -1
        # code here
